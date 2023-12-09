from hashlib import sha256
from common.lib.account import Account
from common.enums import Badges
from common.db_cache import DBCache

def _get_account_from_token(token: str) -> Account | None:
    if (token is None) or (token == ""):
        return None

    split_token = token.split(".")
    userid = split_token[0]
    return Account.get_from_db_by_id(int(userid, base=16))

def _has_badge(token: str | None, badge: Badges) -> bool:
    account_to_check = _get_account_from_token(token)
    return account_to_check is not None and (account_to_check.token & badge.value == badge.value)

def is_valid_token(token: str | None) -> bool:
    account_to_check = _get_account_from_token(token)
    return (account_to_check is not None) and (account_to_check.token == sha256(token.encode("utf-8")).hexdigest())

def is_administrator(token: str) -> bool:
    return _has_badge(token, Badges.ADMINISTRATOR)

def is_moderator(token: str) -> bool:
    return _has_badge(token, Badges.MODERATOR) or _has_badge(token, Badges.ADMINISTRATOR)

def is_planet_owner(token: str, planet_id: int) -> bool:
    split_token = token.split(".")
    userid = split_token[0]
    planet_to_check = DBCache.get_planet(int(planet_id))
    if planet_to_check is None: return False

    return planet_to_check.owner_id == int(userid, base=16)

def is_fleet_owner(token: str, fleet_id: int) -> bool:
    split_token = token.split(".")
    userid = split_token[0]
    planet_to_check = DBCache.get_planet(int(fleet_id))
    if planet_to_check is None: return False

    return planet_to_check.owner_id == int(userid, base=16)

def is_alliance_owner(token: str | None, alliance_id: int) -> bool:
    return False