from random import randint

def main():
    ran = randint(1,6)
    print(ran)
    if (ran == 3 or ran == 4):
        return main()
    else:
        return ran

if __name__ == '__main__':
    count = main()
    if count == 5 or count == 6:
        print("Вы победили!")
    elif count == 1 or count == 2:
        print("Вы проиграли!")