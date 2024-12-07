from fastapi import APIRouter
from crud.db_crud import read_data
import time

router = APIRouter()


@router.get('/first')
async def frist_preprocess():
    # 1. ���� �ð� ���
    start_time = time.time()
    print(f"[lever 1] Start time: {start_time}")

    # 2. ������ ���̽� �о����
    data = await read_data()

    # 3. ���� �ð� ���
    end_time = time.time()
    print(f"[lever 1] End time: {end_time}")

    # 4. ���� �ð� ���
    execution_time = end_time - start_time
    print(f"[level 1] Execution time: {execution_time} seconds")

    return  data