from fastapi import APIRouter
from crud.db_crud import read_data
import time

router = APIRouter()

update_data = []

@router.get('/second')
async def second_preprocess():
    # 1. 시작 시간 기록
    start_time = time.time()
    print(f"[level 2] Start time: {start_time}", flush=True)

    # 2. 데이터 베이스 읽어오기
    data = await read_data()
    
    #print(data, flush=True)
    
    # 3. 사람 객체만 가져오기 
    for privacy in data:
        privacy = privacy.dict()
        
        for cell in privacy['cells']:
            for person in cell['people']:
                #print(person, flush=True)
                
                # 4. IMSI 정보 지우기 
                del person['IMSI']
                
                # 5. 나이 가명 처리 
                if person['age'] > 20 and person['age'] <30 :
                    person['age'] = 'mid_20s'
                
                elif person['age'] > 30 and person['age'] < 40 :
                    person['age'] = 'mid_30s'
                
                elif person['age'] > 40:
                    person['age'] = 'mid_40s'   
                
                # 6. 전화번호 가명 처리 
                tmp = person['mobile_number'].split('-')
                tmp[1] = '****'
                person['mobile_number'] = '-'.join(tmp)
                                  
        update_data.append(privacy)

    # 7. 종료 시간 기록
    end_time = time.time()
    print(f"[level 2] End time: {end_time}", flush=True)

    # 8. 실행 시간 계산
    execution_time = end_time - start_time
    print(f"[level 2] Execution time: {execution_time} seconds", flush=True)           

    return  update_data