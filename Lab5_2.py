data = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
dataLen = len(data)
data = sorted(data)
print('3 лучшие результата - ', data[0],data[1],data[2])
print('3 худшие результата - ', data[dataLen-3],data[dataLen-2],data[dataLen-1])
i = 0
print("Все результаты с 10:")
for i in range(dataLen):
    if data[i]>10:
        print(data[i],end=' ')
