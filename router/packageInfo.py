from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=['package_info'])

@router.get('/package-info')
async def get_package_info(name: str):
    return({'package': name})
    # return(pkglist.get(name, {"error":"package not found"}))