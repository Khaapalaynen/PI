a = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
b = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
arr = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
i = 0
arrLen = len(arr)
for i in range(arrLen):
    if arr[i] == 3:
        arr[i] = 4
while(arr.count(2)):
    arr.remove(2)
print(arr)
    