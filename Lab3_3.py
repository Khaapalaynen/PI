num = int(input())
if ((num >= 0) and (num <= 10)):
    if (num <= 3):
        print(num, 'в диапозоне от 0 до 3 включительно')
    elif  ((num >= 3) and (num <= 6)):
        print(num, 'в диапозоне от 3 до 6')
    else:
        print(num, 'в диапозоне от 6 до 10 включительно')
else:
    print("Число не в нужном диапозоне")