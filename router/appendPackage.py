from fastapi import APIRouter

router = APIRouter(prefix='/api', tags=['append-package'])

@router.post('/append-package')
async def append_package(name: str, key; str):
    if(key=='testKey12345')
