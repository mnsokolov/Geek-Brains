current_result = int(input("Сколько вы сейчас пробегаете?:"))
target_result = int(input("А сколько хотите?:"))
days = 0

while current_result <= target_result:
    days = days +1
    current_result = current_result * 1.1

print(f"Вы добьтесь результата на {days} день")
