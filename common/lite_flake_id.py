import time

class LiteFlakeID():
    epoch = 1672531200
    last_timestamp = 0
    last_sequence = 0
    max_sequence = 31

    @staticmethod
    def generate_id() -> int:
        current_timestamp = int(time.time()) - LiteFlakeID.epoch
        current_sequence = LiteFlakeID.last_sequence

        if current_timestamp == LiteFlakeID.last_timestamp:
            current_sequence = (LiteFlakeID.last_sequence + 1) & LiteFlakeID.max_sequence

        unique_id = (current_timestamp << 5) | current_sequence

        LiteFlakeID.last_timestamp = current_timestamp
        LiteFlakeID.last_sequence = current_sequence
        return unique_id

    @staticmethod
    def get_timestamp(id: int) -> int:
        return (id >> 5) + LiteFlakeID.epoch