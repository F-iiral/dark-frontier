from typing import Never as never
import asyncio

async def main(delay: int=1) -> never:
    while True:
        await asyncio.sleep(delay)