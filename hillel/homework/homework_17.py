# Author: Maksim Derevianko

# 1
def sieve(numbers):
    unique_numbers = set(numbers)
    unique_list = list(unique_numbers)
    unique_list.sort(reverse=True)
    result_tuple = tuple(unique_list)

    return result_tuple


print(sieve([11, 12, 39, 12, 3, 11]))
print(sieve([1, 5, 2, 3, 7, 4, 5, 6, 7]))


# 2
def check_number(num: int) -> bool:
    str_num = str(num)
    num_length = len(str_num)
    unique_digits = set()
    for x in range(1, num_length + 1):
        digit = int(str_num[x - 1])
        if digit in unique_digits:
            return False
        unique_digits.add(digit)
    return True


def unique_numbers(a: int, b: int) -> list:
    result = []
    for x in range(a, b + 1):
        if check_number(x):
            result.append(x)
    return result


print(unique_numbers(100, 110))
print(unique_numbers(1, 5))
print(unique_numbers(110, 120))
