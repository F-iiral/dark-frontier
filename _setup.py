import sqlite3
import time
import bcrypt
import secrets
import base64
import os
import random
from common.lite_flake_id import LiteFlakeID
from common.const import Badges, Activity, ConsoleShortcuts
from common.lib.planet import Planet
from common.env import SPIRAL_COUNT, STAR_COUNT

################################
### SET UP THE MAIN DATABASE ###
################################
start_time = time.time()

if not os.path.exists("database"):
    os.makedirs("database")

conn = sqlite3.connect("database/data.sql")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        token TEXT NOT NULL,
        badges INTEGER NOT NULL,
        activity INTEGER NOT NULL
    )
"""); print(f"{ConsoleShortcuts.log()} Set up the 'accounts' table in the main database.")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        account_id INTEGER PRIMARY KEY,
        planet_ids TEXT,
        alliance_id INTEGER,
        tec_energy INTEGER,
        tec_computing INTEGER,
        tec_hyperspace INTEGER,
        tec_production INTEGER,
        tec_colonization INTEGER,
        tec_shield INTEGER,
        tec_armor INTEGER,
        tec_engine INTEGER,
        tec_storage INTEGER,
        tec_hangar INTEGER,
        tec_conv_weapon INTEGER,
        tec_laser INTEGER,
        tec_ion INTEGER,
        tec_plasma INTEGER,
        tec_disruptor INTEGER,
        FOREIGN KEY(account_id) REFERENCES accounts(id)
    )
"""); print(f"{ConsoleShortcuts.log()} Set up the 'users' table in the main database.")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS planets (
        planet_id INTEGER PRIMARY KEY,
        owner_id INTEGER,
        metal_amount REAL,
        crystal_amount REAL,
        gas_amount REAL,
        position_planet INTEGER,
        position_system INTEGER,
        position_spiral INTEGER,
        stationed_fleet_id INTEGER,
        inbound_fleet_ids TEXT,
        outbound_fleet_ids TEXT,
        bld_metal_mine INTEGER,
        bld_crystal_mine INTEGER,
        bld_gas_mine INTEGER,
        bld_metal_storage INTEGER,
        bld_crystal_storage INTEGER,
        bld_gas_storage INTEGER,
        bld_factory INTEGER,
        bld_shipyard INTEGER,
        bld_laboratory INTEGER,
        bld_terraformer INTEGER,
        def_aa REAL,
        def_rocket REAL,
        def_railgun REAL,
        def_laser REAL,
        def_ion REAL,
        def_plasma REAL,
        def_disruptor REAL,
        def_s_shield INTEGER,
        def_m_shield INTEGER,
        def_l_shield INTEGER,
        name TEXT,
        radius INTEGER,
        temperature INTEGER,
        last_checkout REAL,
        FOREIGN KEY(owner_id) REFERENCES accounts(id),
        FOREIGN KEY(stationed_fleet_id) REFERENCES fleets(id),
        FOREIGN KEY(inbound_fleet_ids) REFERENCES fleets(id),
        FOREIGN KEY(outbound_fleet_ids) REFERENCES fleets(id)
    )
"""); print(f"{ConsoleShortcuts.log()} Set up the 'planet' table in the main database.")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS fleets (
        fleet_id INTEGER PRIMARY KEY,
        owner_id INTEGER,
        moving INTEGER,
        position_planet INTEGER,
        position_system INTEGER,
        position_spiral INTEGER,
        target_planet INTEGER,
        target_system INTEGER,
        target_spiral INTEGER,
        arrival_time REAL,
        fighters REAL,
        interceptors REAL,
        tac_bombers REAL,
        str_bombers REAL,
        frigates REAL,
        destroyers REAL,
        cruisers REAL,
        battlecruisers REAL,
        battleships REAL,
        escort_carriers REAL,
        fleet_carriers REAL,
        titans REAL,
        sattelites REAL,
        small_cargo_ships REAL,
        big_cargo_ships REAL,
        colony_ships REAL,
        science_ships REAL,
        construction_ships REAL,
        FOREIGN KEY(owner_id) REFERENCES accounts(id)
    )
"""); print(f"{ConsoleShortcuts.log()} Set up the 'fleet' table in the main database.")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alliances (
        id INTEGER PRIMARY KEY,
        founder_id INTEGER,
        tag TEXT,
        name TEXT,
        pub_description TEXT,
        prv_description TEXT,
        owners TEXT,
        officers TEXT,
        veterans TEXT,
        members TEXT,
        recruits TEXT,
        wars TEXT,
        truces TEXT,
        associations TEXT,
        join_rule INTEGER,
        major_power INTEGER,
        hide_members INTEGER,
        hide_diplomacy INTEGER,
        FOREIGN KEY(founder_id) REFERENCES accounts(id)
    )
"""); print(f"{ConsoleShortcuts.log()} Set up the 'alliances' table in the main database.")
conn.commit()

###############################
### SET UP THE PLANET TABLE ###
###############################
for arm in range(1, SPIRAL_COUNT + 1):   # we do this here because b is not included in the upper bound but wanted
    for star in range(1, STAR_COUNT):
        star_temp = 2400 + abs(random.normalvariate(0, 1000))

        for planet in range(1, 11):
            new_planet = Planet()
            new_planet.position = [arm, star, planet]
            new_planet.planet_id = arm*100000 + star*100 + planet
            new_planet.radius = int(random.normalvariate(4000, 1000) + 1000)        # 5 sigma chance to be negative
            new_planet.temperature = int((6 * star_temp)/((planet + 4)**2) - 273)
            new_planet.save_to_db()
    print(f"{ConsoleShortcuts.log()} Fully generated arm {arm}.")

############################
### CREATE ADMIN ACCOUNT ###
############################
user_id = LiteFlakeID.generate_id()
password = base64.urlsafe_b64encode(secrets.token_bytes(15)).decode('utf-8')[:18]
hashed_password =  bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
token = f"{hex(user_id).removeprefix('0x')}.{hex(int(time.time())).removeprefix('0x')}.{base64.urlsafe_b64encode(secrets.token_bytes(15)).decode('utf-8')[:18]}"

cursor.execute(
    "INSERT INTO accounts (id, username, password, token, badges, activity) VALUES (?, ?, ?, ?, ?, ?)",
    (user_id, "Admin", hashed_password, token, Badges.ADMINISTRATOR.value, Activity.OFFLINE.value)
)
conn.commit()
print(f"{ConsoleShortcuts.log()} Created the 'Admin' account with password: '{password}'.")

######################
### FINISH PROCESS ###
######################
print(f"{ConsoleShortcuts.ok()} Finished migration in {round(time.time() - start_time)} seconds.")
conn.close()