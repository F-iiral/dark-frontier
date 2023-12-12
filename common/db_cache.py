from common.lib.user import User
from common.lib.planet import Planet
from common.lib.fleet import Fleet
import time

class DBCache():
    recent_users  : dict[str, User] = {}
    recent_planets: dict[str, Planet] = {}
    recent_fleets : dict[str, Fleet] = {}

    @staticmethod
    def purge_cache():
        for item in set(DBCache.recent_users.items()):
            if time.time() - item[1][1] > 3600:
                item[1].save_to_db()
                del DBCache.recent_users[item[0]]
        
        for item in set(DBCache.recent_planets.items()):
            if time.time() - item[1][1] > 3600:
                item[1].save_to_db()
                del DBCache.recent_planets[item[0]]
        
        for item in set(DBCache.recent_fleets.items()):
            if time.time() - item[1][1] > 3600:
                item[1].save_to_db()
                del DBCache.recent_fleets[item[0]]

    @staticmethod
    def get_user(user_id: int) -> User:
        user_id_str = str(user_id)

        if user_id_str in DBCache.recent_users.keys():
            return DBCache.recent_users[user_id_str][0]
        
        user = User.get_from_db_by_owner(user_id)
        DBCache.recent_users[user_id_str] = (user, time.time())
        return user

    @staticmethod
    def get_planet(planet_id: int) -> Planet:
        planet_id_str = str(planet_id)

        if planet_id_str in DBCache.recent_planets.keys():
            return DBCache.recent_planets[planet_id_str][0]
        
        planet = Planet.get_from_db_by_id(planet_id)
        DBCache.recent_planets[planet_id_str] = (planet, time.time())
        return planet
    
    @staticmethod
    def get_fleet(fleet_id: int) -> Fleet:
        fleet_id_str = str(fleet_id)

        if fleet_id_str in DBCache.recent_fleets.keys():
            return DBCache.recent_fleets[fleet_id_str][0]
        
        fleet = Fleet.get_from_db_by_id(fleet_id)
        DBCache.recent_fleets[fleet_id_str] = (fleet, time.time())
        return fleet