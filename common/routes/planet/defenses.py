from flask import abort
from common.db_cache import DBCache
from common.enums import PlanetDefenses

def main(planet_id: int, defense_type: int, defense_amount: int) -> tuple:
    planet = DBCache.get_planet(planet_id)
    if planet is None:                      return "Invalid Planet Id.", 400
    planet.update_resource_count()

    defense_mapping = {
        PlanetDefenses.AA_GUN.value:    ("def_aa",        [1,   0,     0],     6000, False), #  1 min for lvl 10 mine
        PlanetDefenses.ROCKET.value:    ("def_rocket",    [1,   0.1,   0],    30000, False), #  5 min for lvl 10 mine
        PlanetDefenses.RAILGUN.value:   ("def_railgun",   [1,   0.5, 0.5],    30000, False), #  5 min for lvl 10 mine
        PlanetDefenses.LASER.value:     ("def_laser",     [0.5, 1,   0.5],   750000, False), #    1 h for lvl 20 mine
        PlanetDefenses.ION.value:       ("def_ion",       [0.4, 1,   0.5],  1200000, False), #    1 h for lvl 30 mine
        PlanetDefenses.PLASMA.value:    ("def_plasma",    [0.3, 1,   0.5],  1650000, False), #    1 h for lvl 40 mine
        PlanetDefenses.DISRUPTOR.value: ("def_disruptor", [0.2, 1,   0.5],  2100000, False), #    1 h for lvl 50 mine
        PlanetDefenses.SHIELD_S.value:  ("def_s_shield",  [0.2, 1,   0.5],   180000, True),  # 30 min for lvl 10 mine
        PlanetDefenses.SHIELD_M.value:  ("def_m_shield",  [0.2, 1,   0.5],  3800000, True),  #    2 h for lvl 45 mine
        PlanetDefenses.SHIELD_L.value:  ("def_l_shield",  [0.2, 1,   0.5], 15000000, True),  #    8 h for lvl 45 mine
    }
    defense_info = defense_mapping.get(defense_type)
    if defense_info is None:
        return "Invalid defense.", 400

    defense_name, defense_resources, defense_cost_mult, defense_is_unique = defense_info

    if not defense_is_unique:
        building_cost_metal_limited   = (planet.metal_amount / ((planet.bld_factory + 1) * defense_cost_mult * defense_resources[0]))   if defense_resources[0] != 0 else float('inf')
        building_cost_crystal_limited = (planet.crystal_amount / ((planet.bld_factory + 1) * defense_cost_mult * defense_resources[1])) if defense_resources[1] != 0 else float('inf')
        building_cost_gas_limited     = (planet.gas_amount / ((planet.bld_factory + 1) * defense_cost_mult * defense_resources[2]))     if defense_resources[2] != 0 else float('inf')

        defense_amount = int(min(defense_amount, building_cost_metal_limited, building_cost_crystal_limited, building_cost_gas_limited))

        planet.metal_amount   -= defense_amount * defense_cost_mult * defense_resources[0]
        planet.crystal_amount -= defense_amount * defense_cost_mult * defense_resources[1]
        planet.gas_amount     -= defense_amount * defense_cost_mult * defense_resources[2]
        planet.__setattr__(defense_name, planet.__getattribute__(defense_name) + defense_amount)
    elif (defense_is_unique) and (not planet.__getattribute__(defense_name)):
        building_cost_metal   = defense_cost_mult * defense_resources[0] / (planet.bld_factory + 1)
        building_cost_crystal = defense_cost_mult * defense_resources[1] / (planet.bld_factory + 1)
        building_cost_gas     = defense_cost_mult * defense_resources[2] / (planet.bld_factory + 1)

        if building_cost_metal   > planet.metal_amount:     return "Insufficent metal resource.", 400
        if building_cost_crystal > planet.crystal_amount:   return "Insufficent crystals resource.", 400
        if building_cost_gas     > planet.gas_amount:       return "Insufficent gas resource.", 400

        planet.metal_amount   -= building_cost_metal
        planet.crystal_amount -= building_cost_crystal
        planet.gas_amount     -= building_cost_gas
        planet.__setattr__(defense_name, True)
    else:
        return "Invalid defense or already constructed.", 400

    return "Successfully constructed.", 200