# text = ["первого дня", "целевой"]
# a, b = (int(input(f"Введите результат {text[i]}, км: ")) for i in range(2))

a, b = 2, 3
day_b = 1
while a < b:
    day_b += 1
    a *= 1.10
print(f"На {day_b} день спортсмен достиг результата не менее {b} км.")
