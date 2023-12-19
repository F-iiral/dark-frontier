import re
import bcrypt
import sqlite3
import time
import secrets
import base64
import random
from flask import jsonify
from common.env import SPIRAL_COUNT, STAR_COUNT
from common.const import Activity, ConsoleShortcuts
from common.lite_flake_id import LiteFlakeID
from common.lib.user import User
from common.lib.planet import Planet

def main(username: str, password: str) -> tuple:
    if not (isinstance(username, str)):
        return "Username must be a string.", 400
    if not (isinstance(password, str)):
        return "Password must be a string.", 400
    if not (re.match('^[a-zA-Z0-9_]+$', username)):
        return "Username can only contain alphanumerical characters and underscores.", 400
    if not (3 <= len(username.encode("utf-8")) <= 24):
        return "Username needs to be between 3 and 24 chracters long.", 400
    if not (6 <= len(password.encode("utf-8")) <= 72):
        return "Password must be atleast 6 characters long.", 400

    character_requirements = [
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in "@#$%^&*_-~=+()[]{}<>|.,;:?!'\"`\\/" for c in password),
    ]

    if not (sum(character_requirements) >= 2):
        return "Password is too simple.", 400
    
    user_id = LiteFlakeID.generate_id()
    create_account(user_id)
    token = store_credentials(username, password, user_id)
    data = {
        "token": token
    }
    return jsonify(data), 201

def store_credentials(username: str, password: str, user_id: int) -> str:
    hashed_password =  bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    token = f"{hex(user_id).removeprefix('0x')}.{hex(int(time.time())).removeprefix('0x')}.{base64.urlsafe_b64encode(secrets.token_bytes(15)).decode('utf-8')[:18]}"

    # (true) entropy of the token is ~120 with a resulting brute force time
    # of 10^23 years or >10^13 as long as the universes has existed for

    try:
        conn = sqlite3.connect("database/data.sql")
        cursor = conn.cursor()
    
        cursor.execute("""
        INSERT INTO accounts (
            id, username, password, token, badges, activity
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (user_id, username, hashed_password, token.encode("utf-8"), 0, Activity.OFFLINE.value))
        conn.commit()
    except Exception as e:
        print(f"{ConsoleShortcuts.error()} Failed to store credentials: {e}")

    return token

def create_account(user_id) -> None:
    new_user = User()
    new_user.id = user_id
    new_user.save_to_db()

    new_planet = find_free_planet()
    new_planet.owner_id = user_id
    new_planet.name = "Home Planet"
    new_planet.radius += 500
    new_planet.metal_amount = 100000
    new_planet.crystal_amount = 100000
    new_planet.gas_amount = 100000
    new_planet.save_to_db()

def find_free_planet() -> Planet:
    while True:
        random_position_id = random.randint(1, SPIRAL_COUNT) * 100000 + random.randint(1, STAR_COUNT) * 100 + random.randint(1, 11)
        new_planet = Planet.get_from_db_by_id(random_position_id)

        if new_planet.owner == None:
            return new_planet