from flask import jsonify
from common.db_cache import DBCache

def main(token: str) -> tuple:
    split_token = token.split(".")
    userid = split_token[0]
    user = DBCache.get_user(int(userid, base=16))

    data = []
    for fleet_id in user.fleet_ids:
        fleet = DBCache.get_fleet(fleet_id)
        data.append(fleet.to_dict())

    return jsonify(data), 200