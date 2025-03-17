from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter(prefix="/api", tags=['download'])

@router.get('/download')
async def download_pkg(name: str):
    pathname = '../testFiles/' + name + '.txt'
    test_file = os.path.join('testFiles', name)
    if os.path.exists(test_file):
        return(FileResponse(test_file))
    return({'package': name})
    # return(pkglist.get(name, {"error":"package not found"}))