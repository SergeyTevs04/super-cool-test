# Создание
# Из списка 
# categories = ['shoes', 'bags', 'shoes', 'accessories']
# cat_set = set(categories)
# print(cat_set)

# Литерал множества
# campaings = {'brand', 'retargeting', 'search'}
# print(campaings)
# Из строки(уникальный символы)
# letters = set('Hello')
# print(letters)

# Из словаря
# product = {'sku': 123, 'price': 1999, 'name': 'Sneakers'}
# keys = set(product)
# print(keys)

# Добавление и удаления элементов
# segment = {101, 102}
# segment.add(103) # добавить один элемент
# segment.update([104, 105]) # добавить несколько (из итерируемого)
# {101, 102, 103, 104, 105}
# segment.remove(101) # удалить, если точно есть (иначе ошибка)
# segment.discard(999) # удалить, если есть, если нет - тихо пропустить 
# # {102, 103, 104, 105}
# x = segment.pop() # удалить и вернуть 'какой-то' элемент
# print(x)
# segment.clear() # очистить все

# # Удалить дубликанты из списка
# emails = ['a@x', 'b@x', 'a@x', 'c@x']
# uniq_any_order = list(set(emails))
# print(uniq_any_order)

# # Объединение множеств 
# A = {101, 102, 103, 104}
# B = {103, 104, 105}
# reach_total = A | B # или A.union(B)
# print(reach_total) # {101, 102, 103, 104, 105}
# print(len(reach_total)) # 5

# # Пересечение множеств
# A = {101, 102, 103, 104}
# B = {103, 104, 105}
# overlap = A & B # или A.intersection(B)
# print(overlap)
# print(len(overlap))

# # Разность множеств
# A = {101, 102, 103, 104}
# B = {103, 104, 105}
# only_A = A - B
# only_B = B - A
# print(only_A)
# print(only_B)

# # Симметрическая разность 
# A = {101, 102, 103, 104}
# B = {103, 104, 105}
# either_but_not_both = A ^ B
# print(either_but_not_both)

# # Подможества и надмножества 
# required = {'read', 'export'}
# user_perms = {'read', 'write', 'export', 'share'}
# print(required <= user_perms)
# print(user_perms.issuperset(required))

# DZ
# 1
# emails = ['udrz@zqu.com', 'qqiw@sjprre.com', 'htrfdfmq@fvs.com', 'pukxcg@tlxmfu.com', 'udrz@zqu.com', 'udrz@zqu.com', 'pukxcg@tlxmfu.com', 'udrz@zqu.com', 'udrz@zqu.com', 'qqiw@sjprre.com', 'pukxcg@tlxmfu.com', 'udrz@zqu.com', 'pukxcg@tlxmfu.com']
# emails_sets = set(emails)
# print(len(emails_sets))

# 2
# first_suppliers = {'ОптимаЛогистика', 'ЭкспрессДоставка', 'КачествоПлюс', 'БыстрыйСервис'}
# second_suppliers = {'НадежныйПартнер', 'БыстраяДоставка', 'НадежныеПоставки', 'СуперЛогист', 'КачественныйСервис'}
# all_suppl = first_suppliers | second_suppliers
# print(len(all_suppl))

# 3
# first_customers = {'Павел', 'Николай', 'Иван', 'Андрей', 'Юлия'}
# second_customers = {'Ирина', 'Павел', 'Светлана', 'Екатерина', 'Алексей'}
# inter_customers = first_customers & second_customers
# print(len(inter_customers))

# 4
# all_employees = {'Екатерина', 'Иван', 'Ирина', 'Наталья', 'Павел', 'Петр', 'Татьяна', 'Мария'}
# trained_employees = {'Мария', 'Павел', 'Ирина', 'Иван', 'Петр'}
# no_training_employees = all_employees - trained_employees
# print(len(no_training_employees))

# 5
# required_products = {'БлокПитания', 'Докстанция', 'Вебкамера'}
# warehouse_products = {'ВнешнийЖесткийДиск', 'Микрофон', 'Камера', 'Наушники', 'Динамики', 'Клавиатура', 'Мышь'}
# print(required_products <= warehouse_products)