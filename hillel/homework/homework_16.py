# Author: Maksim Derevianko

def check_number(num: int) -> bool:
    str_num = str(num)
    num_length = len(str_num)
    sum_result = 0
    for x in range(1, num_length + 1):
        sum_result += int(str_num[x - 1]) ** x
    if sum_result == num:
        return True
    else:
        return False


def special_numbers(a: int, b: int) -> list:
    result = []
    for x in range(a, b + 1):
        if check_number(x):
            result.append(x)
        x += 1
    return result


print(special_numbers(1, 10))
print(special_numbers(1, 100))
print(special_numbers(90, 100))
