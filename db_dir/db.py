import asyncpg
from fastapi import FastAPI

DATABASE_URL="postgresql://postgres:root@localhost/pipepackagemanager"

async def dbConnect():
    return await asyncpg.create_pool(DATABASE_URL)

async def fetchPackageInfo(name: str):
    async with await dbConnect() as pool:
        async with pool.acquire() as conn:
            return await conn.fetchrow("select * from packagesList where name = $1", name)

async def insertPackage(name: str, version: str, dependencies: list, pkg_type:str):
    pool = await dbConnect()
    async with pool.acquire() as databasewriter:
        await databasewriter.execute("insert into packagesList (name, version, dependencies, pkg_type) values ($1, $2, $3, $4)", name, version, dependencies, pkg_type)
