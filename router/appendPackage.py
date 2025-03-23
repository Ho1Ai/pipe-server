from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from db_dir.db import fetchPackageInfo, insertPackage

class PackageRequest(BaseModel):
    name: str
    version: str
    dependencies: List[str]
    key: str
    pkg_type: str

router = APIRouter(prefix='/api')

@router.post('/append-package')
async def append_package(pkg: PackageRequest):
    if(pkg.key == 'testKey12345'):
        if(pkg.pkg_type == 'app' or pkg.pkg_type == 'lib'):
            await insertPackage(pkg.name, pkg.version, pkg.dependencies, pkg.pkg_type)
            return {"message": "Package added succesfully"}
        else:
            return {"message": "You can't use this type of package; you can use next types of packages: lib, app"}
