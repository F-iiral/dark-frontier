from flask import abort, jsonify
from common.db_cache import DBCache
from common.lib.planet import Planet
import random

def main(planet_id: int, auth_token: str) -> tuple:
    planet = DBCache.get_planet(planet_id)
    if planet is None:                      return "Invalid 'Planet ID'.", 400
    planet.update_resource_count()

    actor = DBCache.get_user(int(auth_token.split(".")[0], base=16))
    enemy_tech = planet.owner.tec_computing if planet.owner is not None else 0
    tech_difference = actor.tec_computing - enemy_tech

    if actor.id == planet.owner.id:         return "You cannot spy on yourself.", 400

    if tech_difference >= 5:
        data = _create_spy_report(
            planet=planet,
            scan_level="perfect",
            defenses_diff=0,
            building_diff=0,
            resources_diff=0,
            fleet_visible=True,
        )
    elif tech_difference >= 3:
        data = _create_spy_report(
            planet=planet,
            scan_level="great",
            defenses_diff=0.1,
            building_diff=0,
            resources_diff=0,
            fleet_visible=True,
        )
    elif tech_difference >= 2:
        data = _create_spy_report(
            planet=planet,
            scan_level="good",
            defenses_diff=0.15,
            building_diff=0.15,
            resources_diff=0,
            fleet_visible=True,
        )
    elif tech_difference >= 1:
        data = _create_spy_report(
            planet=planet,
            scan_level="satisfactory",
            defenses_diff=0.2,
            building_diff=0.3,
            resources_diff=0,
            fleet_visible=False,
        )
    elif tech_difference == 0:
        data = _create_spy_report(
            planet=planet,
            scan_level="okay",
            defenses_diff=0.25,
            building_diff=1,
            resources_diff=0.1,
            fleet_visible=False,
        )
    elif tech_difference >= -1: # Bad Scan | Defenses: 30%, Buildings: Invisible, Resources: 20%, Fleet: Invisible
        data = _create_spy_report(
            planet=planet,
            scan_level="bad",
            defenses_diff=0.3,
            building_diff=1,
            resources_diff=0.2,
            fleet_visible=False,
        )
    elif tech_difference >= -2: # Terrible | Defenses: 35%, Buildings: Invisible, Resources: 30%, Fleet: Invisible
        data = _create_spy_report(
            planet=planet,
            scan_level="terrible",
            defenses_diff=0.35,
            building_diff=1,
            resources_diff=0.3,
            fleet_visible=False,
        )
    elif tech_difference >= -3:
        data = _create_spy_report(
            planet=planet,
            scan_level="failed",
            defenses_diff=1,
            building_diff=1,
            resources_diff=1,
            fleet_visible=False,
        )
    
    return jsonify(data), 200

def _create_spy_report(planet: Planet, scan_level: str, defenses_diff: float, building_diff: float, resources_diff: float, fleet_visible: bool) -> dict:
    return {
        "scan_level": scan_level,
        "metal_amount": round(random.normalvariate(mu=planet.metal_amount, sigma=planet.metal_amount * resources_diff)) if resources_diff != 1 else "unknown",
        "crystal_amount": round(random.normalvariate(mu=planet.crystal_amount, sigma=planet.crystal_amount * resources_diff)) if resources_diff != 1 else "unknown",
        "gas_amount": round(random.normalvariate(mu=planet.gas_amount, sigma=planet.gas_amount * resources_diff)) if resources_diff != 1 else "unknown",
        "stationed_fleet": (planet.stationed_fleet.to_dict() if planet.stationed_fleet is not None else None) if fleet_visible else "unknown",
        "bld_metal_mine": round(random.normalvariate(mu=planet.bld_metal_mine, sigma=planet.bld_metal_mine * building_diff)) if building_diff != 1 else "unknown",
        "bld_crystal_mine": round(random.normalvariate(mu=planet.bld_crystal_mine, sigma=planet.bld_crystal_mine * building_diff)) if building_diff != 1 else "unknown",
        "bld_gas_mine": round(random.normalvariate(mu=planet.bld_gas_mine, sigma=planet.bld_gas_mine * building_diff)) if building_diff != 1 else "unknown",
        "bld_metal_storage": round(random.normalvariate(mu=planet.bld_metal_storage, sigma=planet.bld_metal_storage * building_diff)) if building_diff != 1 else "unknown",
        "bld_crystal_storage": round(random.normalvariate(mu=planet.bld_crystal_storage, sigma=planet.bld_crystal_storage * building_diff)) if building_diff != 1 else "unknown",
        "bld_gas_storage": round(random.normalvariate(mu=planet.bld_gas_storage, sigma=planet.bld_gas_storage * building_diff)) if building_diff != 1 else "unknown",
        "bld_factory": round(random.normalvariate(mu=planet.bld_factory, sigma=planet.bld_factory * building_diff)) if building_diff != 1 else "unknown",
        "bld_shipyard": round(random.normalvariate(mu=planet.bld_shipyard, sigma=planet.bld_shipyard * building_diff)) if building_diff != 1 else "unknown",
        "bld_laboratory": round(random.normalvariate(mu=planet.bld_laboratory, sigma=planet.bld_laboratory * building_diff)) if building_diff != 1 else "unknown",
        "bld_terraformer": round(random.normalvariate(mu=planet.bld_terraformer, sigma=planet.bld_terraformer * building_diff)) if building_diff != 1 else "unknown",
        "def_aa": round(random.normalvariate(mu=planet.def_aa, sigma=planet.def_aa * defenses_diff)) if defenses_diff != 1 else "unknown",
        "def_rocket": round(random.normalvariate(mu=planet.def_rocket, sigma=planet.def_rocket * defenses_diff)) if defenses_diff != 1 else "unknown",
        "def_railgun": round(random.normalvariate(mu=planet.def_railgun, sigma=planet.def_railgun * defenses_diff)) if defenses_diff != 1 else "unknown",
        "def_laser": round(random.normalvariate(mu=planet.def_laser, sigma=planet.def_laser * defenses_diff)) if defenses_diff != 1 else "unknown",
        "def_ion": round(random.normalvariate(mu=planet.def_ion, sigma=planet.def_ion * defenses_diff)) if defenses_diff != 1 else "unknown",
        "def_plasma": round(random.normalvariate(mu=planet.def_plasma, sigma=planet.def_plasma * defenses_diff)) if defenses_diff != 1 else "unknown",
        "def_disruptor": round(random.normalvariate(mu=planet.def_disruptor, sigma=planet.def_disruptor * defenses_diff)) if defenses_diff != 1 else "unknown",
        "def_s_shield": planet.def_s_shield if defenses_diff > 0.3 else "unknown",
        "def_m_shield": planet.def_m_shield if defenses_diff > 0.25 else "unknown",
        "def_l_shield": planet.def_l_shield if defenses_diff > 0.2 else "unknown",
    }