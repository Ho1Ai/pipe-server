from fastapi import APIRouter, HTTPException
from db_dir.db import fetchPackageInfo, insertPackage

router = APIRouter(prefix="/api")

@router.get('/package-info')
async def get_package_info(name: str):
    pkg = await fetchPackageInfo(name)
    if not pkg:
        raise HTTPException(status_code=404, detail="Couldn't find package. Are you sure this package is called like this?")
    return dict(pkg)
    #return({'package': name})
    # return(pkglist.get(name, {"error":"package not found"}))
