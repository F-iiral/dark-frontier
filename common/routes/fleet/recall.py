from common.db_cache import DBCache
from common.const import FleetMissions, ConsoleShortcuts
import time

def main(fleet_id: int) -> tuple:
    fleet = DBCache.get_fleet(fleet_id)
    if fleet is None:                       return "Invalid Fleet ID.", 400

    if (fleet.mission == FleetMissions.HOLD.value) or (fleet.mission == FleetMissions.RECALL.value):
        return "Cannot recall a fleet that is holding position or already returning.", 400

    if fleet.arrival_time and fleet.start_time:
        print(f"{ConsoleShortcuts.warn()} Failed to get either start_time or start_time for Fleet {fleet_id}.")
        flight_time = 0
        flown_time = 0
        recall_time = 0
    else:
        flight_time = fleet.arrival_time - fleet.start_time
        flown_time = fleet.arrival_time - time.time()
        recall_time = flight_time - flown_time
    
    if recall_time < 0:
        return "Cannot recall a fleet that has already arrived.", 400
    
    fleet.arrival_time = time.time() + recall_time
    fleet.start_time = time.time()
    fleet.mission = FleetMissions.RECALL.value
    fleet.target = fleet.position
    DBCache.recent_fleets[f'{fleet.fleet_id}'] = (fleet, time.time())
    return "Successfully returning fleet.", 200