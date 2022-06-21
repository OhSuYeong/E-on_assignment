import DataBase
data = DataBase.TrainList #TrainList를 data에 저장
ticket=[]
k=0

def menu() : #메뉴 출력 함수
    print("==기차표 예매 프로그램==")
    print("1. 빠른 시간 기차 검색 및 예매")
    print("2. 전체 기차 리스트 출력")
    print("3. 나의 예매 현황 출력 및 예매 취소")
    print("4. 프로그램 종료")

def fast() : #빠른 시간 기차 검색 및 예매
    print("예매할 기차의 정보를 입력해주세요")
    new = input("\n시, 분, 출발역, 도착역, 열차종류(,로 구분) : ").split(",")    #new에 예약정보 저장
    for i in range(0,len(data)) : #리스트에서 리스트 길이만큼 반복해서
             if(new[2] == data[i][2] and new[3] == data[i][3] and new[4] == data[i][4] and new[0]*60+new[1] <= data[i][0]*60+data[i][1]) : #해당되는 리스트에서 출발역, 도착역, 열차종류가 같고 지나간 열차를 제외하고
                k=i
             else :
                return 0
    print("시간 :", data[k][0],":", data[k][1], "/ 출발 :", data[k][2], "/ 도착 :", data[k][3], "/ 열차종류 :", data[k][4], "/잔여좌석수 :", data[k][5])
    get=input(int("해당 열차를 예매하시겠습니까?(네:1, 아니오:2)"))
            if get==1 :
                    ticket=data
                    data[k][5]-=1
            elif get==2 :
                fast()
            else :
                print("잘못된 접근입니다.")

def alllist() : #전체 기차 리스트 출력
    for i in range(0,len(data)) : #리스트 길이만큼 반복
        print(i+1,"번", "시간 :", data[i][0],":", data[i][1], "/ 출발 :", data[i][2], "/ 도착 :", data[i][3], "/ 열차종류 :", data[i][4], "/잔여좌석수 :", data[i][5])

def modify() : #나의 예매 현황 출력 및 예매 취소
    print("==나의 예매 현황==")
    print("시간 :", ticket[0],":", ticket[1], "/ 출발 :", ticket[2], "/ 도착 :", ticket[3], "/ 열차종류 :", ticket[4])
    getin = int(input("\n예매를 취소하시겠습니까?(예:1, 아니오:2) "))
        if  getin == 1 :
            ticket=[]
            data[k][5]+=1
        elif getin == 2 :
            fast()
        else :
            print("잘못된 접근입니다.")

def close() : #프로그램 나가기 함수
    exit()

while True :
    menu()
    num = int(input("\n수행할 기능의 번호를 입력 : "))
    
    if num == 1 :
        fast()
    elif num == 2 :
        alllist()
    elif num == 3 :
        modify()
    elif num == 4 :
        close()
    else:
        print("잘못된 접근입니다")
