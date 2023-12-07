import bcrypt
from flask import jsonify
from common.lib.account import Account

def main(username: str, input_password: str) -> tuple:
    account_to_test: Account = Account.get_from_db_by_name(username)

    if account_to_test is None:
        return "Wrong username or password.", 400
    
    hashed_password = account_to_test.password.removeprefix("b'").removesuffix("'").encode("utf-8")
    if bcrypt.checkpw(input_password.encode("utf-8"), hashed_password):
        data = {
            "token": account_to_test.token
        }
        return jsonify(data), 200
    else:
        return "Wrong username or password.", 400