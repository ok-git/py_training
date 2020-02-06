# number = ''  # define var

# waiting for digits only
# while not number.isdigit():
#     number = input("Input number:")
# number = int(number)  # change str to int

number = 128098
print(f"In the number {number}", end=" ")
greater_digit = 0
while number:
    if number % 10 > greater_digit:
        greater_digit = number % 10
    number //= 10
print(f"the greatest digit is {greater_digit}")

# Extended version with greater digit position detection
original_number = 1288
greater_digit = 0
number_length = 0
greater_digit_position = 0
number = original_number
while number:
    number_length += 1
    if number % 10 >= greater_digit:
        greater_digit = number % 10
        greater_digit_position = number_length
    number //= 10
print(f"The number {original_number} consists of {number_length} digits and the greatest digit is {greater_digit} "
      f"in position {number_length - greater_digit_position + 1} (from the left)")
