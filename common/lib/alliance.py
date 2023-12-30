import sqlite3
from typing import Union

class Alliance():
    def __init__(self) -> None:
        ### Basic Information
        self.id                 : int       = None
        self.founder_id         : int       = None

        ### Display
        self.tag                : str       = ""
        self.name               : str       = ""
        self.pub_description    : str       = ""
        self.prv_description    : str       = ""

        ### Roles
        self.owners             : list[int] = []
        self.officers           : list[int] = []
        self.veterans           : list[int] = []
        self.members            : list[int] = []
        self.recruits           : list[int] = []

        ### Diplomacy
        self.wars               : list[int] = []
        self.truces             : list[int] = []
        self.associations       : list[int] = []

        ### Settings
        self.join_rule          : int       = 0
        self.major_power        : bool      = False
        self.hide_members       : bool      = False
        self.hide_diplomacy     : bool      = False

    def to_dict(self, hide_private_info: bool=True) -> dict:
        return {
            "id": self.id,
            "founder_id": self.founder_id,
            "tag": self.tag,
            "name": self.name,
            "join_rule": self.join_rule,
            "major_power": self.major_power,
            "pub_description": self.pub_description,
            "prv_description": self.prv_description if not hide_private_info else None,
            "owners": self.owners if not self.hide_members else None,
            "officers": self.officers if not self.hide_members else None,
            "veterans": self.veterans if not self.hide_members else None,
            "members": self.members if not self.hide_members else None,
            "recruits": self.recruits if not self.hide_members else None,
            "wars": self.wars if not self.hide_diplomacy else None,
            "truces": self.truces if not self.hide_diplomacy else None,
            "associations": self.associations if not self.hide_diplomacy else None,
        }

    def save_to_db(self) -> None:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO alliances (
                id, founder_id, tag, name, pub_description, prv_description,
                owners, officers, veterans, members, recruits,
                wars, truces, associations, join_rule, major_power, hide_members, hide_diplomacy
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.id, self.founder_id, self.tag, self.name, self.pub_description, self.prv_description,
            ",".join(map(str, self.owners)), ",".join(map(str, self.officers)), ",".join(map(str, self.veterans)),
            ",".join(map(str, self.members)), ",".join(map(str, self.recruits)),
            ",".join(map(str, self.wars)), ",".join(map(str, self.truces)), ",".join(map(str, self.associations)),
            self.join_rule, int(self.major_power), int(self.hide_members), int(self.hide_diplomacy)
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_from_db_by_id(alliance_id: int) -> Union['Alliance', None]:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id, founder_id, tag, name, pub_description, prv_description,
                owners, officers, veterans, members, recruits,
                wars, truces, associations, join_rule, major_power, hide_members, hide_diplomacy
            FROM alliances
            WHERE id = ?
        """, (alliance_id,))

        alliance_data = cursor.fetchone()
        conn.close()

        if alliance_data is None:
            print(f"Could not find 'alliance' by ID {alliance_id}.")
            return alliance_data

        alliance = Alliance()
        alliance.id = alliance_data[0]
        alliance.founder_id = alliance_data[1]
        alliance.tag = alliance_data[2]
        alliance.name = alliance_data[3]
        alliance.pub_description = alliance_data[4]
        alliance.prv_description = alliance_data[5]
        alliance.owners = list(map(int, alliance_data[6].split(',')))
        alliance.officers = list(map(int, alliance_data[7].split(',')))
        alliance.veterans = list(map(int, alliance_data[8].split(',')))
        alliance.members = list(map(int, alliance_data[9].split(',')))
        alliance.recruits = list(map(int, alliance_data[10].split(',')))
        alliance.wars = list(map(int, alliance_data[11].split(',')))
        alliance.truces = list(map(int, alliance_data[12].split(',')))
        alliance.associations = list(map(int, alliance_data[13].split(',')))
        alliance.join_rule = alliance_data[14]
        alliance.major_power = bool(alliance_data[15])
        alliance.hide_members = bool(alliance_data[16])
        alliance.hide_diplomacy = bool(alliance_data[17])

        return alliance