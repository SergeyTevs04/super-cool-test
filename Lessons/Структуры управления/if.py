# if elif else

n_good_campaings = 10

revenu = 1534
cost = 6000
threshold = 1000

# revenu > threshold
# revenu > cost
# n_good_campaings += 1
# print Всего хороших компания: n_good_campaings
# Если компания плохая, но количество хороших компаний больше 10
# print Эта компания так себе, но хороших уже много 
# print Эта компания так себе, давайте посмотрим следующую 
# if revenu > threshold:
#     if revenu > cost:
#         n_good_campaings += 1
#         print(f'Всего хороших компаний: {n_good_campaings}')
#     elif n_good_campaings > 10:
#         print('Эта компания так себе, но хороших уже много!')
#     else:
#         print('Эта компания так себе, давайте посмотрим следующую!')

# a = 30
# b = 30
# if a > b:
#     print('a больше b')
# elif a < b:
#     print('a меньше b')
# else:
#     print('a равно b')

# year = 2000
# if year % 4 == 0 and year % 100 != 0:
#     print('Високосный')
# elif year % 400 == 0:
#     print('Високосный')
# else:
#     print('Не високосный')
   
# income = 30000
# if income < 30000:
#     print('Низкий доход')
# elif 30000 <= income <= 100000:
#     print('Средний доход')
# else:
#     print('Высокий доход')

# a = 2
# b = 4
# c = 1
# if a == b and a == c and b == c:
#     print('Равносторонний')
# elif a == b or a == c or b == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# hour = 18
# if 0 <= hour <= 5:
#     print('Ночь')
# elif 6 <= hour <= 11:
#     print('Утро')
# elif 12 <= hour <= 17:
#     print('День')
# else:
#     print('Вечер')

# green = False
# small = False
# if small and green:
#      print('Горошек')
# elif small:
#      print('Вишня')
# elif not small and not green:
#      print('Тыква')
# else:
#      print('Арбуз')

# ip_address = '129.108.161.58'
# parts = ip_address.split('.')
# print(len(parts) == 4 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit() \
# and 0 <= int(parts[0]) <= 255 and 0 <= int(parts[1]) <= 255 \
# and 0 <= int(parts[2]) <= 255 and 0 <= int(parts[3]) <= 255 and len(parts) == 1 or parts[]​ != '0')


# Здесь нет проверки на ведущие нули и я не знаю как их сделать 
# ip_address = '129.108.161.58'
# parts = ip_address.split('.')
# if len(parts) == 4 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit()\
#     and 0 <= int(parts[0]) <= 255 and 0 <= int(parts[1]) <= 255 and 0 <= int(parts[2]) <= 255\
#         and 0 <= int(parts[3]) <= 255:
#     print(True)
# else:
#     print(False)


