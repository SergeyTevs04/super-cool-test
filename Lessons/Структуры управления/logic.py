# окупаемость:
# 1. выручка должна быть больше порогового значения 
# 2. выручка должна быть больше расходов 


# threshold = 1000
# revenue = 1423
# cost = 5234

# large_enough = revenue > threshold
# roas_positive = revenue > cost 

# print(large_enough and roas_positive)





# Петя
# from_moscow = False
# no_recent_purchases = False
# large_check = True

# print((from_moscow and no_recent_purchases) or large_check)

# text = 'Users/sergejtevs/Desktop/Projects/ecom/venv/bin/python /Users/sergejtevs'
# search_query = 'tevs'
# print(f'Нашли {search_query}?', search_query in text)








# DZ
#1
# username = 'aJDLRrWWYmuAGhusQdzqDofb'
# age = 68

# valid_username = 5 <= len(username) <= 20
# valid_age = 0 <= age <= 120
# print(valid_username and valid_age)

#2
# hours = 15
# minutes = 51
# seconds = 35

# valid_time_hours = 0 <= hours <= 23
# valid_time_minutes = 0 <= minutes <= 59
# valid_time_seconds = 0 <= seconds <= 59
# print(valid_time_hours and valid_time_minutes and valid_time_seconds)

# 3
# age = 69
# country = 'СШA'
# countrys = 'Россия' 'США' 'Канада' 'Австралия'
# valid_age = 18 <= age <= 60
# valid_coutry = country in countrys
# print(valid_coutry)


# age = 69
# country = 'США'
# countrys = 'Россия' 'США' 'Канада' 'Австралия'
# valid_age = 18 <= age <= 60
# valid_countrys = country in countrys
# print(valid_age and valid_countrys)

# age = 69
# country = 'США'
# valid_age = 18 <= age <= 60
# valid_countrys = country in 'Россия' 'США' 'Канада' 'Австралия'
# print(valid_age and valid_countrys)

# 4
# password = '7QQxI9TbAaY'
# valid_password = any(c.isupper() for c in password)
# val

# print(valid_password)

#5
# ip_address = '129.108.161.58'
# parts = ip_address.split('.')
# if len(parts) == 4 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit() \
#     and 0 <= int(parts[0]) <= 255 and 0 <= int(parts[1]) <= 255 and 0 <= int(parts[2]) <= 255 \
#         and 0 <= int(parts[3]) <= 255 and not parts[0].startswith('0') and not parts[1].startswith('0') \
#             and not parts[2].startswith('0') and not parts[3].startswith('0'):
#     print(True)
# else:
#     print(False)













