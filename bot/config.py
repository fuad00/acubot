from modules.env import env
import httpx

BOT_TOKEN = env.BOT_TOKEN
FASTAPI_KEY = env.FASTAPI_KEY

async def http(url: str, method: str = "GET", headers = None, data = None, json = None, verify = None):
    headers = {"X-API-Key": FASTAPI_KEY}

    try:
        async with httpx.AsyncClient(headers=headers, verify=verify) as req:
            if method != "POST":
                resp = await req.get(url=url) # [GET]
            else:
                resp = await req.post(url=url, data=data, json=json) # [POST] with json in body

            result = resp

    except Exception as e:
        result = {"Success": False, "Reason": str(e)}

    return result

