# 2022 ESW 회의일지
## Built-In Driving Assistant
> 내장형 블랙박스를 이용한 운전자 시야확장 시스템
---
### **220807**
## 역할 재조정
1. Object Detection(이서연)
>   - RPI 환경의 최적의 모델
>   - ADXL MODE, Right MODE, A-Pillar MODE 등 3가지 모델로 개별적 분류
2. 시점변환(박승철)
>   - 블랙박스 시점과 운전자 시점 사이의 차이를 알아내 시점 변환
>   - GAN 염두
3. RPI 여러 대의 통신 및 실시간 화면 스트리밍(정우진)
>   - 동일 네트워크선상에서 영상의 송수신
>   - 
4. 전체 알고리즘 통합 및 환경 조성, ROI등 최적화(신지혜)
>   - FLOW 통합 및 관련 기능 분류
>   - 훈련 Dataset
>   - 기능 최적화

## FLOW
*전체 과정은 .sh로 조절 및 시행되도록 구성*
 1. A-Pillar MODE
> - Real time
> - A필러를 담당하는 Display에 시점변환된 영상 송출<br/>
> - +) 이상주행차량 감지 및 알림
 
 2. ADXL- 경사로 정상 MODE
> - ADXL345의 기울기가 일정 값을 넘으면 작동
> - 블랙박스 화면의 전면에서 Detection  
> -> 오토바이/차량의 전면, 자전거/보행자 등을 감지
 3. Right - 우회전 보조 MODE  
> - 우회전 깜빡이 On 시 차선변경 상황인지 우회전 상황인지 구분  
> -> 앞쪽의 횡단보도 감지, 필요 시 사용자의 수동ON
> - 블랙박스 화면의 우측에서 Detection
>> ``` python
>> if(보행자 신호 == Green):
>>  print("Stop")
>>  if(!detectperson()):
>>      print("No Person")
>>  else:
>>      print("Wait")
>> else :
>>  print("GO")
>>```

### **220809**
## 기술교육지원 변경사항 회의 & 역할 재조정
*기술교육지원 관련 자세한 사항은 `기술지원교육.md` 참고*

### 역할 재조정
> 1. Object Detection, 시점변환은 현재 역할 유지
> 2. 라즈베라파이 연동 관련 역할이 사라짐.
> 3. 기존 4번 항목 `전체 알고리즘 통합 및 환경 조성, ROI등 최적화` 를 분배.
> - 횡단보도 인지 및 우회전 의도 파악 -> 정우진
