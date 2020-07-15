split_text = input("Введите предложение: ").split()

for ind, i in enumerate(split_text,1):
    print(ind, i[:10])