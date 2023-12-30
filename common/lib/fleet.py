import sqlite3
from common.lite_flake_id import LiteFlakeID
from common.const import ConsoleShortcuts, FleetMissions, ShipRanges, ship_statistics_record
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
        self.fleet_id           : int               = LiteFlakeID.generate_id()
        self.mission            : int               = FleetMissions.HOLD.value
        self.position           : list[int] | None  = None
        self.target             : list[int] | None  = None
        self.arrival_time       : float | None      = None
        self.start_time         : float | None      = None

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
        combined_fleet.mission            = FleetMissions.HOLD.value
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
        combined_fleet.mission            = FleetMissions.HOLD.value
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

    def to_dict(self, *args) -> dict:
        return {
            "owner_id": self.owner_id,
            "owner": self.owner.to_dict() if self.owner is not None else None,
            "fleet_id": self.fleet_id,
            "mission": self.mission,
            "position": self.position,
            "target": self.target,
            "arrival_time": self.arrival_time,
            "start_time": self.start_time,
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

    def get_fleet_worth(self) -> float:
        return (self.fighters             *      6000 * 2.0
                + self.interceptors       *      6000 * 2.0
                + self.tac_bombers        *      6000 * 2.0
                + self.str_bombers        *     30000 * 2.0
                + self.frigates           *    180000 * 2.0
                + self.destroyers         *    725000 * 2.2
                + self.cruisers           *   2500000 * 2.2
                + self.battlecruisers     *   3800000 * 2.2
                + self.battleships        *  15000000 * 3.3
                + self.escort_carriers    *   2500000 * 2.2
                + self.fleet_carriers     *  15000000 * 2.2
                + self.titans             * 180000000 * 2.3
                + self.sattelites         *      6000 * 1.25
                + self.small_cargo_ships  *     30000 * 2.2
                + self.big_cargo_ships    *    725000 * 2.2
                + self.colony_ships       *     30000 * 2.2
                + self.science_ships      *     30000 * 2.2
                + self.construction_ships *     30000 * 2.2)
    
    def get_fleet_speed(self) -> float:
        values = []
        if self.fighters            > 0: values.append(ship_statistics_record["ship_fighter"].speed)
        if self.interceptors        > 0: values.append(ship_statistics_record["ship_interceptor"].speed)
        if self.tac_bombers         > 0: values.append(ship_statistics_record["ship_tac_bomber"].speed)
        if self.str_bombers         > 0: values.append(ship_statistics_record["ship_str_bomber"].speed)
        if self.frigates            > 0: values.append(ship_statistics_record["ship_frigate"].speed)
        if self.destroyers          > 0: values.append(ship_statistics_record["ship_destroyer"].speed)
        if self.cruisers            > 0: values.append(ship_statistics_record["ship_cruiser"].speed)
        if self.battlecruisers      > 0: values.append(ship_statistics_record["ship_battlecruiser"].speed)
        if self.battleships         > 0: values.append(ship_statistics_record["ship_battleship"].speed)
        if self.escort_carriers     > 0: values.append(ship_statistics_record["ship_escort_carrier"].speed)
        if self.fleet_carriers      > 0: values.append(ship_statistics_record["ship_fleet_carrier"].speed)
        if self.titans              > 0: values.append(ship_statistics_record["ship_titan"].speed)
        if self.sattelites          > 0: values.append(ship_statistics_record["ship_sattelites"].speed)
        if self.small_cargo_ships   > 0: values.append(ship_statistics_record["ship_small_cargo"].speed)
        if self.big_cargo_ships     > 0: values.append(ship_statistics_record["ship_large_cargo"].speed)
        if self.colony_ships        > 0: values.append(ship_statistics_record["ship_colony_ship"].speed)
        if self.science_ships       > 0: values.append(ship_statistics_record["ship_science_ship"].speed)
        if self.construction_ships  > 0: values.append(ship_statistics_record["ship_construction_ship"].speed)

        return min(values)

    def get_fleet_range(self) -> int:
        return ShipRanges.GALACTIC.value

    def save_to_db(self) -> None:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO fleets (
                fleet_id, owner_id, mission, position_planet, position_system, position_spiral,
                target_planet, target_system, target_spiral, arrival_time, start_time,
                fighters, interceptors, tac_bombers, str_bombers, frigates, destroyers,
                cruisers, battlecruisers, battleships, escort_carriers, fleet_carriers, titans,
                sattelites, small_cargo_ships, big_cargo_ships, colony_ships, science_ships,
                construction_ships
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.fleet_id, self.owner_id, self.mission, self.position[0], self.position[1], self.position[2],
            self.target[0] if self.target else None, self.target[1] if self.target else None, self.target[2] if self.target else None,
            self.arrival_time, self.start_time, self.fighters, self.interceptors, self.tac_bombers, self.str_bombers,
            self.frigates, self.destroyers, self.cruisers, self.battlecruisers, self.battleships,
            self.escort_carriers, self.fleet_carriers, self.titans, self.sattelites, self.small_cargo_ships,
            self.big_cargo_ships, self.colony_ships, self.science_ships, self.construction_ships
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_from_db_by_owner(account_id: int) -> 'Fleet'  | None:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                fleet_id, owner_id, mission, position_planet, position_system, position_spiral,
                target_planet, target_system, target_spiral, arrival_time, start_time,
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
        fleet.mission            = fleet_data[2]
        fleet.position           = [fleet_data[3], fleet_data[4], fleet_data[5]]
        fleet.target             = [fleet_data[6], fleet_data[7], fleet_data[8]] if fleet_data[6] is not None else None
        fleet.arrival_time       = float(fleet_data[9])                          if fleet_data[9] is not None else None
        fleet.start_time         = float(fleet_data[10])                         if fleet_data[10] is not None else None
        fleet.fighters           = float(fleet_data[11])
        fleet.interceptors       = float(fleet_data[12])
        fleet.tac_bombers        = float(fleet_data[13])
        fleet.str_bombers        = float(fleet_data[14])
        fleet.frigates           = float(fleet_data[15])
        fleet.destroyers         = float(fleet_data[16])
        fleet.cruisers           = float(fleet_data[17])
        fleet.battlecruisers     = float(fleet_data[18])
        fleet.battleships        = float(fleet_data[19])
        fleet.escort_carriers    = float(fleet_data[20])
        fleet.fleet_carriers     = float(fleet_data[21])
        fleet.titans             = float(fleet_data[22])
        fleet.sattelites         = float(fleet_data[23])
        fleet.small_cargo_ships  = float(fleet_data[24])
        fleet.big_cargo_ships    = float(fleet_data[25])
        fleet.colony_ships       = float(fleet_data[26])
        fleet.science_ships      = float(fleet_data[27])
        fleet.construction_ships = float(fleet_data[28])

        return fleet

    @staticmethod
    def get_from_db_by_id(fleet_id: int) -> 'Fleet' | None:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                fleet_id, owner_id, mission, position_planet, position_system, position_spiral,
                target_planet, target_system, target_spiral, arrival_time, start_time,
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
        fleet.mission            = fleet_data[2]
        fleet.position           = [fleet_data[3], fleet_data[4], fleet_data[5]]
        fleet.target             = [fleet_data[6], fleet_data[7], fleet_data[8]] if fleet_data[6] is not None else None
        fleet.arrival_time       = float(fleet_data[9])                          if fleet_data[9] is not None else None
        fleet.start_time         = float(fleet_data[10])                         if fleet_data[10] is not None else None
        fleet.fighters           = float(fleet_data[11])
        fleet.interceptors       = float(fleet_data[12])
        fleet.tac_bombers        = float(fleet_data[13])
        fleet.str_bombers        = float(fleet_data[14])
        fleet.frigates           = float(fleet_data[15])
        fleet.destroyers         = float(fleet_data[16])
        fleet.cruisers           = float(fleet_data[17])
        fleet.battlecruisers     = float(fleet_data[18])
        fleet.battleships        = float(fleet_data[19])
        fleet.escort_carriers    = float(fleet_data[20])
        fleet.fleet_carriers     = float(fleet_data[21])
        fleet.titans             = float(fleet_data[22])
        fleet.sattelites         = float(fleet_data[23])
        fleet.small_cargo_ships  = float(fleet_data[24])
        fleet.big_cargo_ships    = float(fleet_data[25])
        fleet.colony_ships       = float(fleet_data[26])
        fleet.science_ships      = float(fleet_data[27])
        fleet.construction_ships = float(fleet_data[28])

        return fleet