# number = ''  # define var

# waiting for digits only
# while not number.isdigit():
#     number = input("Input number:")
# number = int(number)  # change str to int

number = 3

# variant 1
result = number + number*11 + number*111
print(f"v1 Result is {result}")

# variant 2
result = number * 123
print(f"v2 Result is {result}")

# variant 3
result = 0
multiply = [1, 11, 111]
for i in multiply:
    result += number * i
print(f"v3 Result is {result}")
