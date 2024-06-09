# Author: Maksim Derevianko

path_read_file = 'files/examples.txt'
path_write_file = 'files/result.txt'


def calculate(line: str) -> int:
    """Написать функцию которая решает пример"""
    return 0


with open(path_read_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    clean_lines = []
    for line in lines:
        line = line.replace('\n', '')
        line = line.strip()
        clean_lines.append(line)
    print(clean_lines)

result_list = []
for line in clean_lines:
    result_list.append(f'{line} = {calculate(line)}')
print(result_list)


with open(path_write_file, 'w', encoding='utf-8') as file:
    for line in result_list:
        file.write(f"{line}\n")


