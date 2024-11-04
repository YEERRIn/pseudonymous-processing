from fastapi import APIRouter
from crud.db_crud import read_data
from api.api_v1.endpoints.second_preprocessing import second_preprocess

router = APIRouter()

update_data = []
age = [0, 0, 0, 0]

@router.get('/third')
async def second_preprocess():
    
    #for문 실행 전에 start 찍기 
    # 1. 데이터 베이스 읽어오기
    data = await read_data()
    
    
    #print(data, flush=True)
    
    for privacy in data:
        privacy = privacy.dict()
        
        for cell in privacy['cells']:
            #2. age_distribution 삭제
            del cell['age_distribution']
            
            #3. age_distribution 추가 
            cell['age_distribution'] ={
                "youth": 0,
                "middle_aged": 0,
                "senior": 0, 
                "elderly": 0
            }
            
            print(cell, flush=True)

            #4. 2단계 가명 처리 
            for person in cell['people']:
                
                #print(person, flush=True)
                
                # 3. IMSI 정보 지우기, 전화번호 지우기
                del person['mobile_number']
                del person['IMSI']
                
                # 4. 나이 가명 처리 
            
                if person['age'] > 20 and person['age'] <30 :
                    person['age'] = 'mid_20s'
                    age[0]+=1
                
                elif person['age'] > 30 and person['age'] < 40 :
                    person['age'] = 'mid_30s'
                    age[0]+=1
                
                elif person['age'] > 40:
                    person['age'] = 'mid_40s'   
                    age[1]+=1
                
            
            
            cell['age_distribution']['youth'] = age[0]
            cell['age_distribution']['middle_aged'] = age[1]
            cell['age_distribution']['senior'] = age[2]
            cell['age_distribution']['elderly'] = age[3]
        
        update_data.append(privacy) 
        
        #end시간 여기다가 찍고 update_data에 시간 추가 -> 화면에 반환하기 
        
                     
    return update_data
        