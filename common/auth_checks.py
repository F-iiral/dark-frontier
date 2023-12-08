from hashlib import sha256
from common.lib.account import Account
from common.enums import Badges
from common.db_cache import DBCache

def is_valid_token(token: str | None) -> bool:
    if token is None:
        return False
    split_token = token.split(".")
    userid = split_token[0]
    account_to_check = Account.get_from_db_by_id(int(userid, base=16))

    if not (account_to_check.token == sha256(token.encode("utf-8")).hexdigest()):
        return False
    return True

def is_administrator(token: str) -> bool:
    return False

def is_moderator(token: str) -> bool:
    return False

def is_account_owner(token: str, user_id: int) -> bool:
    return False

def is_planet_owner(token: str, planet_id: int) -> bool:
    return False

def is_fleet_owner(token: str, fleet_id: int) -> bool:
    return False

def is_alliance_owner(token: str, alliance_id: int) -> bool:
    return False