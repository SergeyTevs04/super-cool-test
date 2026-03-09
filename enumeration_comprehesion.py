# comprehension - более короткий перебор списка и применение к нему какой-то логики

# sales = [10, 5, 6, 8, 1]
# total = sum([x for x in sales if x < 10])
# print(total)

# client = {
#     'name': 'Федор',
#     'email': 'fedor@yandex.ru',
#     'reg_date': '2021-01-01',
#     'status': 'active',
#     'n_orders': 12,
#     'total_sales': 100500
# }
# res = []
# for k, v in client.items():
#     if type(v) == int:
#         res.append(v) 
# print(res)

# res = [v for v in client.values() if type(v) == int]
# print(res)

# res = {k: v for k, v in client.items() if type(v) == int}
# print(res)
# enumeration
# sales = [10, 5, 6, 8, 1]
# for i, x in enumerate(sales):
#     if i % 2 == 0:
#         sales[i] *= 2
# print(sales)

# DZ
# 1
# reviews = {'review_0': 3, 'review_1': 2, 'review_2': 3, 'review_3': 4, 'review_4': 4, 'review_5': 3, 'review_6': 2, 'review_7': 3, 'review_8': 5, 'review_9': 2}
# positive_rev = {k: v for k, v in reviews.items() if v >= 4}
# print(positive_rev)

# 2
# feedback_scores = [5, 4, 4, 4, 2, 5, 4, 4, 4, 4]
# dict_enum_rev = {k: v for k, v in enumerate(feedback_scores) if v < 4}
# print(dict_enum_rev)

# 3
# clicks = [63, 97, 78, 124, 87, 111, 62, 100, 145, 102]
# average_clicks = sum(clicks) / len(clicks)
# good_campaings = {k: v for k, v in enumerate(clicks) if v >= average_clicks}
# print(good_campaings)


    



