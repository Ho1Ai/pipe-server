from fastapi import APIRouter
from fastapi.responses import FileResponse
from db_dir.db import fetchPackageInfo
import os

router = APIRouter(prefix="/api", tags=['download'])

@router.get('/download')
async def download_pkg(name: str):
    #pathname = '../testFiles/' + name
    pkg_data = await fetchPackageInfo(name)
    #print(pkg_data)
    pkg_name = pkg_data.get('server_pkg_name')
    #print(pkg_name) # debug
    #print(pkg_data) # debug
    pkg_type = pkg_data.get('pkg_type') # I don't know do I need it or not... I just keep it here
    pkg_version = pkg_data.get('version')
    pkg_buildtype = pkg_data.get('build_type')
    test_file = os.path.join('testFiles', pkg_name)
    if os.path.exists(test_file):
        return(FileResponse(test_file, headers={"X-Pkg-Type":pkg_type, "X-Pkg-Version":pkg_version, "X-Pkg-Name": pkg_name, "X-Pkg-Buildtype": pkg_buildtype}))
    else:
        return({'Error': 'Package does not exist, unfortunately... As Steve Jobs said: "Let\'s go invent tomorrow rather than worrying about what happened yesterday". Then go and write this application. Go ahead! Good luck! :D'})
    # return(pkglist.get(name, {"error":"package not found"}))
