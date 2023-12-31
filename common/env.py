import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", verbose=True)

DEV_MODE        : bool      = True if os.getenv("DEV_MODE").casefold() == 'true' else False
SPIRAL_CIRCLE   : bool      = True if os.getenv("SPIRAL_CIRCLE").casefold() == 'true' else False
STAR_CIRCLE     : bool      = True if os.getenv("STAR_CIRCLE").casefold() == 'true' else False
SPIRAL_COUNT    : int       = int(os.getenv("SPIRAL_COUNT"))
STAR_COUNT      : int       = int(os.getenv("STAR_COUNT"))
RESOURCE_SPEED  : float     = float(os.getenv("RESOURCE_SPEED"))
FLEET_SPEED     : float     = float(os.getenv("FLEET_SPEED"))
FLEET_MANAGER_DELAY: int    = int(os.getenv("FLEET_MANAGER_DELAY"))