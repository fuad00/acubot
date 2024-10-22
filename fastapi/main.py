from modules import config
from modules.example import ex
from fastapi import Body

# pre-config #
app = config.api_init()



### Init ###

@app.get("/ping", tags=[config.Tags.observability], summary="Ping the server")
async def func():
    pass
    # r = await api.ping()
    # return r

@app.get("/health", tags=[config.Tags.observability], summary="Check the health of the server")
async def func():
    pass
    # r = await api.ping()
    # return r

### Search ###
# TODO
