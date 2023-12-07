import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

DEV_MODE        : bool      = True if os.getenv("DEV_MODE") == 'True' else False
ARM_CIRCLE   : bool      = True if os.getenv("ARM_CIRCLE") == 'True' else False
STAR_CIRCLE     : bool      = True if os.getenv("STAR_CIRCLE") == 'True' else False
ARM_COUNT    : int       = int(os.getenv("ARM_COUNT"))
STAR_COUNT      : int       = int(os.getenv("STAR_COUNT"))
RESOURCE_SPEED  : float     = float(os.getenv("RESOURCE_SPEED"))
FLEET_SPEED     : float     = float(os.getenv("FLEET_SPEED"))