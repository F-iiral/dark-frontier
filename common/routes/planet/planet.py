from flask import abort
from common.db_cache import DBCache

def main(planet_id: int) -> tuple:
    planet = DBCache.get_planet(planet_id)
    planet.update_resource_count()

    return planet.to_dict(), 200