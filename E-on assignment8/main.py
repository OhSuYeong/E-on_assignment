import DataBase
data = DataBase.TrainList #TrainList를 data에 저장
ticket_number = 0
list_len = 0


def menu() : #메뉴 출력 함수
    print("==기차표 예매 프로그램==")
    print("1. 빠른 시간 기차 검색 및 예매")
    print("2. 전체 기차 리스트 출력")
    print("3. 나의 예매 현황 출력 및 예매 취소")
    print("4. 프로그램 종료")

def fast() : #빠른 시간 기차 검색 및 예매
    search_train = []
    global ticket_number
    
    print("예매할 기차의 정보를 입력해주세요")
    new = input("\n시간(시:분), 출발역, 도착역, 열차종류(,로 구분) : ").split(",")    #new에 예약정보 저장
    for i in range(0,len(data)) : #리스트에서 리스트 길이만큼 반복해서
        if (new[0] == data[i][1]) and (new[1] == data[i][3]) and (new[2] == data[i][4]) and (data[i][5] != '매진') :
            if datetime.datetime(1999, 02, 09, int(new[0][0:2]), int(new[0][3:5])) < datetime.datetime(1999, 02, 09, int(data[i][0][0:2]), int(data[i][0][3:5]) ) :
                search_train = ' '.join(map(str, data[i]))
                ticket_number = i
                break;
    if not search_train  : 
        print("해당 기차의 좌석은 전부 매진됐습니다.\n")
    else : 
        print(search_train, '\n')
        getin = input('해당 기차로 예매하시겠습니까?(예:1, 아니오:2)')

        if(getin == 1) : 
            print("예매되었습니다.\n")
            data[i][5] = int(data[i][5]) - 1

            if data[i][5] == 0 : 
                data[i][5] = '매진'
            file=open('c:/input.txt', "w", encoding='UTF-8') #쓰기 형태로 파일 열기
            for i in range(0,len(data)) :
                    data[i].append('\n')
                    data[i] = ' '.join(map(str, data[i]))
                    file.write(data[i])
                    file.close()
        elif getin == 2 : 
            print("메인화면으로 돌아갑니다.\n")
        else :
            print("잘못된 접근입니다.")

def alllist() : #전체 기차 리스트 출력
    for i in range(0,len(data)) : #리스트 길이만큼 반복
        print(i+1,"번", "시간 :", data[i][0],":", data[i][1], "/ 출발 :", data[i][2], "/ 도착 :", data[i][3], "/ 열차종류 :", data[i][4], "/잔여좌석수 :", data[i][5])

def modify() : #나의 예매 현황 출력 및 예매 취소
    print("==나의 예매 현황==")
    global ticket_number

    if ticket_number == 0:
        print("티켓이 조회되지 않습니다.\n")

    else:
        print("==나의 예매 현황==")
        print(data[ticket_number])
        getin = input("\n 1. 예매 취소\n 2. 뒤로 가기")

        if getin == '1' :
            print("예매가 취소되었습니다.")

            #좌석 연산을 위해 배열로 변환
            temp_list = data[ticket_number].split()
            #좌석이 숫자가 아니라 "매진" 문자열일 확률 고려
            if temp_list[5] == '매진' : temp_list[5] = 1
            else : temp_list[5] = int(temp_list[5]) + 1
            #배열을 문자열로 변환
            data[ticket_number] = ' '.join(map(str,temp_list))

            file=open('c:/input.txt', "w", encoding='UTF-8') #쓰기 형태로 파일 열기
            for i in range(len(data)) :
                file.write(data[i])
                file.close()
                    
            else :
                input("메뉴화면으로 돌아가시려면 아무 키나 눌러주세요.\n")

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
