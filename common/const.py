import enum
import datetime

class ConsoleShortcuts():
    def log():   return f"{Colors.MAGENTA.value}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}]{Colors.WHITE.value}"
    def ok():    return f"{Colors.GREEN.value}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}]{Colors.WHITE.value}"
    def warn():  return f"{Colors.YELLOW.value}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}]{Colors.WHITE.value}"
    def error(): return f"{Colors.RED.value}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}]{Colors.WHITE.value}"

class Colors(enum.Enum):
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"

class Badges(enum.Enum):
    ADMINISTRATOR = 1
    MODERATOR = 2
    BANNED = 4
    INACTIVE_SHORT = 8
    INACTIVE_LONG = 16
    VACATION = 32

class Activity(enum.Enum):
    OFFLINE = 0
    ACTIVE = 1
    IDLE = 2
    DND = 3

class PlanetBuildings(enum.Enum):
    METAL_MINE      = 1
    CRYSTAL_MINE    = 2
    GAS_MINE        = 3
    METAL_STORAGE   = 4
    CRYSTAL_STORAGE = 5
    GAS_STORAGE     = 6
    FACTORY         = 7
    SHIPYARD        = 8
    LABORATORY      = 9
    TERRAFORMER     = 10

class PlanetDefenses(enum.Enum):
    AA_GUN          = 1
    ROCKET          = 2
    RAILGUN         = 3
    LASER           = 4
    ION             = 5
    PLASMA          = 6
    DISRUPTOR       = 7
    SHIELD_S        = 8
    SHIELD_M        = 9
    SHIELD_L        = 10

class FleetShips(enum.Enum):
    FIGHTERS           = 0
    INTERCEPTORS       = 1
    TAC_BOMBERS        = 2
    STR_BOMBERS        = 3
    FRIGATES           = 4
    DESTROYERS         = 5
    CRUISERS           = 6
    BATTLECRUISERS     = 7
    BATTLESHIPS        = 8
    ESCORT_CARRIERS    = 9
    FLEET_CARRIERS     = 10
    TITANS             = 11
    SATTELITES         = 12
    SMALL_CARGO_SHIPS  = 13
    BIG_CARGO_SHIPS    = 14
    COLONY_SHIPS       = 15
    SCIENCE_SHIPS      = 16
    CONSTRUCTION_SHIPS = 17

class ShipWeapons(enum.Enum):
    CONVENTIONAL = 0
    LASER = 1
    PLASMA = 2
    ION = 3
    DISRUPTOR = 4

class ShipRanges(enum.Enum):
    INTERPLANETARY = 0
    INTERSTELLAR = 1
    GALACTIC = 2
    INTERSTELLAR_PLUS = 3

class UnitStatisticsFull:
    def __init__(self, name, description, description_long, damage_mults, armor, shields, weapons, weapon_type, speed, range, fuel_usage, cargo_space, hangar_space, hangar_usage):
        self.name               : str         = name
        self.description        : str         = description
        self.description_long   : str         = description_long
        self.damage_mults       : list[float] = damage_mults
        self.armor              : int         = armor
        self.shields            : int         = shields
        self.weapons            : int         = weapons
        self.weapon_type        : int         = weapon_type
        self.speed              : int | None  = speed
        self.range              : int | None  = range
        self.fuel_usage         : int | None  = fuel_usage
        self.cargo_space        : int | None  = cargo_space
        self.hangar_space       : int | None  = hangar_space
        self.hangar_usage       : int | None  = hangar_usage

ship_statistics_record: dict[str, UnitStatisticsFull] = {
    "ship_fighter": UnitStatisticsFull(
        name="Fighter",
        description="Fighters are small but cheap craft that can be produced easily to escort larger fleet groups.",
        description_long="The nimble Fighters, designed as cost-effective assets, are the backbone of any formidable fleet. They serve as the vanguard, swiftly neutralizing threats. However, caution is advised when facing Frigates, as their limited armor makes them susceptible to concentrated fire.",
        damage_mults=[0, 1.5, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, -5, 0, 0, -5, -5, 0, 0, 0, 0, 0],
        armor=8,
        shields=0,
        weapons=1,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=10000,
        range=ShipRanges.INTERPLANETARY.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship_interceptor": UnitStatisticsFull(
        name="Interceptor",
        description="Interceptors are an evolution of fighters that focuses on speed, making them much faster and more agile.",
        description_long="The Interceptor, a refined iteration of its predecessor, the Fighter, is meticulously engineered for unparalleled speed and agility on the battlefield. With double the damage output against Bombers, they can easily protect capital ships against their weapons.",
        damage_mults=[-1.5, 0, 2, 2, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -5, -5, 0, 0, 0, 0, 0],
        armor=8,
        shields=0,
        weapons=1,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=12000,
        range=ShipRanges.INTERPLANETARY.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship_tac_bomber": UnitStatisticsFull(
        name="Bomber",
        description="Bombers are designed to carry nukes and other big weapons to destroy capital ships with raw firepower.",
        description_long="Bombers have the raw firepower necessary to annihilate capital ships with unparalleled efficiency. Armed with the capacity to carry nukes and heavy weapons, it becomes the vengeful force against any large craft that dares to enter the battlefield unprotected.",
        damage_mults=[0, -2, 0, 0, -3, 0, 2, 2, 4, 5, 5, 10, 0, 0, 0, 0, 0, 0, -5, 0, 0, -5, -5, 0, 0, 0, 0, 0],
        armor=8,
        shields=0,
        weapons=2,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=8000,
        range=ShipRanges.INTERPLANETARY.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-str-bomber": UnitStatisticsFull(
        name="Strategic Bomber",
        description="Strategic bombers were designed to carry out long distance bombing runs on other planets.",
        description_long="Strategic Bombers are designed to execute precision bombing runs across distant planets. With an arsenal tailored for planetary assault, they unleash cataclysmic damage, devastating any static planetary defenses. Unfortunately, they are helpless in space-to-space combat.",
        damage_mults=[0, -2, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 10, 10, 5, 5, 3, 2, 5, 5, 5],
        armor=40,
        shields=0,
        weapons=10,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=8000,
        range=ShipRanges.GALACTIC.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-frigate": UnitStatisticsFull(
        name="Frigate",
        description="Frigates are ideal for interstellar patrol duties and planetary defense forces.",
        description_long="Frigates are designed to protect planets in smaller planetary defense force fleets but can also be used in larger fleetgroups to destroy any smaller craft like fighters or bombers. This is possible thanks to the extensive point defense and anti-air grid on their hulls.",
        damage_mults=[3, 3, 3, 3, 0, -2, -3, 0, 0, 0, 0, 0, 9, 3, 3, 0, 0, 0, 0, -3, 0, -20, -20, -15, -5, 0, 0, 0],
        armor=240,
        shields=0,
        weapons=30,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=4000,
        range=ShipRanges.INTERSTELLAR.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-destroyer": UnitStatisticsFull(
        name="Destroyer",
        description="Destroyers form the backbone of any interstellar strike force, as they are fast and can operate as escorts.",
        description_long="Destroyers, the backbone of interstellar strike forces, combine speed and versatility to operate effectively as escorts. With double damage against Frigates and Battleships, thanks to torpedos, they are able to screen against smaller vessels or use numbers to attack larger craft.",
        damage_mults=[0, 0, 0, 0, 2, 0, -2, 0, 0, 2, 0, 0, 12, 5, 5, 0, 0, 0, 0, -2, 0, -20, -20, -15, -5, 0, 0, 0],
        armor=950,
        shields=20,
        weapons=120,
        weapon_type=ShipWeapons.LASER.value,
        speed=4000,
        range=ShipRanges.INTERSTELLAR_PLUS.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-cruiser": UnitStatisticsFull(
        name="Cruiser",
        description="Cruisers are large enough to operate independently and cross galactic distances without refueling at all.",
        description_long="Cruisers were designed for two goals=They needed to be large enough to cross galactic distances and they needed to protect even heavier ships against the rise of destroyers. Their shields were reinforced as well, making them able to withstand fire for extended periods of time.",
        damage_mults=[0, 0, -2, 0, 3, 2, 0, 0, -2, -3, 0, -2, 25, 8, 8, 2, 2, 2, 0, -2, 0, -15, -15, -20, -15, 0, 0, 0],
        armor=3000,
        shields=300,
        weapons=420,
        weapon_type=ShipWeapons.LASER.value,
        speed=3500,
        range=ShipRanges.GALACTIC.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-battlecruiser": UnitStatisticsFull(
        name="Battlecruiser",
        description="Battlecruisers were designed to outgun everything they cant run from and outrun anything they do not outgun.",
        description_long="Battlecruisers were an offshoot of the cruiser that was designed to carry bigger guns and still be comperatively fast. They have a combined arsenal of lasers and plasma weapons to achieve the first goal and are also still the same speed as Cruiser though they did have to sacrifice both armor and shield strength.",
        damage_mults=[0, 0, -4, 0, 0, 0, 2, 0, 0, 0, 0, -4, 30, 10, 10, 3, 3, 3, 0, 0, -2, 0, 0, -25, -20, 0, 0, 0],
        armor=4800,
        shields=300,
        weapons=620,
        weapon_type=ShipWeapons.LASER.value + ShipWeapons.PLASMA.value,
        speed=3500,
        range=ShipRanges.GALACTIC.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-battleship": UnitStatisticsFull(
        name="Battleship",
        description="Battleships carry heavy guns, are well armored and have strong shields, making them the flagship of an interstellar strike force.",
        description_long="Battleships are large capital ships with plasma weapons, heavy armor and strong shields. As such, they are often the flagship of any given fleet. While powerful in their own right, they require an escort fleet as they would rapidly fall to Bombers or larger Destroyer groups without them.",
        damage_mults=[0, 0, -5, 0, 0, -2, 3, 0, 0, 0, 0, -3, 30, 10, 10, 3, 3, 3, 0, 0, -2, 0, 0, -20, -30, 0, 0, 0],
        armor=18000,
        shields=2000,
        weapons=2500,
        weapon_type=ShipWeapons.PLASMA.value,
        speed=2500,
        range=ShipRanges.GALACTIC.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-escort-carrier": UnitStatisticsFull(
        name="Escort Carrier",
        description="Escort Carriers were designed to transport small Fighters that cannot cross interstellar distances themselves.",
        description_long="Escort Carriers, designed for transporting small Fighters incapable of interstellar travel, excel in low-priority strategic deployment. Unfortunetly, they are not fast enough to keep pace with combat ships, but they are able to keep pace with Large Cargoships, which is how they go their name.",
        damage_mults=[0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, -3, 8, 4, 4, 0, 0, 0, 0, -2, 0, -15, -15, -20, -15, 0, 0, 0],
        armor=300,
        shields=300,
        weapons=20,
        weapon_type=ShipWeapons.ION.value,
        speed=2200,
        range=ShipRanges.INTERSTELLAR_PLUS.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=400,
        hangar_usage=0,
    ),
    "ship-fleet-carrier": UnitStatisticsFull(
        name="Fleet Carrier",
        description="Fleet Carriers are a larger version of the Escort Carries and are fast enough to keep pace with Cruisers.",
        description_long="Fleet Carriers, an enlarged iteration of Escort Carriers, match the speed of Cruisers while also having enhanced offensive capabilities. While this does not mean that they are designed to engage in the frontline, they are much less likely to fall to a stray bomber that somehow got through its extensive fighter screen.",
        damage_mults=[0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, -3, 15, 5, 5, 2, 2, 2, 0, 0, -2, 0, 0, -20, -30, 0, 0, 0],
        armor=1800,
        shields=2000,
        weapons=160,
        weapon_type=ShipWeapons.ION.value,
        speed=3500,
        range=ShipRanges.GALACTIC.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=2300,
        hangar_usage=0,
    ),
    "ship-titan": UnitStatisticsFull(
        name="Titan",
        description="Titans are gigantic and ludicrously expensive flagships only few can afford. They are a navy's pride.",
        description_long="Titans, colossal and exorbitantly priced flagships, stand as the epitome of a navy's prestige, reserved for the empire few who can afford them. With awe-inspiring damage against any smaller ships, Titans reign supreme on the galactic battlefield and are naval supremacy made manifest.",
        damage_mults=[0, 0, -10, 0, 0, 0, 2, 3, 4, 3, 3, 0, 100, 25, 25, 8, 8, 8, 0, 0, -3, 0, 0, -15, -25, 0, 0, 0],
        armor=220000,
        shields=20000,
        weapons=30000,
        weapon_type=ShipWeapons.PLASMA.value + ShipWeapons.DISRUPTOR.value,
        speed=500,
        range=ShipRanges.GALACTIC.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-sattelites": UnitStatisticsFull(
        name="Sattelites",
        description="Satellites can be used for many purposes, ranging from power generation to spying on others.",
        description_long="Satellites can be used for many purposes, ranging from power generation to spying on others. However, they are EXTREMELY, fragile and will die to just about anything.",
        damage_mults=[-2, 0, 0, 0, -9, -12, -25, -8, -30, -30, -15, -100, 0, 0, -5, 0, 0, -10, -25, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor=1,
        shields=0,
        weapons=0,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=100000,
        range=ShipRanges.INTERPLANETARY.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-small-cargo": UnitStatisticsFull(
        name="Small Cargoship",
        description="Small Cargoships allow trade between different planets and stars in your empire.",
        description_long="Small Cargoships allow trade between different planets and stars in your empire. They are not capable of crossing between different spiral arms without upgrades and have nearly no armor, resulting in them requiring escorts to keep alive.",
        damage_mults=[0, 0, 0, 0, -3, -5, -8, -4, -10, -10, -5, -25, 0, 0, 0, 0, 0, 0, -2, -10, 0, 0, 0, 0, 0, 0, 0, 0],
        armor=120,
        shields=0,
        weapons=0,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=2500,
        range=ShipRanges.INTERSTELLAR_PLUS.value,
        fuel_usage=0,
        cargo_space=30000,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-large-cargo": UnitStatisticsFull(
        name="Large Cargoship",
        description="A larger cargo vessel was needed, and so the Large Cargoship was created. It can cross galactic distances.",
        description_long="A larger cargo vessel was needed, and so the Large Cargoship was created. It has been upgraded to be able to cross between different spiral arms, increased cargo capacity and has also been equipped with some self-defense weapons to reduce the risk of them being destroyed in pirate attacks.",
        damage_mults=[0, 0, 0, 0, -3, -5, -8, -4, -10, -10, -5, -25, 5, 0, 0, 0, 0, 0, -10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor=400,
        shields=20,
        weapons=20,
        weapon_type=ShipWeapons.ION.value,
        speed=2200,
        range=ShipRanges.GALACTIC.value,
        fuel_usage=0,
        cargo_space=750000,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-colony-ship": UnitStatisticsFull(
        name="Colony Ship",
        description="Colony ships carry colonists to distant planets to expand your empire across the entire Galaxy.",
        description_long="Colony ships carry colonists to distant planets to expand your empire across the entire Galaxy.",
        damage_mults=[0, 0, 0, 0, 0, 0, -2, 0, -3, -3, -2, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor=120,
        shields=0,
        weapons=0,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=500,
        range=ShipRanges.INTERSTELLAR_PLUS.value,
        fuel_usage=0,
        cargo_space=750000,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-science-ship": UnitStatisticsFull(
        name="Science Ship",
        description="Science ships can be used to explore deep space and return valuable resources from it.",
        description_long="Science ships can be used to explore deep space and return valuable resources from it.",
        damage_mults=[0, 0, 0, 0, 0, 0, -2, 0, -3, -3, -2, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor=120,
        shields=0,
        weapons=0,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=0,
        range=ShipRanges.INTERSTELLAR_PLUS.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "ship-construction-ship": UnitStatisticsFull(
        name="Construction Ship",
        description="Construction ships can aid in resource production and can be used to create megastructures for your alliance.",
        description_long="Construction ships can aid in resource production and can be used to create megastructures for your alliance.",
        damage_mults=[0, 0, 0, 0, 0, 0, -2, 0, -3, -3, -2, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor=120,
        shields=0,
        weapons=0,
        weapon_type=ShipWeapons.CONVENTIONAL.value,
        speed=0,
        range=ShipRanges.INTERSTELLAR_PLUS.value,
        fuel_usage=0,
        cargo_space=0,
        hangar_space=0,
        hangar_usage=0,
    ),
    "def-aa": UnitStatisticsFull(
        name= "AA Guns",
        description= "AA Guns are small and not very strong, but they are very cheap and can be constructed en masse.",
        descriptionLong= "AA Guns are small and not very strong, but they are very cheap and can be constructed en masse.",
        damageMults= [5, 5, 5, -20, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 8,
        shields= 0,
        weapons= 1,
        weaponType= ShipWeapons.CONVENTIONAL.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    ),
    "def-railgun": UnitStatisticsFull(
        name= "Railgun Turrets",
        description= "Railgun turrets use electromagnets to launch hypersonic slugs at the enemy.",
        descriptionLong= "Railgun turrets use electromagnets to launch hypersonic slugs at the enemy.",
        damageMults= [0, 0, 0, -10, 3, 2, 2, 2, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 40,
        shields= 0,
        weapons= 10,
        weaponType= ShipWeapons.CONVENTIONAL.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    ),
    "def-rocket": UnitStatisticsFull(
        name= "Rocket Launchers",
        description= "Rocket Launchers are able to launch surface-to-orbit missiles tipped with nukes at enemy capital ships.",
        descriptionLong= "Rocket Launchers are able to launch surface-to-orbit missiles tipped with nukes at enemy capital ships.",
        damageMults= [0, 0, 0, -10, 0, 0, 0, 0, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 40,
        shields= 0,
        weapons= 10,
        weaponType= ShipWeapons.CONVENTIONAL.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    ),
    "def-laser": UnitStatisticsFull(
        name= "Laser Turrets",
        description= "Laser turrets are ideal to use against small- or midsized ships due to their comparatively low cost and high output.",
        descriptionLong= "Laser turrets are ideal to use against small- or midsized ships due to their comparatively low cost and high output.",
        damageMults= [5, 5, 5, -5, 20, 20, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 950,
        shields= 0,
        weapons= 120,
        weaponType= ShipWeapons.LASER.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    ),
    "def-ion": UnitStatisticsFull(
        name= "Ion Turrets",
        description= "Ion turrets have the same raw power as lasers, but sacrifice armor for shield strength.",
        descriptionLong= "Ion turrets have the same raw power as lasers, but sacrifice armor for shield strength.",
        damageMults= [5, 5, 5, -5, 20, 20, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 950,
        shields= 1520,
        weapons= 120,
        weaponType= ShipWeapons.ION.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    ),
    "def-plasma": UnitStatisticsFull(
        name= "Plasma Turrets",
        description= "Plasma turrets launch large plasma bolts against medium and large ships to melt their armor away.",
        descriptionLong= "Plasma turrets launch large plasma bolts against medium and large ships to melt their armor away.",
        damageMults= [0, 0, 0, -3, 15, 15, 20, 20, 25, 20, 20, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 2000,
        shields= 100,
        weapons= 220,
        weaponType= ShipWeapons.PLASMA.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    ),
    "def-disruptor": UnitStatisticsFull(
        name= "Disruptor Turrets",
        description= "Disruptor turrets can be used to rapidly disassemble even large capital ships in orbit.",
        descriptionLong= "Disruptor turrets can be used to rapidly disassemble even large capital ships in orbit.",
        damageMults= [0, 0, 0, -3, 5, 5, 15, 15, 20, 30, 30, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 2500,
        shields= 150,
        weapons= 280,
        weaponType= ShipWeapons.DISRUPTOR.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    ),
    "def-s-shield": UnitStatisticsFull(
        name= "Small Shield",
        description= "A small shield generator that can protect the area surrounding it from the enemy. Only one can be built.",
        descriptionLong= "A small shield generator that can protect the area surrounding it from the enemy. Only one can be built.",
        damageMults= [0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 150,
        shields= 1500,
        weapons= 0,
        weaponType= ShipWeapons.CONVENTIONAL.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    ),
    "def-m-shield": UnitStatisticsFull(
        name= "Large Shield",
        description= "A large shield generator that can protect large regions from the enemy. Only one can be built.",
        descriptionLong= "A large shield generator that can protect large regions from the enemy. Only one can be built.",
        damageMults= [0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 3150,
        shields= 31500,
        weapons= 0,
        weaponType= ShipWeapons.CONVENTIONAL.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    ),
    "def-l-shield": UnitStatisticsFull(
        name= "Planetary Shield",
        description= "A gigantic shield generator that can protect the entire planet from the enemy. Only one can be built.",
        descriptionLong= "A gigantic shield generator that can protect the entire planet from the enemy. Only one can be built.",
        damageMults= [0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        armor= 12500,
        shields= 125000,
        weapons= 0,
        weaponType= ShipWeapons.CONVENTIONAL.value,
        speed=None,
        range=None,
        fuel_usage=None,
        cargo_space=None,
        hangar_space=None,
        hangar_usage=None,
    )