from fastapi import APIRouter, HTTPException
from db_dir.db import fetchPackageInfo, insertPackage
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/api")

class PackageRequest(BaseModel):
    name: str
    version: str
    dependencies: List[str]
    key: str

@router.get('/package-info')
async def get_package_info(name: str):
    pkg = await fetchPackageInfo(name)
    if not pkg:
        raise HTTPException(status_code=404, detail="Couldn't find package. Are you sure you want to find this package?")
    return dict(pkg)
    #return({'package': name})
    # return(pkglist.get(name, {"error":"package not found"}))

@router.post('/append-package')
async def append_package(pkg: PackageRequest):
    if(pkg.key == 'testKey12345'):
        await insertPackage(pkg.name, pkg.version, pkg.dependencies)
        return {"message":"Package added succesfully"}
