from typing import Never as never
import time
import asyncio
from common.lib.fleet import Fleet
from common.db_cache import DBCache
from common.const import FleetMissions, ConsoleShortcuts

async def main(delay: int=1) -> never:
    while True:
        start_time = time.time()

        for fleet in DBCache.recent_fleets.values():

            if not (isinstance(fleet[0].arrival_time, float)):
                continue
            if not (fleet[0].arrival_time <= time.time()):
                continue

            match fleet[0].mission:
                case FleetMissions.HOLD.value:          ...
                case FleetMissions.DEPLOY.value:        _fleet_deploy(fleet)
                case FleetMissions.TRANSPORT.value:     _fleet_transport(fleet)
                case FleetMissions.COLLECT.value:       _fleet_collect(fleet)
                case FleetMissions.SPY.value:           _fleet_spy(fleet)
                case FleetMissions.ATTACK.value:        _fleet_attack(fleet)
                case FleetMissions.EXPLORE.value:       _fleet_explore(fleet)
                case FleetMissions.COLONIZE.value:      _fleet_colonize(fleet)
                case FleetMissions.RECYCLE.value:       _fleet_recycle(fleet)

        elapsed_time = time.time() - start_time
        remaining_time = max(0, delay - elapsed_time)
        if remaining_time == 0: print(f"{ConsoleShortcuts.warn()} The Fleet Manager is lagging behind! {(delay - elapsed_time) * 1000}ms missing!")
        await asyncio.sleep(remaining_time)

def _fleet_deploy(fleet: Fleet):
    pass

def _fleet_transport(fleet: Fleet):
    pass

def _fleet_collect(fleet: Fleet):
    pass

def _fleet_spy(fleet: Fleet):
    pass

def _fleet_attack(fleet: Fleet):
    pass

def _fleet_explore(fleet: Fleet):
    pass

def _fleet_colonize(fleet: Fleet):
    pass

def _fleet_recycle(fleet: Fleet):
    pass