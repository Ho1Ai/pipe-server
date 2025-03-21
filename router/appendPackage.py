from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from db_dir.db import fetchPackageInfo, insertPackage

class PackageRequest(BaseModel):
    name: str
    version: str
    dependencies: List[str]
    key: str

router = APIRouter(prefix='/api')

@router.post('/append-package')
async def append_package(pkg: PackageRequest):
    if(pkg.key == 'testKey12345'):
        await insertPackage(pkg.name, pkg.version, pkg.dependencies)
        return {"message":"Package added succesfully"}
