from flask import abort
from common.db_cache import DBCache

def main(planet_id: int) -> tuple:
    planet = DBCache.get_planet(planet_id)

    return planet.__dict__