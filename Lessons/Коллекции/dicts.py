# Словари

# Создание
# client = {
#     'name': 'Федор',
#     'email': 'fedor@yandex.ru',
#     'reg_date': '2021-01-01',
#     'status': 'active',
#     1: 'foobar'
# }
# Извлечение
# print(client['email'])

# Редактироание и добавление значений 
# client['name'] = 'Константин'
# client['birth_date'] = '1990-01-01'
# print(client) 


# Удаление 
# del client[1]
# print(client)    

# for k in client:
#     print(k, client[k])

# print((client.keys()))
# print((client.values()))
# print()
# print(client.items())

# for k, v in client.items():
#     if k == 'name':
#         print(v)
#     elif k == 'reg_date':
#         foo = v
# print(foo)

# name, email, reg_date, status, birth_date = client.items()
# print(name, email, reg_date, status, birth_date)
 
# x = {
#     'foo': 1,
#     'bar': 2,
# }
# print()
# print(sum(x.values()))

# DZ
# 1
# products = {'mango': 296, 'raspberry': 496, 'kiwi': 237, 'grape': 182}
# product_name = 'grape'
# print(products[product_name])

# 2
# product_info = {'product2': 100, 'product7': 64, 'product3': 99, 'product10': 56, 'product4': 58}
# sales = {'product2': 13}
# for k in sales:
#     if k in product_info:
#         product_info[k] += sales[k] # !!!
# print(product_info)


# 3
# audience_data = {'network6': 19890, 'network5': 18283, 'network8': 15095, 'network7': 13513, 'network4': 19373}
# new_network = 'network15'
# audience_data[new_network] = 0
# print(audience_data)

# 4
# audience_data = {'network8': 5001, 'network1': 11237, 'network9': 10184, 'network2': 16820, 'network6': 10406}
# network = 'network6'
# new_followers = 170
# audience_data[network] += new_followers
# print(audience_data)

# 5
product_info = {'product4': 87, 'product1': 62, 'product6': 82, 'product2': 85, 'product9': 73, 'product5': 90, 'product7': 51, 'product10': 67, 'product8': 60}
for k,v in product_info.items():
    print(k, v)

# 6
# contacts = {'Alex': '+7-916-100-10-10', 'Bob': '+7-916-100-10-11', 'Charlie': '+7-916-100-10-12', 'David': '+7-916-100-10-13', 'Eva': '+7-916-100-10-14'}
# friend_name = 'Alex'
# new_phone = '+7-916-600-60-60'
# contacts[friend_name] = new_phone
# print(contacts)

# 7
# contacts = {'Alex': '+7-916-100-10-10', 'Bob': '+7-916-100-10-11', 'Charlie': '+7-916-100-10-12', 'David': '+7-916-100-10-13', 'Eva': '+7-916-100-10-14'}
# new_friend_name = 'Friend0'
# new_phone = '+7-916-70-70-70'
# contacts[new_friend_name] = new_phone
# print(contacts)
