from flask import abort
from common.db_cache import DBCache
from common.enums import FleetShips

def main(planet_id: int, ship_type: int, ship_amount: int) -> tuple:
    return abort(501) # not thoroughly tested & no fixed cost
    planet = DBCache.get_planet(planet_id)
    planet.update_resource_count()

    defense_mapping = {
        FleetShips.FIGHTERS.value:           ("fighters",           [1, 1, 1], 1),
        FleetShips.INTERCEPTORS.value:       ("interceptors",       [1, 1, 1], 1),
        FleetShips.TAC_BOMBERS.value:        ("tac_bombers",        [1, 1, 1], 1),
        FleetShips.STR_BOMBERS.value:        ("str_bombers",        [1, 1, 1], 1),
        FleetShips.FRIGATES.value:           ("frigates",           [1, 1, 1], 1),
        FleetShips.DESTROYERS.value:         ("destroyers",         [1, 1, 1], 1),
        FleetShips.CRUISERS.value:           ("cruisers",           [1, 1, 1], 1),
        FleetShips.BATTLECRUISERS.value:     ("battlecruisers",     [1, 1, 1], 1),
        FleetShips.BATTLESHIPS.value:        ("battleships",        [1, 1, 1], 1),
        FleetShips.ESCORT_CARRIERS.value:    ("escort_carriers",    [1, 1, 1], 1),
        FleetShips.FLEET_CARRIERS.value:     ("fleet_carriers",     [1, 1, 1], 1),
        FleetShips.TITANS.value:             ("titans",             [1, 1, 1], 1),
        FleetShips.SATTELITES.value:         ("sattelites",         [1, 1, 1], 1),
        FleetShips.SMALL_CARGO_SHIPS.value:  ("small_cargo_ships",  [1, 1, 1], 1),
        FleetShips.BIG_CARGO_SHIPS.value:    ("big_cargo_ships",    [1, 1, 1], 1),
        FleetShips.COLONY_SHIPS.value:       ("colony_ships",       [1, 1, 1], 1),
        FleetShips.SCIENCE_SHIPS.value:      ("science_ships",      [1, 1, 1], 1),
        FleetShips.CONSTRUCTION_SHIPS.value: ("construction_ships", [1, 1, 1], 1),
    }
    ship_info = defense_mapping.get(ship_type)
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
    planet.__setattr__(ship_name, planet.__getattribute__(ship_name) + ship_amount)

    return 200