file = open('C:\Users\오수영\python', "r")
TrainList = file.read().splitlines() #txt파일 내용을 \n 제거 후 TrainList에 저장
TrainList = TrainList.replace(':', ' ')
TrainList = TrainList.replace('-', '')
TrainList = TrainList.replace('> ', '')
for l in range(0,len(TrainList)) :      #TrainList를 이중 리스트로 구현
    n = TrainList[l].split()
    TrainList[l] = n
file.close()
