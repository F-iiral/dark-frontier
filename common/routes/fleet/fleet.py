from common.db_cache import DBCache

def main(fleet_id: int) -> tuple:
    fleet = DBCache.get_fleet(fleet_id)
    if fleet is None:                      return "Invalid Fleet Id.", 400

    return fleet.to_dict(), 200