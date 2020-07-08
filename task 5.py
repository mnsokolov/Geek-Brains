revenue = int(input("Введите выручку фирмы:"))
cost = int(input("Введите издержки фирмы:"))

if cost > revenue:
    print("Ваша фирма работает в убыток")
else:
    print("Ваша фирма работает в прибыль")
    rent = (revenue / cost) * 100
    print("Рентабельность вашей фирмы: {:.2f} %".format(rent))
    staff_count = int(input("Сколько в вашей фирме сотрудников?:"))
    revenue_by_staff = revenue / staff_count
    print("На сотрудника приходится {:.2f} выручки".format(revenue_by_staff))
