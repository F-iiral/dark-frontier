from common.const import FleetMissions, Badges, ShipRanges
from common.db_cache import DBCache
from common.env import STAR_COUNT, SPIRAL_COUNT, STAR_CIRCLE, SPIRAL_CIRCLE, FLEET_SPEED
import time
import math

def main(fleet_id: int, mission: int, target: list[int], speed_factor: float) -> tuple:
    fleet = DBCache.get_fleet(fleet_id)
    if fleet is None:                       return "Invalid Fleet ID.", 400
    if target == fleet.position:            return "Cannot move to same position.", 400
    if 0 > target[0] > SPIRAL_COUNT:        return "Invalid target position (spiral).", 400
    if 0 > target[1] > STAR_COUNT:          return "Invalid target position (star).", 400
    if 0 > target[2] > 16:                  return "Invalid target position (planet).", 400

    target_planet = DBCache.get_planet(int(f'{target[0]}{target[1]}{target[2]}'))
    if target_planet is None:               return "Failed to get planet from DB.", 500

    # TRANSPORT - valid for all planets
    # RECYCLE   - valid for all planets
    # HOLD      - valid for own planets
    # DEPLOY    - valid for own planets
    # COLLECT   - valid for own planets
    # SPY       - valid for foreign planets
    # ATTACK    - valid for foreign planets
    # EXPLORE   - valid for 16th slot
    # COLONIZE  - valid for non-colonized planet

    if not (FleetMissions.HOLD.value <= mission <= FleetMissions.RECYCLE.value):
        return "Unknown mission type.", 400
    if target_planet.owner.account.activity & Badges.VACATION.value == Badges.VACATION.value:
        return "Cannot move to planet in vacation-mode.", 400
    
    if (target_planet.owner_id == fleet.owner_id)       and (mission in [FleetMissions.ATTACK.value, FleetMissions.SPY.value]):
        return "Cannot perform that mission on yourself.", 400
    if not (target_planet.owner_id == fleet.owner_id)   and (mission in [FleetMissions.COLLECT.value, FleetMissions.HOLD.value, FleetMissions.DEPLOY.value]):
        return "Cannot perform that mission on a foreign player."
    if (target_planet.owner == None)                    and not (mission == FleetMissions.COLONIZE.value):
        return "Cannot perform that mission on an uncolonized planet.", 400
    if not (target_planet.owner == None)                and (mission == FleetMissions.COLONIZE.value):
        return "Cannot perform that mission on a colonized planet.", 400
    if (target[2] == 16)                                and not (mission == FleetMissions.EXPLORE.value) :
        return "Cannot perform that mission on a empty tile.", 400
    if not (target[2] == 16)                            and mission == FleetMissions.EXPLORE.value:
        return "Cannot perform that mission on a non-empty tile.", 400

    planet_distance = abs(target[2] - fleet.position[2])
    if STAR_CIRCLE:
        star_distance = math.floor(abs((target[1] - fleet.position[1]) % STAR_COUNT + STAR_COUNT/2))
    else:
        star_distance = abs(target[1] - fleet.position[1])
    if SPIRAL_CIRCLE:
        spiral_distance = math.floor(abs((target[1] - fleet.position[1]) % SPIRAL_COUNT + SPIRAL_COUNT/2))
    else:
        spiral_distance = abs(target[0] - fleet.position[0])
    
    if star_distance > 0 and fleet.get_fleet_range() < ShipRanges.INTERSTELLAR.value:
        return "Fleet does not have enough range for interstellar travel.", 400
    if spiral_distance > 0 and fleet.get_fleet_range() < ShipRanges.GALACTIC.value:
        return "Fleet does not have enough range for galactic travel.", 400

    # Temporary OGame formula
    if spiral_distance == 0:
        if star_distance == 0:
            distance = 3000 + 100 * star_distance
        else:
            distance = 1000 + 5 * planet_distance
    else:
        distance = 20000 * spiral_distance
    
    arrival_time = time.time() + ((10 + 3500/speed_factor + math.sqrt(10 * distance / fleet.get_fleet_speed())) / FLEET_SPEED)

    fleet.arrival_time = arrival_time
    fleet.mission = mission
    DBCache.recent_fleets[f'{fleet.fleet_id}'] = (fleet, time.time())
    return "Successfully moved fleet.", 200