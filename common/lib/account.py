import sqlite3
from common.const import ConsoleShortcuts

class Account():
    """
    Represents the account of a person and only contains information relevant outside the game like passwords or tokens.
    """

    def __init__(self) -> None:
        self.id             : int   = None
        self.username       : str   = None
        self.password       : str   = None
        self.token          : str   = None
        self.badges         : int   = 0
        self.activity       : int   = 0

    def to_dict(self, *args):
        """Does not return password and token for security reasons."""
        return {
            "id": self.id,
            "username": self.username,
            "badges": self.badges,
            "activity": self.activity,
        }

    def save_to_db(self) -> None:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO accounts (id, username, password, token, badges, activity)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.id, self.username, self.password, self.token, self.badges, self.activity))

        conn.commit()
        conn.close()

    @staticmethod
    def get_from_db_by_id(account_id) -> 'Account':
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, username, password, token, badges, activity
            FROM accounts
            WHERE id = ?
        """, (account_id,))

        account_data = cursor.fetchone()
        conn.close()
        if account_data is None:
            print(f"{ConsoleShortcuts.warn()} Could not find 'account' by ID {account_id}.")
            return account_data

        new_account = Account()
        new_account.id       = account_data[0]
        new_account.username = str(account_data[1])
        new_account.password = str(account_data[2])
        new_account.token    = str(account_data[3])
        new_account.badges   = int(account_data[4])
        new_account.activity = int(account_data[5])

        return new_account

    @staticmethod
    def get_from_db_by_name(username) -> 'Account':
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, username, password, token, badges, activity
            FROM accounts
            WHERE username = ?
        """, (username,))

        account_data = cursor.fetchone()
        conn.close()
        if account_data is None:
            print(f"{ConsoleShortcuts.warn()} Could not find 'account' by name {username}.")
            return account_data

        new_account = Account()
        new_account.id       = account_data[0]
        new_account.username = str(account_data[1])
        new_account.password = str(account_data[2])
        new_account.token    = str(account_data[3])
        new_account.badges   = int(account_data[4])

        return new_account