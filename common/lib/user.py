import sqlite3
from common.lib.alliance import Alliance
from common.dev import ConsoleShortcuts
from common.lib.account import Account
from common.env import FLEET_SPEED, RESOURCE_SPEED, STAR_COUNT, SPIRAL_COUNT

class User():
    """
    Represents a user inside the game.
    """
    
    def __init__(self) -> None:
        ### Account
        self.id                 : int | None        = None
        self.account            : Account | None    = None

        ### Quick Access
        self.planet_ids         : list[int]         = []
        self.alliance_id        : int | None        = None
        self.alliance           : Alliance | None   = None

        ### Technologies
        self.tec_energy         : int       = 0
        self.tec_computing      : int       = 0
        self.tec_hyperspace     : int       = 0
        self.tec_production     : int       = 0
        self.tec_colonization   : int       = 0
        self.tec_shield         : int       = 0
        self.tec_armor          : int       = 0
        self.tec_engine         : int       = 0
        self.tec_storage        : int       = 0
        self.tec_hangar         : int       = 0
        self.tec_conv_weapon    : int       = 0
        self.tec_laser          : int       = 0
        self.tec_ion            : int       = 0
        self.tec_plasma         : int       = 0
        self.tec_disruptor      : int       = 0
    
    def to_dict(self, *args):
        return {
            "id": self.id,
            "account": self.account.to_dict(),
            "planet_ids": self.planet_ids,
            "alliance_id": self.alliance_id,
            "alliance": self.alliance.to_dict() if self.alliance is not None else None,
            "tec_energy": self.tec_energy,
            "tec_computing": self.tec_computing,
            "tec_hyperspace": self.tec_hyperspace,
            "tec_production": self.tec_production,
            "tec_colonization": self.tec_colonization,
            "tec_shield": self.tec_shield,
            "tec_armor": self.tec_armor,
            "tec_engine": self.tec_engine,
            "tec_storage": self.tec_storage,
            "tec_hangar": self.tec_hangar,
            "tec_conv_weapon": self.tec_conv_weapon,
            "tec_laser": self.tec_laser,
            "tec_ion": self.tec_ion,
            "tec_plasma": self.tec_plasma,
            "tec_disruptor": self.tec_disruptor,
            "galaxy": {
                "fleet_speed": FLEET_SPEED,
                "resource_speed": RESOURCE_SPEED,
                "star_count": STAR_COUNT,
                "spiral_count": SPIRAL_COUNT
            }
        }

    def save_to_db(self) -> None:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO users (
                account_id, tec_energy,
                planet_ids, alliance_id,
                tec_computing, tec_hyperspace, tec_production,
                tec_colonization, tec_shield, tec_armor, tec_engine, tec_storage,
                tec_hangar, tec_conv_weapon, tec_laser, tec_ion, tec_plasma, tec_disruptor
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.id, self.tec_energy,
            ",".join(map(str,self.planet_ids)), self.alliance_id,
            self.tec_computing, self.tec_hyperspace, self.tec_production,
            self.tec_colonization, self.tec_shield, self.tec_armor, self.tec_engine, self.tec_storage,
            self.tec_hangar, self.tec_conv_weapon, self.tec_laser, self.tec_ion, self.tec_plasma,
            self.tec_disruptor
        ))

        conn.commit()
        conn.close()
    
    @staticmethod
    def get_from_db_by_owner(account_id: int) -> 'User':
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                account_id, tec_energy, tec_computing, tec_hyperspace, tec_production,
                tec_colonization, tec_shield, tec_armor, tec_engine, tec_storage,
                tec_hangar, tec_conv_weapon, tec_laser, tec_ion, tec_plasma, tec_disruptor
            FROM users
            WHERE account_id = ?
        """, (account_id,))

        user_data = cursor.fetchone()
        conn.close()
        if user_data is None:
            print(f"{ConsoleShortcuts.warn()} Could not find 'account' by ID {account_id}.")
            return user_data

        user = User()
        user.id               = user_data[0]
        user.account          = Account.get_from_db_by_id(user_data[0])
        user.planet_ids       = list(map(int, user_data[1].split(',')))
        user.alliance_id      = user_data[2] if user_data[2] is not None else None
        user.alliance         = Alliance.get_from_db_by_id(user_data[2]) if user_data[2] is not None else None
        user.tec_energy       = int(user_data[4])
        user.tec_computing    = int(user_data[5])
        user.tec_hyperspace   = int(user_data[6])
        user.tec_production   = int(user_data[7])
        user.tec_colonization = int(user_data[8])
        user.tec_shield       = int(user_data[9])
        user.tec_armor        = int(user_data[10])
        user.tec_engine       = int(user_data[11])
        user.tec_storage      = int(user_data[12])
        user.tec_hangar       = int(user_data[13])
        user.tec_conv_weapon  = int(user_data[14])
        user.tec_laser        = int(user_data[15])
        user.tec_ion          = int(user_data[16])
        user.tec_plasma       = int(user_data[17])
        user.tec_disruptor    = int(user_data[18])

        return user
