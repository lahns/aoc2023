def get_calib_value(line: str):
    text_numbers = {
        "one" : "o1e",
        "two" : "t2e",
        "three" : "t3e",
        "four" : "f4r",
        "five" : "f5e",
        "six" : "s6x",
        "seven" : "s7n",
        "eight" : "e8t",
        "nine" : "n9e"
    }

    for key in text_numbers:
        if key in line:
            line = line.replace(key, text_numbers[key])

    digits = []

    for i in line:
        if i.isdigit():
            digits.append(i)

    return int(digits[0]+digits[-1])

with open('input.txt', 'r') as file:
    sum = 0
    for line in file:
        sum += get_calib_value(line)
    print(sum)

