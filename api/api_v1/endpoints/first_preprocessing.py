from fastapi import APIRouter
from crud.db_crud import read_data

router = APIRouter()

@router.get('/first')
async def frist_preprocess():
    # 1. 데이터 베이스 읽어오기
    data = await read_data()
    return  data

 
    
    
    
    