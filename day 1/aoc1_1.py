def get_calib_value(line: str):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first_digit = ""
    last_digit = ""

    for i in line:
        if i in numbers:
            first_digit = i
            break

    for i in line[::-1]:
        if i in numbers:
            last_digit = i
            break

    return int(first_digit+last_digit)

with open('input.txt', 'r') as file:
    sum = 0
    for line in file:
        sum += get_calib_value(line)

    print(sum)
