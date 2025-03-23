from fastapi import FastAPI
from router import packageInfo, download, dependencies, appendPackage

app = FastAPI()

app.include_router(packageInfo.router)
app.include_router(download.router)
app.include_router(dependencies.router)
app.include_router(appendPackage.router)

@app.get('/')
def start():
    return {'message': 'You sent basic request (request to "/"). To use API send request to /api/...'}
