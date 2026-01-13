
startTime, endTime = map(int,input().split())
if endTime > startTime:
    duration = endTime - startTime
elif endTime < startTime:
    duration = (24 - startTime) + endTime
elif startTime == endTime:
    duration = (endTime - startTime) + 24
    
print (f"O JOGO DUROU {duration} HORA(S)")