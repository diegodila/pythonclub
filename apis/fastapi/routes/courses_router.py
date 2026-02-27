from fastapi import APIRouter 

router = APIRouter()

@router.get('/api/v1/courses')
async def get_my_courses():
    
    return {"id":"retornando o id 1"}