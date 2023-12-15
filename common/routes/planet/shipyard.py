from flask import abort
from common.lib.fleet import Fleet
from common.db_cache import DBCache
from common.enums import FleetShips

def main(planet_id: int, ship_type: int, ship_amount: int) -> tuple:
    planet = DBCache.get_planet(planet_id)
    if planet is None:                      return "Invalid Planet Id.", 400
    planet.update_resource_count()

    ship_mapping = {
        FleetShips.FIGHTERS.value:           ("fighters",           [0.5, 1,   0.5],      6000), #  1 min for lvl 10 mine
        FleetShips.INTERCEPTORS.value:       ("interceptors",       [0.5, 0.5, 1.0],      6000), #  1 min for lvl 10 mine
        FleetShips.TAC_BOMBERS.value:        ("tac_bombers",        [1,   0.5, 0.5],      6000), #  1 min for lvl 10 mine
        FleetShips.STR_BOMBERS.value:        ("str_bombers",        [1,   0.5, 0.5],     30000), #  5 min for lvl 10 mine
        FleetShips.FRIGATES.value:           ("frigates",           [1,   0.8, 0.2],    180000), # 30 min for lvl 10 mine
        FleetShips.DESTROYERS.value:         ("destroyers",         [1,   0.7, 0.5],    725000), #    2 h for lvl 10 mine
        FleetShips.CRUISERS.value:           ("cruisers",           [1,   0.7, 0.5],   2500000), #    2 h for lvl 30 mine
        FleetShips.BATTLECRUISERS.value:     ("battlecruisers",     [1,   0.7, 0.5],   3800000), #    2 h for lvl 45 mine
        FleetShips.BATTLESHIPS.value:        ("battleships",        [1,   0.8, 1.5],  15000000), #    8 h for lvl 45 mine
        FleetShips.ESCORT_CARRIERS.value:    ("escort_carriers",    [0.7, 1,   0.5],   2500000), #    2 h for lvl 30 mine
        FleetShips.FLEET_CARRIERS.value:     ("fleet_carriers",     [0.7, 1,   0.5],  15000000), #    8 h for lvl 45 mine
        FleetShips.TITANS.value:             ("titans",             [1,   0.8, 0.5], 180000000), #   96 h for lvl 45 mine
        FleetShips.SATTELITES.value:         ("sattelites",         [0,   1,  0.25],      6000), #  1 min for lvl 10 mine
        FleetShips.SMALL_CARGO_SHIPS.value:  ("small_cargo_ships",  [0.6, 0.6,   1],     30000), #  5 min for lvl 10 mine
        FleetShips.BIG_CARGO_SHIPS.value:    ("big_cargo_ships",    [0.6, 0.6,   1],    725000), #  2 h   for lvl 10 mine
        FleetShips.COLONY_SHIPS.value:       ("colony_ships",       [1,   0.5, 0.7],     30000), #  5 min for lvl 10 mine
        FleetShips.SCIENCE_SHIPS.value:      ("science_ships",      [1,   0.5, 0.7],     30000), #  5 min for lvl 10 mine
        FleetShips.CONSTRUCTION_SHIPS.value: ("construction_ships", [1,   0.5, 0.7],     30000), #  5 min for lvl 10 mine
    }
    ship_info = ship_mapping.get(ship_type)
    if ship_info is None:
        return "Invalid ship.", 400

    ship_name, ship_resources, ship_cost_mult = ship_info

    building_cost_metal_limited   = planet.metal_amount / ((planet.bld_factory + 1) * ship_cost_mult * ship_resources[0])
    building_cost_crystal_limited = planet.crystal_amount / ((planet.bld_factory + 1) * ship_cost_mult * ship_resources[1])
    building_cost_gas_limited     = planet.gas_amount / ((planet.bld_factory + 1) * ship_cost_mult * ship_resources[2])

    ship_amount = int(min(ship_amount, building_cost_metal_limited, building_cost_crystal_limited, building_cost_gas_limited))

    planet.metal_amount   -= ship_amount * ship_cost_mult * ship_resources[0]
    planet.crystal_amount -= ship_amount * ship_cost_mult * ship_resources[1]
    planet.gas_amount     -= ship_amount * ship_cost_mult * ship_resources[2]

    if planet.stationed_fleet is not None:
        planet.stationed_fleet.__setattr__(ship_name, planet.stationed_fleet.__getattribute__(ship_name) + ship_amount)
    else:
        new_fleet = Fleet()
        new_fleet.owner_id = new_fleet.owner_id
        new_fleet.owner = planet.owner
        new_fleet.__setattr__(ship_name, ship_amount)
        planet.stationed_fleet = new_fleet
        planet.stationed_fleet_id = new_fleet.fleet_id

    return "Successfully constructed.", 200