file = open('C:/TrainList.txt', "r", encoding='UTF-8')
TrainList = file.read().splitlines() #txt파일 내용을 \n 제거 후 TrainList에 저장
del TrainList[0]
for l in range(0,len(TrainList)) :      #TrainList를 이중 리스트로 구현
    n = TrainList[l].split()
    TrainList[l] = n
file.close()
