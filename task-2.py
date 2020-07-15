count = 1
l = []

while count <= 5:
    l.append(input("Введите элемент массива: "))
    count += 1

print("Вы задали массив:", l)
tmp = 0

for i in range(int(len(l) / 2)):
    l[tmp], l[tmp + 1] = l[tmp + 1], l[tmp]
    tmp += 2

print("Измененный массив: ", l)
