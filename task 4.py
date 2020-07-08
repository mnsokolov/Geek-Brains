user_number = int(input("Введите целое положительное число:"))
max_letter = 0

while user_number > 0:
    letter_for_check = user_number % 10
    user_number = user_number // 10
    if letter_for_check > max_letter:
        max_letter = letter_for_check
    else:
        continue

print(f"Максимальна цифра в числе: {max_letter}")
