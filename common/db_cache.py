from typing import Never as never
from common.lib.user import User
from common.lib.planet import Planet
from common.lib.fleet import Fleet
from common.const import ConsoleShortcuts, FleetMissions
from common.env import DEV_MODE
import asyncio
import time

class DBCache():
    recent_users  : dict[str, tuple[User, float]] = {}
    recent_planets: dict[str, tuple[Planet, float]] = {}
    recent_fleets : dict[str, tuple[Fleet, float]] = {}

    @staticmethod
    async def purge_cache() -> never:
        if DEV_MODE: delay = 6
        else:        delay = 360

        while True:
            await asyncio.sleep(delay)
            print(f"{ConsoleShortcuts.log()} Purging cache.")
            for item in set(DBCache.recent_users.items()):
                if time.time() - item[1][1] > 10:
                    item[1][0].save_to_db()
                    del DBCache.recent_users[item[0]]

            for item in set(DBCache.recent_planets.items()):
                if time.time() - item[1][1] > 10:
                    item[1][0].save_to_db()
                    del DBCache.recent_planets[item[0]]

            for item in set(DBCache.recent_fleets.items()):
                if not time.time() - item[1][1] > 10:
                    continue

                if item[1][0].mission == FleetMissions.HOLD.value:
                    item[1][0].save_to_db()
                    del DBCache.recent_fleets[item[0]]

    @staticmethod
    def get_user(user_id: int) -> User | None:
        user_id_str = str(user_id)

        if user_id_str in DBCache.recent_users.keys():
            return DBCache.recent_users[user_id_str][0]

        user = User.get_from_db_by_owner(user_id)
        DBCache.recent_users[user_id_str] = (user, time.time())
        return user

    @staticmethod
    def get_planet(planet_id: int) -> Planet | None:
        planet_id_str = str(planet_id)

        if planet_id_str in DBCache.recent_planets.keys():
            return DBCache.recent_planets[planet_id_str][0]

        planet = Planet.get_from_db_by_id(planet_id)
        DBCache.recent_planets[planet_id_str] = (planet, time.time())
        return planet

    @staticmethod
    def get_fleet(fleet_id: int) -> Fleet | None:
        fleet_id_str = str(fleet_id)

        if fleet_id_str in DBCache.recent_fleets.keys():
            return DBCache.recent_fleets[fleet_id_str][0]

        fleet = Fleet.get_from_db_by_id(fleet_id)
        DBCache.recent_fleets[fleet_id_str] = (fleet, time.time())
        return fleet