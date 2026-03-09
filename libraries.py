# import pandas
# import math
# from math import sin,sqrt
# from datetime import datetime

# txt = '05-02-2026'
# dt = datetime.strptime(txt, '%d-%m-%Y')
# print(dt)

# print(sin(30))
# print(sqrt(2))

# DZ 
# 1
# from datetime import datetime
# date_str = "8-6-2021" # Данные представлены в переменной в виде строки 
# def extract_month_year(date_str): # Функция принимающая один аргумент 
#     dt = datetime.strptime(date_str, '%d-%m-%Y') # Метод datetime.strptime принимает на вход строку и строку с кодами форматирования, которая в точности описывает структуру исходной строки и превращает это в объект datetime
#     dt_cor = dt.strftime("%m-%Y") # Метод dt.strftime берет объект datetime и оформляет в виде строки с кодами форматирования, которые мы указали в скобочках
#     return dt_cor
# print(extract_month_year(date_str))

# print(dt)

# 2
# import math
# num = 694.2933542879372
# def calculate_sqrt(num):
#     return math.sqrt(num)
# print(calculate_sqrt(num))

# 3
# user_times = [649.1769993188137, 599.7554563969355, 114.34563950525333, 153.17823009679933, 265.95693049727976, 727.4932566909035, 88.9022066627403, 753.151709001954, 294.6440146843577, 959.5452803978691, 608.5583526701408]
# import statistics
# def calculate_median(user_times):
#     return statistics.median(user_times)
# print(calculate_median(user_times))
# print(sum(user_times) / len(user_times))