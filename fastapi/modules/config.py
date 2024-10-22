from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from modules.env import env
from enum import Enum
import asyncpg

# VARS #
SECRET_VALUE = env.FASTAPI_KEY
SECRET_HEADER = 'X-API-Key'


docs_title = 'Acubot'
docs_description = 'https://github.com/fuad00/acubot'

class Tags(Enum):
    init = "Init"
    scan = "Scan"



def auth401():
    X_API_KEY = APIKeyHeader(name=SECRET_HEADER)

    def api_key_auth(x_api_key: str = Depends(X_API_KEY)):
        if x_api_key != SECRET_VALUE:
            raise HTTPException(status_code=401)

    auth_dep = [Depends(api_key_auth)]
    return auth_dep

def api_init():

    app = FastAPI(
        # docs_url = None, # Disable docs (Swagger UI)
        # redoc_url = None, # Disable redoc
        dependencies = auth401(),
        title = docs_title,
        description = docs_description,
        )

    return app


# asyncpg wrapper
"""
Usage example:

db = PostgreSQL()
await db.execute("CREATE TABLE IF NOT EXISTS ...")
row = await db.fetch("SELECT * FROM test LIMIT 1")
rows = await db.fetchall("SELECT * FROM test")
"""
class PostgreSQL():
    def __init__(self):
        self.pool = None
 
    async def connect(self):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(env.POSTGRES_DSN)
            return self
 
    async def disconnect(self):
        if self.pool is not None:
            await self.pool.close()
 
    async def execute(self, query: str, args = ()):
        await self.connect()
 
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                await connection.execute(query, *args)
 
    async def fetch(self, query: str, args = (), count: int = 1, cache: bool = False):
        await self.connect()
 
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                cursor = await connection.cursor(query, *args)
                response = await cursor.fetch(count)
 
                if count == 1 and len(response) > 0:
                    return dict(response[0])
 
                return response if len(response) > 0 else None
 
    async def fetchall(self, query: str, args = ()):
        await self.connect()
        
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                return await connection.fetch(query, *args)
 