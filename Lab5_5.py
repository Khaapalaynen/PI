list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def transform_numbers_to_sets(numbers):
    result = set()
    for num in numbers:
        if numbers.count(num) > 1:
            num_str = str(num)
            num_set = {num_str * i for i in range(1, numbers.count(num) + 1)}
            result.update(num_set)
        else:
            result.add(num)
    return result

result_set = transform_numbers_to_sets(list_1)
print(result_set)