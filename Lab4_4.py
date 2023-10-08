def main(*count):
    lenCount = len(count)
    return sum(count)/lenCount

if __name__ == '__main__':
    print('Среднее арифметическое - ', main(1,2,3))
