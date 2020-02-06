sec = ''  # define var

# waiting for digits only
while not sec.isdigit():
    sec = input("Input time in seconds:")
sec = int(sec)  # change str to int

# variant 1
hours = sec // 3600
minutes = sec // 60 % 60
seconds = sec % 60

print(f"v1 {sec} seconds is equal to {hours} hour(s), {minutes} minute(s) and {seconds} second(s) ")

# variant 2
hours = sec // 3600
minutes = sec % 3600 // 60
seconds = sec % 3600 % 60

print(f"v2 {sec} seconds is equal to {hours} hour(s), {minutes} minute(s) and {seconds} second(s) ")
