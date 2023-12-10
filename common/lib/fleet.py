import sqlite3
from common.dev import ConsoleShortcuts
from common.lib.user import User

class Fleet():
    """
    Represents a fleet inside the game.

    Position is stored the following way: [planet, system, arm]
    Target is stored the following way:   [planet, system, arm]
    """

    def __init__(self) -> None:
        ### Owner
        self.owner_id           : int | None    = None
        self.owner              : User | None   = None

        ### Basic Information
        self.fleet_id           : int               = 0
        self.moving             : bool              = False
        self.position           : list[int]         = None
        self.target             : list[int] | None  = None
        self.arrival_time       : float | None      = None

        ### Military
        self.fighters           : float     = 0.0
        self.interceptors       : float     = 0.0
        self.tac_bombers        : float     = 0.0
        self.str_bombers        : float     = 0.0
        self.frigates           : float     = 0.0
        self.destroyers         : float     = 0.0
        self.cruisers           : float     = 0.0
        self.battlecruisers     : float     = 0.0
        self.battleships        : float     = 0.0
        self.escort_carriers    : float     = 0.0
        self.fleet_carriers     : float     = 0.0
        self.titans             : float     = 0.0

        ### Civilian
        self.sattelites         : float     = 0.0
        self.small_cargo_ships  : float     = 0.0
        self.big_cargo_ships    : float     = 0.0
        self.colony_ships       : float     = 0.0
        self.science_ships      : float     = 0.0
        self.construction_ships : float     = 0.0

    def __add__(self, other: 'Fleet') -> 'Fleet':
        if not isinstance(other, Fleet):
            raise TypeError(f"'Fleet' object can only be combined with 'Fleet' not {type(other)}")
        
        combined_fleet = Fleet()
        combined_fleet.owner_id           = self.owner_id
        combined_fleet.owner              = self.owner
        combined_fleet.fleet_id           = self.fleet_id
        combined_fleet.moving             = False
        combined_fleet.position           = self.position          
        combined_fleet.target             = None
        combined_fleet.arrival_time       = None
        combined_fleet.fighters           = self.fighters           + other.fighters
        combined_fleet.interceptors       = self.interceptors       + other.interceptors
        combined_fleet.tac_bombers        = self.tac_bombers        + other.tac_bombers
        combined_fleet.str_bombers        = self.str_bombers        + other.str_bombers
        combined_fleet.frigates           = self.frigates           + other.frigates
        combined_fleet.destroyers         = self.destroyers         + other.destroyers
        combined_fleet.cruisers           = self.cruisers           + other.cruisers
        combined_fleet.battlecruisers     = self.battlecruisers     + other.battlecruisers
        combined_fleet.battleships        = self.battleships        + other.battleships
        combined_fleet.escort_carriers    = self.escort_carriers    + other.escort_carriers
        combined_fleet.fleet_carriers     = self.fleet_carriers     + other.fleet_carriers
        combined_fleet.titans             = self.titans             + other.titans
        combined_fleet.sattelites         = self.sattelites         + other.sattelites
        combined_fleet.small_cargo_ships  = self.small_cargo_ships  + other.small_cargo_ships
        combined_fleet.big_cargo_ships    = self.big_cargo_ships    + other.big_cargo_ships
        combined_fleet.colony_ships       = self.colony_ships       + other.colony_ships
        combined_fleet.science_ships      = self.science_ships      + other.science_ships
        combined_fleet.construction_ships = self.construction_ships + other.construction_ships

        return combined_fleet

    def __sub__(self, other: 'Fleet') -> 'Fleet':
        if not isinstance(other, Fleet):
            raise TypeError(f"'Fleet' object can only be combined with 'Fleet' not {type(other)}")
        
        combined_fleet = Fleet()
        combined_fleet.owner_id           = self.owner_id
        combined_fleet.owner              = self.owner
        combined_fleet.fleet_id           = self.fleet_id
        combined_fleet.moving             = False
        combined_fleet.position           = self.position
        combined_fleet.target             = None
        combined_fleet.arrival_time       = None
        combined_fleet.fighters           = self.fighters           - other.fighters
        combined_fleet.interceptors       = self.interceptors       - other.interceptors
        combined_fleet.tac_bombers        = self.tac_bombers        - other.tac_bombers
        combined_fleet.str_bombers        = self.str_bombers        - other.str_bombers
        combined_fleet.frigates           = self.frigates           - other.frigates
        combined_fleet.destroyers         = self.destroyers         - other.destroyers
        combined_fleet.cruisers           = self.cruisers           - other.cruisers
        combined_fleet.battlecruisers     = self.battlecruisers     - other.battlecruisers
        combined_fleet.battleships        = self.battleships        - other.battleships
        combined_fleet.escort_carriers    = self.escort_carriers    - other.escort_carriers
        combined_fleet.fleet_carriers     = self.fleet_carriers     - other.fleet_carriers
        combined_fleet.titans             = self.titans             - other.titans
        combined_fleet.sattelites         = self.sattelites         - other.sattelites
        combined_fleet.small_cargo_ships  = self.small_cargo_ships  - other.small_cargo_ships
        combined_fleet.big_cargo_ships    = self.big_cargo_ships    - other.big_cargo_ships
        combined_fleet.colony_ships       = self.colony_ships       - other.colony_ships
        combined_fleet.science_ships      = self.science_ships      - other.science_ships
        combined_fleet.construction_ships = self.construction_ships - other.construction_ships

        return combined_fleet

    def to_dict(self, *args):
        return {
            "owner_id": self.owner_id,
            "owner": self.owner.to_dict(),
            "fleet_id": self.fleet_id,
            "moving": self.moving,
            "position": self.position,
            "target": self.target,
            "arrival_time": self.arrival_time,
            "fighters": self.fighters,
            "interceptors": self.interceptors,
            "tac_bombers": self.tac_bombers,
            "str_bombers": self.str_bombers,
            "frigates": self.frigates,
            "destroyers": self.destroyers,
            "cruisers": self.cruisers,
            "battlecruisers": self.battlecruisers,
            "battleships": self.battleships,
            "escort_carriers": self.escort_carriers,
            "fleet_carriers": self.fleet_carriers,
            "titans": self.titans,
            "sattelites": self.sattelites,
            "small_cargo_ships": self.small_cargo_ships,
            "big_cargo_ships": self.big_cargo_ships,
            "colony_ships": self.colony_ships,
            "science_ships": self.science_ships,
            "construction_ships": self.construction_ships
        }

    def save_to_db(self) -> None:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO fleets (
                fleet_id, owner_id, moving, position_planet, position_system, position_spiral,
                target_planet, target_system, target_spiral, arrival_time,
                fighters, interceptors, tac_bombers, str_bombers, frigates, destroyers,
                cruisers, battlecruisers, battleships, escort_carriers, fleet_carriers, titans,
                sattelites, small_cargo_ships, big_cargo_ships, colony_ships, science_ships,
                construction_ships
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.fleet_id, self.owner_id, int(self.moving), self.position[0], self.position[1], self.position[2],
            self.target[0] if self.target else None, self.target[1] if self.target else None, self.target[2] if self.target else None,
            self.arrival_time, self.fighters, self.interceptors, self.tac_bombers, self.str_bombers,
            self.frigates, self.destroyers, self.cruisers, self.battlecruisers, self.battleships,
            self.escort_carriers, self.fleet_carriers, self.titans, self.sattelites, self.small_cargo_ships,
            self.big_cargo_ships, self.colony_ships, self.science_ships, self.construction_ships
        ))

        conn.commit()
        conn.close()
    
    @staticmethod
    def get_from_db_by_owner(account_id: int) -> 'Fleet':
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                fleet_id, owner_id, moving, position_planet, position_system, position_spiral,
                target_planet, target_system, target_spiral, arrival_time,
                fighters, interceptors, tac_bombers, str_bombers,
                frigates, destroyers, cruisers, battlecruisers, battleships,
                escort_carriers, fleet_carriers, titans, sattelites, small_cargo_ships,
                big_cargo_ships, colony_ships, science_ships, construction_ships
            FROM fleets
            WHERE owner_id = ?
        """, (account_id,))

        fleet_data = cursor.fetchone()
        conn.close()
        if fleet_data is None:
            print(f"{ConsoleShortcuts.warn()} Could not find 'fleet' by owner ID {account_id}.")
            return fleet_data

        fleet = Fleet()
        fleet.fleet_id           = fleet_data[0]
        fleet.owner_id           = fleet_data[1]
        fleet.owner              = User.get_from_db_by_owner(fleet_data[1])
        fleet.moving             = bool(fleet_data[2])
        fleet.position           = [fleet_data[3], fleet_data[4], fleet_data[5]]
        fleet.target             = [fleet_data[6], fleet_data[7], fleet_data[8]] if fleet_data[6] is not None else None
        fleet.arrival_time       = float(fleet_data[9])                          if fleet_data[9] is not None else None
        fleet.fighters           = float(fleet_data[10])
        fleet.interceptors       = float(fleet_data[11])
        fleet.tac_bombers        = float(fleet_data[12])
        fleet.str_bombers        = float(fleet_data[13])
        fleet.frigates           = float(fleet_data[14])
        fleet.destroyers         = float(fleet_data[15])
        fleet.cruisers           = float(fleet_data[16])
        fleet.battlecruisers     = float(fleet_data[17])
        fleet.battleships        = float(fleet_data[18])
        fleet.escort_carriers    = float(fleet_data[19])
        fleet.fleet_carriers     = float(fleet_data[20])
        fleet.titans             = float(fleet_data[21])
        fleet.sattelites         = float(fleet_data[22])
        fleet.small_cargo_ships  = float(fleet_data[23])
        fleet.big_cargo_ships    = float(fleet_data[24])
        fleet.colony_ships       = float(fleet_data[25])
        fleet.science_ships      = float(fleet_data[26])
        fleet.construction_ships = float(fleet_data[27])

        return fleet

    @staticmethod
    def get_from_db_by_id(fleet_id: int) -> 'Fleet':
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                fleet_id, owner_id, moving, position_planet, position_system, position_spiral,
                target_planet, target_system, target_spiral, arrival_time,
                fighters, interceptors, tac_bombers, str_bombers,
                frigates, destroyers, cruisers, battlecruisers, battleships,
                escort_carriers, fleet_carriers, titans, sattelites, small_cargo_ships,
                big_cargo_ships, colony_ships, science_ships, construction_ships
            FROM fleets
            WHERE fleet_id = ?
        """, (fleet_id,))

        fleet_data = cursor.fetchone()
        conn.close()
        if fleet_data is None:
            print(f"{ConsoleShortcuts.warn()} Could not find 'fleet' by fleet ID {fleet_id}.")
            return fleet_data

        fleet = Fleet()
        fleet.fleet_id           = fleet_data[0]
        fleet.owner_id           = fleet_data[1]
        fleet.owner              = User.get_from_db_by_owner(fleet_data[1])
        fleet.moving             = bool(fleet_data[2])
        fleet.position           = [fleet_data[3], fleet_data[4], fleet_data[5]]
        fleet.target             = [fleet_data[6], fleet_data[7], fleet_data[8]] if fleet_data[6] is not None else None
        fleet.arrival_time       = float(fleet_data[9])                          if fleet_data[9] is not None else None
        fleet.fighters           = float(fleet_data[10])
        fleet.interceptors       = float(fleet_data[11])
        fleet.tac_bombers        = float(fleet_data[12])
        fleet.str_bombers        = float(fleet_data[13])
        fleet.frigates           = float(fleet_data[14])
        fleet.destroyers         = float(fleet_data[15])
        fleet.cruisers           = float(fleet_data[16])
        fleet.battlecruisers     = float(fleet_data[17])
        fleet.battleships        = float(fleet_data[18])
        fleet.escort_carriers    = float(fleet_data[19])
        fleet.fleet_carriers     = float(fleet_data[20])
        fleet.titans             = float(fleet_data[21])
        fleet.sattelites         = float(fleet_data[22])
        fleet.small_cargo_ships  = float(fleet_data[23])
        fleet.big_cargo_ships    = float(fleet_data[24])
        fleet.colony_ships       = float(fleet_data[25])
        fleet.science_ships      = float(fleet_data[26])
        fleet.construction_ships = float(fleet_data[27])

        return fleet