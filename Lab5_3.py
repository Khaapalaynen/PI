one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def Geron(a,b,c):
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s

newOne = sorted(one)
newTwo = sorted(two)
newThree = sorted(three)
print("Площадь из минимальных - ", Geron(newOne[0],newTwo[0],newThree[0]))


newOne = sorted(one, reverse=True)
newTwo = sorted(two, reverse=True)
newThree = sorted(three, reverse=True)
print("Площадь из максимальных - ", Geron(newOne[0],newTwo[0],newThree[0]))