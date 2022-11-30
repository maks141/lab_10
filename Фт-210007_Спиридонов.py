# Ввод
while True:
    n = int(input('Введите N: '))
    if n < 1: 
        print('Введите значение превыщающее ноль!')
    else:
        break

nominals_info = []

# Рассчет
while n >= 64:
    n -= 64
    nominals_info.append(64)

while n >= 32:
    n -= 32
    nominals_info.append(32)

while n >= 16:
    n -= 16
    nominals_info.append(16)

while n >= 8:
    n -= 8
    nominals_info.append(8)

while n >= 4:
    n -= 4
    nominals_info.append(4)

while n >= 2:
    n -= 2
    nominals_info.append(2)

while n >= 1:
    n -= 1
    nominals_info.append(1)


# Вывод
i = 1
while i < 65:
    nominal_count = nominals_info.count(i)
    if nominal_count != 0:
        print(f'Купюр номинала <{i}> испольовано: {nominal_count}')
    i *= 2