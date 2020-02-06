text = ["выручки", "издержек"]
revenue, expenses = (int(input(f"Введите значене {text[i]}, руб: ")) for i in range(2))

# revenue, expenses = 100, 80

income = revenue - expenses

if income > 0:
    print(f"Фирма отработала с прибылью {income} руб.")
    print(f"Рентабельность составила {income / revenue * 100 } %")
    staff = int(input("Сколько человек работает в компании? "))
    print(f"Прибыль фирмы на одного сотрудника {income / staff} руб.")
else:
    print(f"Фирма отработала с убытком {income}")
