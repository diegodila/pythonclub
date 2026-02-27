from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/users')
async def get_my_users():
    return {"id":"retornando meu id 1"}