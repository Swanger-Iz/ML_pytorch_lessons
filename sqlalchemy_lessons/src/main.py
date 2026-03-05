import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

from queries.core import SyncCore
from queries.orm import AsyncOrm, SyncOrm

# SyncCore.create_tables()
# SyncCore.insert_workers()
# SyncCore.select_workers()
# SyncCore.update_worker(1, "Igor Kuchkov")
# SyncCore.select_workers()


async def start_script():
    SyncOrm.create_tables()
    await AsyncOrm.insert_data_workers_resumes()
    await AsyncOrm.join_cte_subquery_window_func()


if __name__ == "__main__":
    asyncio.run(start_script())
