from fastapi import APIRouter
from crud.db_crud import read_data
from api.api_v1.endpoints.second_preprocessing import second_preprocess
import time

router = APIRouter()

update_data = []
age = [0, 0, 0, 0]

@router.get('/third')
async def second_preprocess():
    
    # 1. ���� �ð� ���
    start_time = time.time()
    print(f"[level 3] Start time: {start_time}", flush=True)
    
    # 2. ������ ���̽� �о����
    data = await read_data()
    
    
    #print(data, flush=True)
    
    # 3. ��� ��ü�� ��������
    for privacy in data:
        privacy = privacy.dict()
        
        for cell in privacy['cells']:
            #4. age_distribution ����
            del cell['age_distribution']
            
            #5. age_distribution �߰� 
            cell['age_distribution'] ={
                "youth": 0,
                "middle_aged": 0,
                "senior": 0, 
                "elderly": 0
            }
            
            print(cell, flush=True)

            #6. 2�ܰ� ���� ó�� 
            for person in cell['people']:
                
                #print(person, flush=True)
                
                # 7. IMSI ���� �����, ��ȭ��ȣ �����
                del person['mobile_number']
                del person['IMSI']
                
                # 8. ���� ���� ó�� 
                if person['age'] > 20 and person['age'] <30 :
                    person['age'] = 'mid_20s'
                    age[0]+=1
                
                elif person['age'] > 30 and person['age'] < 40 :
                    person['age'] = 'mid_30s'
                    age[0]+=1
                
                elif person['age'] > 40:
                    person['age'] = 'mid_40s'   
                    age[1]+=1
                
            # 9. ���� ���� ������Ʈ
            cell['age_distribution']['youth'] = age[0]
            cell['age_distribution']['middle_aged'] = age[1]
            cell['age_distribution']['senior'] = age[2]
            cell['age_distribution']['elderly'] = age[3]
        
        update_data.append(privacy) 
        
    # 10. ���� �ð� ���
    end_time = time.time()
    print(f"[level 3] End time: {end_time}", flush=True)

    # 11. ���� �ð� ���
    execution_time = end_time - start_time
    print(f"[level 3] Execution time: {execution_time} seconds", flush=True)
                     
    return update_data