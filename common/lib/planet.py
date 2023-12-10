import sqlite3
from common.dev import ConsoleShortcuts
from common.lib.user import User
from common.lib.fleet import Fleet

class Planet():
    """
    Represents a planet inside the game.

    Position is stored the following way: [planet, system, arm]
    """

    def __init__(self) -> None:
        ### Owner
        self.owner_id            : int | None    = None
        self.owner               : User | None   = None

        ### Basic Information
        self.name                : str          = "Colony"
        self.planet_id           : int          = 0
        self.position            : list[int]    = [0, 0, 0]
        self.metal_amount        : float        = 0.0
        self.crystal_amount      : float        = 0.0
        self.gas_amount          : float        = 0.0

        ### Fleets
        self.stationed_fleet_id  : int | None   = None
        self.stationed_fleet     : Fleet        = None
        self.inbound_fleet_ids   : list[int]    = None
        self.inbound_fleets      : list[Fleet]  = None
        self.outbound_fleet_ids  : list[int]    = None
        self.outbound_fleets     : list[Fleet]  = None

        ### Buildings
        self.bld_metal_mine      : int       = 0
        self.bld_crystal_mine    : int       = 0
        self.bld_gas_mine        : int       = 0
        self.bld_metal_storage   : int       = 0
        self.bld_crystal_storage : int       = 0
        self.bld_gas_storage     : int       = 0
        self.bld_factory         : int       = 0
        self.bld_shipyard        : int       = 0
        self.bld_laboratory      : int       = 0
        self.bld_terraformer     : int       = 0

        ### Defense
        self.def_aa              : float     = 0.0
        self.def_rocket          : float     = 0.0
        self.def_railgun         : float     = 0.0
        self.def_laser           : float     = 0.0
        self.def_ion             : float     = 0.0
        self.def_plasma          : float     = 0.0
        self.def_disruptor       : float     = 0.0
        self.def_s_shield        : bool      = False
        self.def_m_shield        : bool      = False
        self.def_l_shield        : bool      = False

    def to_dict(self, *args):
        return {
            "owner_id": self.owner_id,
            "owner": self.owner.to_dict(),
            "name": self.name,
            "planet_id": self.planet_id,
            "position": self.position,
            "metal_amount": self.metal_amount,
            "crystal_amount": self.crystal_amount,
            "gas_amount": self.gas_amount,
            "stationed_fleet_id ": self.stationed_fleet_id ,
            "stationed_fleet": self.stationed_fleet.to_dict() if self.stationed_fleet is not None else None ,
            "inbound_fleet_ids": self.inbound_fleet_ids,
            "inbound_fleets": [i.to_dict()  if i is not None else None for i in self.inbound_fleets],
            "outbound_fleet_ids": self.outbound_fleet_ids,
            "outbound_fleets": [i.to_dict()  if i is not None else None for i in self.outbound_fleets],
            "bld_metal_mine": self.bld_metal_mine,
            "bld_crystal_mine": self.bld_crystal_mine,
            "bld_gas_mine": self.bld_gas_mine,
            "bld_metal_storage ": self.bld_metal_storage ,
            "bld_crystal_storage": self.bld_crystal_storage,
            "bld_gas_storage": self.bld_gas_storage,
            "bld_factory": self.bld_factory,
            "bld_shipyard": self.bld_shipyard,
            "bld_laboratory": self.bld_laboratory,
            "bld_terraformer": self.bld_terraformer,
            "def_aa": self.def_aa,
            "def_rocket": self.def_rocket,
            "def_railgun": self.def_railgun,
            "def_laser": self.def_laser,
            "def_ion": self.def_ion,
            "def_plasma": self.def_plasma,
            "def_disruptor": self.def_disruptor,
            "def_s_shield": self.def_s_shield,
            "def_m_shield": self.def_m_shield,
            "def_l_shield": self.def_l_shield,
        }

    def save_to_db(self) -> None:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO planets (
                planet_id, owner_id, metal_amount, crystal_amount, gas_amount,
                position_planet, position_system, position_spiral,
                stationed_fleet_id,
                inbound_fleet_ids,
                outbound_fleet_ids,
                bld_metal_mine, bld_crystal_mine, bld_gas_mine, bld_metal_storage, bld_crystal_storage, bld_gas_storage,
                bld_factory, bld_shipyard, bld_laboratory, bld_terraformer,
                def_aa, def_rocket, def_railgun, def_laser, def_ion, def_plasma, def_disruptor,
                def_s_shield, def_m_shield, def_l_shield
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.planet_id,self.owner_id, self.metal_amount, self.crystal_amount, self.gas_amount,
            self.position[0], self.position[1], self.position[2],
            self.stationed_fleet_id,
            ",".join(map(str, self.inbound_fleet_ids)) if self.inbound_fleet_ids else None,
            ",".join(map(str, self.outbound_fleet_ids)) if self.outbound_fleet_ids else None,
            self.bld_metal_mine, self.bld_crystal_mine, self.bld_gas_mine, self.bld_metal_storage, self.bld_crystal_storage, self.bld_gas_storage,
            self.bld_factory, self.bld_shipyard, self.bld_laboratory, self.bld_terraformer,
            self.def_aa, self.def_rocket, self.def_railgun, self.def_laser, self.def_ion, self.def_plasma, self.def_disruptor,
            int(self.def_s_shield), int(self.def_m_shield), int(self.def_l_shield)
        ))

        conn.commit()
        conn.close()
    
    @staticmethod
    def get_from_db_by_owner(owner_id: int) -> 'Planet':
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                planet_id, owner_id, metal_amount, crystal_amount, gas_amount,
                position_planet, position_system, position_spiral,
                stationed_fleet_id, inbound_fleet_ids, outbound_fleet_ids,
                bld_metal_mine, bld_crystal_mine, bld_gas_mine,
                bld_metal_storage, bld_crystal_storage, bld_gas_storage,
                bld_factory, bld_shipyard, bld_laboratory, bld_terraformer,
                def_aa, def_rocket, def_railgun, def_laser, def_ion, def_plasma,
                def_disruptor, def_s_shield, def_m_shield, def_l_shield
            FROM planets
            WHERE owner_id = ?
        """, (owner_id,))

        planet_data = cursor.fetchone()
        conn.close()
        if planet_data is None:
            print(f"{ConsoleShortcuts.warn()} Could not find 'planet' by owner ID {owner_id}.")
            return planet_data

        new_planet = Planet()
        new_planet.planet_id            = planet_data[0]
        new_planet.owner_id             = planet_data[1]
        new_planet.owner                = User.get_from_db_by_owner(planet_data[1])
        new_planet.metal_amount         = float(planet_data[2])
        new_planet.crystal_amount       = float(planet_data[3])
        new_planet.gas_amount           = float(planet_data[4])
        new_planet.position             = [int(planet_data[5]), int(planet_data[6]), int(planet_data[7])]
        new_planet.stationed_fleet_id   = planet_data[8]
        
        inbound_fleet_ids_str = planet_data[9]
        new_planet.inbound_fleet_ids    = list(map(int, inbound_fleet_ids_str.split(','))) if inbound_fleet_ids_str else []
        new_planet.inbound_fleets       = []
        for fleet_id in new_planet.inbound_fleet_ids:
            new_planet.inbound_fleets.append(Fleet.get_from_db_by_id(fleet_id))

        outbound_fleet_ids_str = planet_data[10]
        new_planet.outbound_fleet_ids   = list(map(int, outbound_fleet_ids_str.split(','))) if outbound_fleet_ids_str else []
        new_planet.outbound_fleets      = []
        for fleet_id in new_planet.outbound_fleet_ids:
            new_planet.outbound_fleet_ids.append(Fleet.get_from_db_by_id(fleet_id))

        new_planet.bld_metal_mine       = int(planet_data[11])
        new_planet.bld_crystal_mine     = int(planet_data[12])
        new_planet.bld_gas_mine         = int(planet_data[13])
        new_planet.bld_metal_storage    = int(planet_data[14])
        new_planet.bld_crystal_storage  = int(planet_data[15])
        new_planet.bld_gas_storage      = int(planet_data[16])
        new_planet.bld_factory          = int(planet_data[17])
        new_planet.bld_shipyard         = int(planet_data[18])
        new_planet.bld_laboratory       = int(planet_data[19])
        new_planet.bld_terraformer      = int(planet_data[20])
        new_planet.def_aa               = float(planet_data[21])
        new_planet.def_rocket           = float(planet_data[22])
        new_planet.def_railgun          = float(planet_data[23])
        new_planet.def_laser            = float(planet_data[24])
        new_planet.def_ion              = float(planet_data[25])
        new_planet.def_plasma           = float(planet_data[26])
        new_planet.def_disruptor        = float(planet_data[27])
        new_planet.def_s_shield         = bool(planet_data[28])
        new_planet.def_m_shield         = bool(planet_data[29])
        new_planet.def_l_shield         = bool(planet_data[30])

        return new_planet

    @staticmethod
    def get_from_db_by_id(planet_id: int) -> 'Planet':
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                planet_id, owner_id, metal_amount, crystal_amount, gas_amount,
                position_planet, position_system, position_spiral,
                stationed_fleet_id, inbound_fleet_ids, outbound_fleet_ids,
                bld_metal_mine, bld_crystal_mine, bld_gas_mine,
                bld_metal_storage, bld_crystal_storage, bld_gas_storage,
                bld_factory, bld_shipyard, bld_laboratory, bld_terraformer,
                def_aa, def_rocket, def_railgun, def_laser, def_ion, def_plasma,
                def_disruptor, def_s_shield, def_m_shield, def_l_shield
            FROM planets
            WHERE planet_id = ?
        """, (planet_id,))

        planet_data = cursor.fetchone()
        conn.close()
        if planet_data is None:
            print(f"{ConsoleShortcuts.warn()} Could not find 'planet' by planet ID {planet_id}.")
            return planet_data

        new_planet = Planet()
        new_planet.planet_id            = planet_data[0]
        new_planet.owner_id             = planet_data[1]
        new_planet.owner                = User.get_from_db_by_owner(planet_data[1])
        new_planet.metal_amount         = float(planet_data[2])
        new_planet.crystal_amount       = float(planet_data[3])
        new_planet.gas_amount           = float(planet_data[4])
        new_planet.position             = [int(planet_data[5]), int(planet_data[6]), int(planet_data[7])]
        new_planet.stationed_fleet_id   = planet_data[8]
        
        inbound_fleet_ids_str = planet_data[9]
        new_planet.inbound_fleet_ids    = list(map(int, inbound_fleet_ids_str.split(','))) if inbound_fleet_ids_str else []
        new_planet.inbound_fleets       = []
        for fleet_id in new_planet.inbound_fleet_ids:
            new_planet.inbound_fleets.append(Fleet.get_from_db_by_id(fleet_id))

        outbound_fleet_ids_str = planet_data[10]
        new_planet.outbound_fleet_ids   = list(map(int, outbound_fleet_ids_str.split(','))) if outbound_fleet_ids_str else []
        new_planet.outbound_fleets      = []
        for fleet_id in new_planet.outbound_fleet_ids:
            new_planet.outbound_fleet_ids.append(Fleet.get_from_db_by_id(fleet_id))

        new_planet.bld_metal_mine       = int(planet_data[11])
        new_planet.bld_crystal_mine     = int(planet_data[12])
        new_planet.bld_gas_mine         = int(planet_data[13])
        new_planet.bld_metal_storage    = int(planet_data[14])
        new_planet.bld_crystal_storage  = int(planet_data[15])
        new_planet.bld_gas_storage      = int(planet_data[16])
        new_planet.bld_factory          = int(planet_data[17])
        new_planet.bld_shipyard         = int(planet_data[18])
        new_planet.bld_laboratory       = int(planet_data[19])
        new_planet.bld_terraformer      = int(planet_data[20])
        new_planet.def_aa               = float(planet_data[21])
        new_planet.def_rocket           = float(planet_data[22])
        new_planet.def_railgun          = float(planet_data[23])
        new_planet.def_laser            = float(planet_data[24])
        new_planet.def_ion              = float(planet_data[25])
        new_planet.def_plasma           = float(planet_data[26])
        new_planet.def_disruptor        = float(planet_data[27])
        new_planet.def_s_shield         = bool(planet_data[28])
        new_planet.def_m_shield         = bool(planet_data[29])
        new_planet.def_l_shield         = bool(planet_data[30])

        return new_planet