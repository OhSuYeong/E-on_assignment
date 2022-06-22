import Database
data = Database.booklist #booklist를 data에 저장

def menu() : #메뉴 출력 함수
    print("==도서관리 프로그램==")
    print("1.도서 추가")
    print("2.도서 검색")
    print("3.도서 정보 수정")import DataBase
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
    print("4.도서 삭제")
    print("5.현재 총 도서 목록 출력")
    print("6.저장")
    print("7.프로그램 나가기(자동저장)")
    print("*주의 사항 : 항목의 범위에서 벗어나는 번호는 입력하시면 안됩니다.")

def add() : #도서 추가 함수
    newbook= input("\n도서명, 저자, 출판연도, 출판사명, 장르를 입력하세요(,로 구분) : ").split(",") #newbook에 리스트 저장
    Database.booklist.append(newbook) #booklist에 새로운 리스트 newbook을 추가, append는 원소 마지막에 추가하기 위해 사용
    print("추가 완료")


def find() : #도서 검색 함수
    print("\n1.도서명 2. 저자 3. 출판일 4. 출판사명 5. 장르")
    fnum = int(input("\n검색 수단(숫자로 고를 것) : ")) #검색 수단을 고르기 위한 변수 선언
    if fnum == 1 : #1로 저장이 되어있으면
        bname = input("\n도서명 : ") #bname이라는 변수에 도서명을 저장
        for i in range(0,len(data)) : #리스트에서 해당 도서 검색을 위해 리스트 길이만큼 반복해서
             if(bname == data[i][0]) : #해당되는 리스트에서 도서명만 비교해서 같으면
              print(data[i]) #해당 리스트 출력
    elif fnum == 2 : 
        name = input("\n저자 : ")
        for i in range(0,len(data)) :
             if(name == data[i][1]) :
              print(data[i])  
    elif fnum == 3 :
        pdate = input("\n출판일 : ")
        for i in range(0,len(data)) :
             if(pdate == data[i][2]) :
              print(data[i])
    elif fnum == 4 :
        pname = input("\n출판사명 : ")
        for i in range(0,len(data)) :
             if(pname == data[i][3]) :
              print(data[i])
    elif fnum == 5 :
        genre = input("\n장르 : ")
        for i in range(0,len(data)) :
             if(genre == data[i][4]) :
              print(data[i]) 
    else:
        print("잘못된 접근입니다")


def modify() : #도서 정보 수정 함수
    i = int(input("\n수정할 도서데이터 번호 입력(1번부터 시작) : ")) - 1 #수정 도서 선택, 리스트는 0부터 시작하기 때문에 1번인 경우 1대신 0으로 바꿔줘야함
    print("\n1.도서명 2. 저자 3. 출판일4. 출판사명 5. 장르")
    mnum = int(input("\n수정할 정보(숫자로 고를 것) : ")) #mnum라는 변수에 수정할 정보를 고르는 번호 저장
    if mnum == 1 : #만약 mnum가 1일 경우
        data[i][0] = input("\n수정내용 : ") #수정할 도서명 리스트에 저장
        print("수정완료")
    elif mnum == 2 :
        data[i][1] = input("\n수정내용 : ")
        print("수정완료")
    elif mnum == 3 :
        data[i][2] = input("\n수정내용 : ")
        print("수정완료")
    elif mnum == 4 :
        data[i][3] = input("\n수정내용 : ")
        print("수정완료")
    elif mnum == 5 :
        data[i][4] = input("\n수정내용 : ")
        print("수정완료")
    else:
        print("잘못된 접근입니다")       


def delete() : #도서 삭제 함수
    i = int(input("\n삭제할 도서데이터 번호 입력(1번부터 시작) : ")) - 1 #삭제 도서 선택, 리스트는 0부터 시작하기 때문에 1번인 경우 1대신 0으로 바꿔줘야함
    del data[i] #해당 도서 삭제
    print("삭제완료")


def list_print() : #현재 총 도서 목록 출력 함수
    for i in range(0,len(data)) : #리스트 길이만큼 반복
        print(i+1,"번", "도서명 :", data[i][0],"/ 저자 :", data[i][1], "/ 출판일 :", data[i][2], "/ 출판사명 :", data[i][3], "/ 장르 :", data[i][4])


def save() : #저장 함수
    file=open('c:/input.txt', "w") #쓰기 형태로 파일 열기
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
        file.write("\n")
    print("저장완료")
    file.close()


def close() : #프로그램 나가기(자동저장) 함수
    exit(save())
    
#메인 함수 부분
while True :
    menu()
    num = int(input("\n수행할 기능의 번호를 입력 : "))
    
    if num == 1 :
        add()
    elif num == 2 :
        find()
    elif num == 3 :
        modify()
    elif num == 4 :
        delete()
    elif num == 5 :
        list_print()
    elif num == 6 :
        save()
    elif num == 7 :
        close()
    else:
        print("잘못된 접근입니다")
