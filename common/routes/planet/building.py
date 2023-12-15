from flask import abort
from common.db_cache import DBCache
from common.enums import PlanetBuildings

def main(planet_id: int, building_type: int) -> tuple | int:
    planet = DBCache.get_planet(planet_id)
    if planet is None:                      return "Invalid Planet Id.", 400
    planet.update_resource_count()
    
    building_mapping = {
        PlanetBuildings.METAL_MINE.value:      ("bld_metal_mine",      [0, 1, 1],   480),
        PlanetBuildings.CRYSTAL_MINE.value:    ("bld_crystal_mine",    [1, 0, 1],   480),
        PlanetBuildings.GAS_MINE.value:        ("bld_gas_mine",        [1, 1, 0],   480),
        PlanetBuildings.METAL_STORAGE.value:   ("bld_metal_storage",   [0, 1, 1],   240),
        PlanetBuildings.CRYSTAL_STORAGE.value: ("bld_crystal_storage", [1, 0, 1],   240),
        PlanetBuildings.GAS_STORAGE.value:     ("bld_gas_storage",     [1, 1, 0],   240),
        PlanetBuildings.FACTORY.value:         ("bld_factory",         [1, 1, 0.5], 720),
        PlanetBuildings.SHIPYARD.value:        ("bld_shipyard",        [1, 0.5, 1], 480),
        PlanetBuildings.LABORATORY.value:      ("bld_laboratory",      [0.5, 1, 1], 480),
        PlanetBuildings.TERRAFORMER.value:     ("bld_terraformer",     [1, 1, 1],   720),
    }
    building_info = building_mapping.get(building_type)
    if building_info is None:
        return "Invalid building.", 400
    
    building_name, building_resources, building_cost_mult = building_info

    building_cost = building_cost_mult * (1.4142135 ** planet.__getattribute__(building_name)) / (planet.bld_factory + 1)

    if building_cost * building_resources[0] > planet.metal_amount:   return "Insufficent metal resource.", 400
    if building_cost * building_resources[1] > planet.crystal_amount: return "Insufficent crystals resource.", 400
    if building_cost * building_resources[2] > planet.gas_amount:     return "Insufficent gas resource.", 400

    planet.metal_amount   -= building_cost * building_resources[0]
    planet.crystal_amount -= building_cost * building_resources[1]
    planet.gas_amount     -= building_cost * building_resources[2]
    planet.__setattr__(building_name, planet.__getattribute__(building_name) + 1)

    return "Successfully constructed.", 200