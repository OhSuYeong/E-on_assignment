file = open('c:/input.txt', "r")
booklist = file.read().splitlines() #txt파일 내용을 \n 제거 후 booklist에 저장
for l in range(0,len(booklist)) :      #booklist를 이중 리스트로 구현
    n = booklist[l].split()
    booklist[l] = n
file.close()
