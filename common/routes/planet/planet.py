from common.db_cache import DBCache

def main(planet_id: int) -> tuple:
    planet = DBCache.get_planet(planet_id)
    if planet is None:                      return "Invalid Planet Id.", 400
    planet.update_resource_count()

    return planet.to_dict(), 200