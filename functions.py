from src import roas_function
# import src
# from src import get_roas, get_cost, exchange
campaigns = [
    {'clicks': 100, 'cpc': 0.50,'revenue': 120},
    {'clicks': 150, 'cpc': 0.60,'revenue': 200},     # Блок с данными по всем компаниям 
    {'clicks': 90, 'cpc': 0.55,'revenue': 100},
    {'clicks': 200, 'cpc': 0.65,'revenue': 280},
    {'clicks': 80, 'cpc': 0.52,'revenue': 95}
]
exchange_rate = 100


if __name__ == '__main__':
    for i, campaign in enumerate(campaigns):             # Блок с итоговым результатом (Тело программы, берет данные и применяет функции)
        roas = roas_function.get_roas(campaign['clicks'],
                        campaign['cpc'],
                        campaign['revenue'])
        print(f'ROAS for campaign {i}: {round(roas,2)}')


# Пример кода, как можно еще лучше и короче написать блок с логикой для этого примера!
# def get_cost(clicks, cpc):
#     print(exchange_rate)
#     return clicks * cpc

# def get_roas(cost, revenue):
#     return revenue / cost

# for i, campaign in enumerate(campaigns):
#     cost = src.get_cost(campaign['clicks'],
#                     campaign['cpc'])            
#     roas = src.get_roas(cost, campaign['revenue'])
#     print(f'ROAS for campaign {i}: {round(roas,2)}')


# total_clicks = sum([x['clicks'] for x in campaigns])  # Списковое включение 
# print(total_clicks)

# lambda функции(синтаксический сахар)
# def get_roas(cost, revenue):
#     return revenue / cost

# get_roas1 = lambda cost, revenue: revenue / cost   #  Пример, как мы запихнули в переменную - функцию в одну строку

# DZ
# 1
# client_name = 'Василий'
# def greet_client(client_name):
#     return print(f'Привет, {client_name}! Добро пожаловать в наш стартап!')
# greet_client(client_name)

# 2
# foreign_sum = '1542.52'
# exchange_rate = '2.32'

# def convert_currency(rate, amount):
#     return amount * rate
# print(convert_currency(float(exchange_rate), float(foreign_sum)))

# 3
# costs = '1264.91'
# revenue = '2784.7'

# def calculate_roi(costs, revenue):
#     return round((revenue-costs)/costs, 2)
# print(calculate_roi(float(costs), float(revenue)))

# 4
# total_costs = '2801.57'
# total_clicks = '705'

# def calculate_cpc(total_costs, total_clicks):
#     return round(total_costs / total_clicks, 2)
# print(calculate_cpc(float(total_costs), float(total_clicks)))

# 5
# total_visitors = '2729'
# buyers = '1579'
# def calculate_conversion(total_visitors, buyers):
#     return round((buyers / total_visitors) * 100, 2)
# print(calculate_conversion(float(total_visitors), float(buyers)))







