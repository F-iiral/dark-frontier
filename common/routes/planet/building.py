from flask import abort
from common.db_cache import DBCache
from common.enums import PlanetBuildings

def main(planet_id: int, building_type: int) -> tuple | int:
    planet = DBCache.get_planet(planet_id)
    planet.update_resource_count()
    
    if building_type   == PlanetBuildings.METAL_MINE.value:
        building_cost_mult = 480
        building_name = "bld_metal_mine"
        building_resources = [0, 1, 1]
    elif building_type == PlanetBuildings.CRYSTAL_MINE.value:
        building_cost_mult = 480
        building_name = "bld_crystal_mine"
        building_resources = [1, 0, 1]
    elif building_type == PlanetBuildings.GAS_MINE.value:
        building_cost_mult = 480
        building_name = "bld_gas_mine"
        building_resources = [1, 1, 0]
    elif building_type == PlanetBuildings.METAL_STORAGE.value:
        building_cost_mult = 240
        building_name = "bld_metal_storage"
        building_resources = [0, 1, 1]
    elif building_type == PlanetBuildings.CRYSTAL_STORAGE.value:
        building_cost_mult = 240
        building_name = "bld_crystal_storage"
        building_resources = [1, 0, 1]
    elif building_type == PlanetBuildings.GAS_STORAGE.value:
        building_cost_mult = 240
        building_name = "bld_gas_storage"
        building_resources = [1, 1, 0]
    elif building_type == PlanetBuildings.FACTORY.value:
        building_cost_mult = 720
        building_name = "bld_factory"
        building_resources = [1, 1, 0.5]
    elif building_type == PlanetBuildings.SHIPYARD.value:
        building_cost_mult = 480
        building_name = "bld_shipyard"
        building_resources = [1, 0.5, 1]
    elif building_type == PlanetBuildings.LABORATORY.value:
        building_cost_mult = 480
        building_name = "bld_laboratory"
        building_resources = [0.5, 1, 1]
    elif building_type == PlanetBuildings.TERRAFORMER.value:
        building_cost_mult = 720
        building_name = "bld_terraformer"
        building_resources = [1, 1, 1]
    else: return "Invalid building.", 400

    building_cost = building_cost_mult * (1.1486984 ** planet.__getattribute__(building_name))

    if building_cost * building_resources[0] > planet.metal_amount:   return "Insufficent metal resource.", 400
    if building_cost * building_resources[1] > planet.crystal_amount: return "Insufficent crystals resource.", 400
    if building_cost * building_resources[2] > planet.gas_amount:     return "Insufficent gas resource.", 400

    planet.metal_amount   -= building_cost * building_resources[0]
    planet.crystal_amount -= building_cost * building_resources[1]
    planet.gas_amount     -= building_cost * building_resources[2]
    planet.__setattr__(building_name, planet.__getattribute__(building_name) + 1)

    return 200