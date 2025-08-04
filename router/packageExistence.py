from fastapi import APIRouter

router = APIRouter(prefix='/api')

@router.get('/check-existence')
async def checkPackageExistence():
    return{'is_ok': True}
