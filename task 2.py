user_seconds = int(input("Введите количество секуд:"))
hours = user_seconds // 3600
minutes = (user_seconds // 60) % 60
seconds = user_seconds % 60

print(f"Вы ввели {hours} часов, {minutes} минут и {seconds} секуд")
