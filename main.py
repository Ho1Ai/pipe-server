from fastapi import FastAPI
from router import packageInfo, download, dependencies, appendPackage

app = FastAPI()

app.include_router(packageInfo.router)
app.include_router(download.router)
app.include_router(dependencies.router)
app.include_router(appendPackage.router)

@app.get('/')
def start():
    return {'message': 'routes: \n/api/package-info - receive package info: name, dependencies, current version and id in database table;\n/api/append-package - add package to database. Can be used just for tests and will be removed or rewritten on release. File in testFiles directory and name of the package in the database table must have same names;\n/api/dependencies-list - list of dependencies. Will be used by client side of package manager;\n/api/download - download package. At the moment you can use "curl -O localhost:8000/api/download?name=package_name" (instead of package_name use package from testFiles and database. Both must have same names).\n'}
