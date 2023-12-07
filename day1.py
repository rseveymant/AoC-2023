import re

def calculate_sum_of_calibration_values(file_path):
    with open(file_path, "r") as file:
        document = file.readlines()

    sum_of_values = 0
    for line in document:
        line = line.strip()
        first_digit = re.search(r'\d', line)
        last_digit = re.search(r'\d(?=[^\d]*$)', line)
        if first_digit and last_digit:
            sum_of_values += int(first_digit.group() + last_digit.group())

    return sum_of_values

sum_of_values = calculate_sum_of_calibration_values("day1data.txt")

print(f"The sum of all the calibration values is: {sum_of_values}")
