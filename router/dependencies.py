from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=['get_dependencies'])

@router.get('/dependencies-list')
async def get_package_dependencies(name: str):
    return({'this package -> package dependencies': ['qt', 'gtk', 'glibc']})
    # return(pkglist.get(name, {"error":"package not found"}))