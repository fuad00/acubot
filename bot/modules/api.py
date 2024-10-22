from config import http



async def test():
    r = await http("http://fastapi:8000/init/ping", )

    return r.json()


