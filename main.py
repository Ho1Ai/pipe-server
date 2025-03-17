from fastapi import FastAPI
from router import packageInfo, download, dependencies

app = FastAPI()

pkglist = {
    "one": {
        "version": "1.0.0",
        "description": "test package"
    }, 
    "two": {
        "version": "1.1.1",
        "description": "test package"
    }, 
    "three": {
        "version": "1.0.2",
        "description": "test package"
    }
} # заглушка, которая будет удалена после организации этого всего дела через базы данных

app.include_router(packageInfo.router)
app.include_router(download.router)
app.include_router(dependencies.router)

@app.get('/')
def start():
    return {'message': 'Trying on FastAPI!'}

# @app.get('/api/package-info')
# def get_package_info(name: str):
#     return(pkglist.get(name, {"error":"package not found"}))