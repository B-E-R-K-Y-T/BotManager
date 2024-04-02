import aiohttp


class AsyncClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def get(self, endpoint, params=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(self._full_url(endpoint), params=params) as response:
                response.raise_for_status()
                return await response.json()

    async def post(self, endpoint, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.post(self._full_url(endpoint), data=data) as response:
                response.raise_for_status()
                return await response.json()

    def _full_url(self, endpoint):
        return f"{self.base_url}{endpoint}"
