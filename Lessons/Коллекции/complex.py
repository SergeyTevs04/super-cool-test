# Сложные структуры данных
## Списки списков


# students = [
#     [5, 2, 3, 3, 5],
#     [3, 2, 3, 3, 3],      # Также можно поступать с: Кортеж кортежей, Кортеж списков, Список кортежей
#     [5, 4, 5, 5, 5]
# ]
# print(students)
# # Извлечение данных 
# print(students[0][0])
# # Редактирование данных
# students[0][0] = 1
# print(students)

# # Списки словарей 
# users = [
#     {'name': 'Alex', 'reg_date': '2021-01-01'},
#     {'name': 'Maria', 'reg_date': '2022-01-01'},
#     {'name': 'Feder', 'reg_date': '2023-01-01'}
# ]
# print(users)
# # Извлечение данных
# # u = users[0]
# print(users[0]['name'])

# # Словари списков
# students = {
#     'Alex': [5, 2, 3, 3, 5],
#     'Maria': [3, 2, 3, 3, 3],      
#     'Fedor': [5, 4, 5, 5, 5]
# }
# print(students['Fedor'][0])
# # Словари словарей
# stats = {
#     '2023-01-01': {'n_visitors': 100, 'revenue': 0},
#     '2023-01-02': {'n_visitors': 235, 'revenue': 15},
#     '2023-01-03': {'n_visitors': 536, 'revenue': 30}
# }
# print(stats['2023-01-03']['n_visitors'])

# # Перебор и агрегирование 
# total_revenue = 0
# for date in stats:
#     total_revenue += stats[date]['revenue']
#     print(total_revenue)


# total_revenue = sum([date['revenue'] for date in stats.values()])  # Вот эти 2 блока кода делают одно и тоже!
# print(total_revenue)

# # Добавление значений 
# stats['2023-01-04'] = {'n_visitors': 736, 'revenue': 50}
# total_revenue = sum([date['revenue'] for date in stats.values()])  
# print(total_revenue)

# stats['2023-01-05'] = 'ХАХА, вас взломали!'
# print(stats)

# # Удаление значений 
# print(students['Alex'].pop(0))
# print(students)


# del stats['2023-01-01']
# print(stats)

# print(type(x)) # 1 - Определяем тип данных
# print(x.keys()) # 2 - Обращаемся к ключам 
# print(x['context']) # 3 Обращаемся к определенному ключу и смотрим внутрь него(есть ли еще там что-то?)
# print(type(x['context'])) # 4 Определяем тип данных вложенных в этот ключ
# print(x['context'].keys()) # 5 Обращаемся к ключам этого(вложенного словаря)
# print(x['context']['callback']) # 6 Обращаемся к более низкому уровню словаря 
# print(type(x['context']['callback'])) # 7 Определяем тип данных этого(более низкого уровня словаря)
# print(x['context']['callback'].keys()) # 8 (Увидели, что и у него тоже есть ключи) Обращаемся к ключам этого(более низкого уровня словаря)
# print(x['context']['callback']['Data']) # 9 (Увидели какой-то нужный ключ) Обращаемся к этому уровню
# print(type(x['context']['callback']['Data'])) # 10 Проверяем его тип данных
# print(x['context']['callback']['Data'].keys()) # 11 (И у него тоже есть ключи) Обращаемся к ключам
# keys = list(x['context']['callback']['Data'].keys())
# keys.sort()
# print(keys)
# print(x['context']['callback']['Data']['ApiPartnerParams']['install_referrer_referal_time']) # Было еще 2 уровня, и только после этого чдобрались до нужного значения!

# DZ
# 1
# products = [{'name': 'product2', 'available': True}, {'name': 'product8', 'available': False}, {'name': 'product4', 'available': False}, {'name': 'product3', 'available': False}, {'name': 'product9', 'available': False}]
# product_name = 'product4'
# # if (продукт есть на складе):
# #     print(f"Продукт {p} доступен на складе.")
# # else:
# #     print(f"Продукт {p} не доступен на складе.")

# for x in products:
#     if product_name in x['name']:
#         if x['available'] == True:
#             print(f"Продукт {product_name} доступен на складе.")
#         else:
#             print(f"Продукт {product_name} не доступен на складе.")
            


        
   

# 2
# order = [
#     {'name': 'product4', 'price': 43.01377955139875, 'quantity': 5},
#     {'name': 'product9', 'price': 42.21968733051901, 'quantity': 10},
#     {'name': 'product8', 'price': 20.362743852479866, 'quantity': 4},
#     {'name': 'product3', 'price': 44.84208175532348, 'quantity': 7},
#     {'name': 'product1', 'price': 32.31450451851001, 'quantity': 8}
# ]

# total_price = 0
# for x in order:
#     total_price += x['price'] * x['quantity']
# print(total_price)

# 3
# sales_data = {
#             'Kuwait': [{'name': 'Headphones', 'quantity': 42}, {'name': 'Tablet', 'quantity': 16}, {'name': 'Laptop', 'quantity': 42}],
#             'French Polynesia': [{'name': 'Desktop PC', 'quantity': 40}, {'name': 'Headphones', 'quantity': 20}, {'name': 'Printer', 'quantity': 11}],
#             'Lesotho': [{'name': 'Desktop PC', 'quantity': 2}, {'name': 'Laptop', 'quantity': 10}, {'name': 'Router', 'quantity': 17}],
#             'Brazil': [{'name': 'Desktop PC', 'quantity': 33}, {'name': 'Laptop', 'quantity': 13}, {'name': 'Smartphone', 'quantity': 30}],
#             'Australia': [{'name': 'Laptop', 'quantity': 37}, {'name': 'Smartwatch', 'quantity': 30}, {'name': 'Router', 'quantity': 47}]
# }
# country_total_sales = 0
# best_country = None
# # for k, v in sales_data.items():
# #     # print(k, v[0]['quantity']+ v[1]['quantity']+ v[2]['quantity'])
# #     if v[0]['quantity']+ v[1]['quantity']+ v[2]['quantity'] > country_total_sales:
# #         country_total_sales = v[0]['quantity']+ v[1]['quantity']+ v[2]['quantity']
# #         best_country = k
# # print(best_country)

# 4

# clients_data = [
#     ('Joe Smith', 20),
#     ('George Hanna', 8),
#     ('Tami Foster', 19),
#     ('Tami Foster', 23),
#     ('Edwin Davies', 14), ('David Gonzalez', 14), ('Edwin Davies', 20), ('Michelle Wright', 13), ('Tina Wilson', 11), ('Tami Foster', 10)]
# total_uniq = []
# for x in clients_data:
#     if x[0] not in total_uniq:
#         total_uniq.append(x[0])
# print(len(total_uniq))

# 5
# clients_data = [('Brendan Novak', 17), ('Jenny Fisher', 13), ('Michael Carpenter', 2), ('Amber Newton', 14), ('Cynthia Stark', 2), ('Julia Morgan', 6), ('Seth Fox', 2), ('Kristen Gonzalez', 16), ('Michael Carpenter', 3), ('Cynthia Stark', 7), ('Seth Fox', 16), ('Michael Carpenter', 9), ('Victoria Hayes', 20), ('Julia Morgan', 14), ('Julia Morgan', 21), ('Jenny Fisher', 23), ('Victoria Hayes', 11), ('Victoria Hayes', 20), ('Julia Morgan', 6), ('Kristen Gonzalez', 20), ('Cynthia Stark', 14), ('Seth Fox', 6), ('Jenny Fisher', 7), ('Seth Fox', 23), ('Julia Morgan', 15), ('Seth Fox', 22), ('Victoria Hayes', 5), ('Seth Fox', 20), ('Julia Morgan', 19), ('Cynthia Stark', 21)]
# morning_uniq = set()
# day_uniq = set()
# evening_uniq = set()
# night_uniq = set()
# for x in clients_data:
#     if 6 <= x[1] < 12:
#         morning_uniq.add(x[0])
#     elif 12 <= x[1] < 18:
#         day_uniq.add(x[0])
#     elif 18 <= x[1] < 24:
#         evening_uniq.add(x[0])
#     elif 0 <= x[1] < 6:
#          night_uniq.add(x[0])
# print(len(morning_uniq), len(day_uniq), len(evening_uniq), len(night_uniq), sep=', ')




    
    
