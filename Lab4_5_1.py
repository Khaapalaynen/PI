import Lab4_5_2
import math

def Ruc():
    print('Введите стороны a,b:')
    a,b = int(input()),int(input())
    print('Введите градус угла С:')
    c = int(input())
    s = 0.5*a*b*math.sin(math.radians(c))
    return round(s)

print('Формула Герона - ', Lab4_5_2.Geron(5,6,5))
print(Ruc())