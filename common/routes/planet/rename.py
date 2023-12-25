from common.db_cache import DBCache
from common.const import PlanetBuildings

def main(planet_id: int, new_name: str) -> tuple:
    planet = DBCache.get_planet(planet_id)
    if planet is None:                      return "Invalid Planet Id.", 400
    planet.update_resource_count()

    if len(new_name) > 256:                 return "Name may only be 256 characters long.", 400
    if len(new_name) < 4:                   return "Name must be longer than 4 characters long.", 400

    planet.name = new_name
    planet.save_to_db()

    return "Successfully renamed.", 200