import asyncio
from time import time

import aiohttp
import requests


class SyncDownload:
    """Exec time = 4.304265737533569"""

    @classmethod
    def get_file(self, url):
        r = requests.get(url, allow_redirects=True)
        return r

    @classmethod
    def write_file(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, "wb") as f:
            f.write(response.content)

    def main(self):
        t0 = time()

        url = "https://loremflickr.com/320/240"

        for _ in range(10):
            self.write_file(self.get_file(url))

        print(time() - t0)


class AsyncDownload:
    """Exec time = 0.4638099670410156"""

    @classmethod
    def write_image(self, data):
        filename = f"file-{int(time() * 1000)}.jpeg"
        with open(filename, "wb") as f:
            f.write(data)

    @classmethod
    async def fetch_content(self, url, session):
        async with session.get(url, allow_redirects=True) as response:
            data = await response.read()
            self.write_image(data)

    @classmethod
    async def main(self):
        url = "https://loremflickr.com/320/240"
        tasks = []

        async with aiohttp.ClientSession() as session:
            for i in range(10):
                task = asyncio.create_task(self.fetch_content(url, session))
                tasks.append(task)

            await asyncio.gather(*tasks)


if __name__ == "__main__":

    # sd = SyncDownload()
    # sd.main()

    t0 = time()
    asd = AsyncDownload()
    asyncio.run(asd.main())
    print(time() - t0)
    ...
