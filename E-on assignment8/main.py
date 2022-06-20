import DataBase
data = DataBase.TrainList #TrainList를 data에 저장
ticket=[]

def menu() : #메뉴 출력 함수
    print("==기차표 예매 프로그램==")
    print("1. 빠른 시간 기차 검색 및 예매")
    print("2. 전체 기차 리스트 출력")
    print("3. 나의 예매 현황 출력 및 예매 취소")
    print("4. 프로그램 종료")

def fast() : #빠른 시간 기차 검색 및 예매
    print("예매할 기차의 정보를 입력해주세요")
    new = input("\n시, 분, 출발역, 도착역, 열차종류(,로 구분) : ").split(",")    #new에 예약정보 저장
    comp=[]
    for i in range(0,len(data)) : #리스트에서 리스트 길이만큼 반복해서
             if(new[2] == data[i][2] and new[3] == data[i][3] and new[4] == data[i][4]) : #해당되는 리스트에서 출발역, 도착역, 열차종류가 같은 경우
                comp=abs((new[0]*60+new[1])-(data[i][0]*60+data[i][1])) #그 중에 제일 가까운 시간을 찾기 위한 계산
    for i in range(0,len(data)) : #리스트에서 리스트 길이만큼 반복해서
            if(min(comp) == abs((new[0]*60+new[1])-(data[i][0]*60+data[i][1]))) :
                print(data[i][0],":",data[i][1], "출발역 :", data[i][2], "도착역 :", data[i][3], "열차종류 :",data[i][4], "잔여석 :",data[i][5])
                getin = int(input("\n예매하시겠습니까?(예매:1, 취소:2) "))
                if getin==1 :
                    data[i][5]= data[i][5]-1
                    ticket = data[i][0]
                    ticket = data[i][1]
                    ticket = data[i][2]
                    ticket = data[i][3]
                    ticket = data[i][4]
                elif getin==2 :
                    close()
                else:
                    print("잘못된 접근입니다.")

def list_print() : #전체 기차 리스트 출력
    for i in range(0,len(data)) : #리스트 길이만큼 반복
        print(i+1,"번", "시간 :", data[i][0],":", data[i][1], "/ 출발 :", data[i][2], "/ 도착 :", data[i][3], "/ 열차종류 :", data[i][4], "/잔여좌석수 :", data[i][5])

def modify() : #나의 예매 현황 출력 및 예매 취소
    print("==나의 예매 현황==")
    print("시간 :", ticket[0],":", ticket[1], "/ 출발 :", ticket[2], "/ 도착 :", ticket[3], "/ 열차종류 :", ticket[4])
    getin = int(input("\n예매를 취소하시겠습니까?(예:1, 아니오:2) "))
        if getin==1 :
            ticket = []
        elif getin==2 :
            close()
        else:
            print("잘못된 접근입니다.")

def save() : #저장 함수
    file=open('C:\Users\오수영\python', "w") #쓰기 형태로 파일 열기
    for i in range(0,len(data)) : #이중 리스트를 다시 txt파일 형태로 바꾸기
        file.write(data[i][0])
        file.write(" ")
        file.write(data[i][1])
        file.write(" ")
        file.write(data[i][2])
        file.write(" ")
        file.write(data[i][3])
        file.write(" ")
        file.write(data[i][4])
        file.write(" ")
        file.write(data[i][5])
        file.write("\n")
    print("저장완료")
    file.close()

def close() : #프로그램 나가기(자동저장) 함수
    exit(save())

while True :
    menu()
    num = int(input("\n수행할 기능의 번호를 입력 : "))
    
    if num == 1 :
        fast()
    elif num == 2 :
        list_print()
    elif num == 3 :
        modify()
    elif num == 4 :
        close()
    else:
        print("잘못된 접근입니다")
