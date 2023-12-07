from common.lib.account import Account
from common.enums import Badges
from common.db_cache import DBCache

def is_valid_token(token: str) -> bool:
    split_token = token.split(".")
    token_userid = split_token[0]
    token_security = split_token[2]

    account_to_check = Account.get_from_db_by_id(token_userid)

    if not (account_to_check.token.split(".")[2] == token_security):
        return False
    return True

def is_administrator(token: str) -> bool:
    return False

def is_moderator(token: str) -> bool:
    return False

def is_planet_owner(token: str, planet_id: int) -> bool:
    return False

def is_fleet_owner(token: str, fleet_id: int) -> bool:
    return False

def is_alliance_owner(token: str, alliance_id: int) -> bool:
    return False