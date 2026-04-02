import os
import csv
import json

# print(os.getcwd())

# target_dir = 'src'
# os.chdir('/Users/sergejtevs/Desktop/Projects/ecom')

# obj = os.listdir()

# for o in obj:
#     print(o,
#           os.path.isfile(o),
#           os.path.isdir(o),
#           os.path.exists(o))
    
# data_file = 'data.csv'
# print(data_file, 'exists', os.path.exists(data_file))

# if os.path.exists(data_file):
#     ...

# open a file
# with open('if.py', 'r') as f:      # Команда просто на чтение 
#     txt = f.read()
#     lines = f.readlines()
#     for line in f:
#         print(line)

# with open('if.py', 'a') as f:      # Команда на добавление, но к уже существующей наполнености файла
#     f.write('Привет!\n')

# with open('test.txt', 'w') as f:   # Команда на запись, но каждый раз начинаешь с пустого файла
#     f.write('Привет b!\n')
#     f.writelines(['один\n', 'dva\n', 'tri\n'])

# CSV
# comma-separated-values
# new_user = ['Ivan,Ivan', 'Ivanov', 40]

# with open('users.csv', 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(new_user)

# one_more_new_user = {
#     'name': 'Alexsander',
#     'last_name': 'Pushkin',
#     'is_alive': False,
#     'books': ['Капитанская дочка', 'Евгений Онегин']
# }
# # with open('test.txt', 'w') as f:   
#      f.write(json.dumps(one_more_new_user))

# json формат - это всего лишь строка, отформатированная специльаным способом, чтобы все ее могли понять(В том числе, другие языки программирования)
# with open ('test.txt', 'r') as f:
#      line = f.readline()
#      print(line)
#      u = json.loads(line) # json.loads - С помощью этого перевел строку в Питоновский объект(В нашем случае - в словарь)
#      print(u['name'])

# with open ('test.txt', 'r') as f:
#      u = json.load(f)  # Тоже самое, только короче и удобнее
#      print(u['name'])



# json.dumps() # С помощью этого записывает файл в json формат
# json.loads()

# print(os.getcwd()) # Получаем директорию в которой работаем 
# print(os.listdir()) # Получаем список объектов, находящиеся в этой директории
target_dir = '/Users/sergejtevs/Desktop/Projects/ecom/data_processor'
os.chdir(target_dir)

obj = os.listdir()
for o in obj:
    print(o, os.path.isfile(o), os.path.isdir(o), os.path.exists(o))

data_file = 'data.csv'
print(data_file, 'exsists?', os.path.exists(data_file)) # Существует ли вообще такой объект?

# if os.path.exists(data_file): 

# os.path.join(path, *paths) # Где, path - начальный путь, а paths - компоненты пути. Возвращаемое значение - конкатенация пути path и компонентов *paths.
# os.path.basename(file) # Функция, которая принимает на входе адрес файла и возвращает на выходе именно файл(название)
# os.path.dirname(file) # Функция, которая принимает адрес файла и отдает нам путь без basename(без названия этого файла в конце пути)
# os.replace(file, путь) # Функцию os.replace() можно использовать для перемещения файлов или каталогов:
# заменить (переместить) этот файл в другой каталог
# os.replace("renamed-text.txt", "folder/renamed-text.txt")
# Стоит обратить внимание, что это перезапишет путь, поэтому если в папке folder уже есть файл с таким же именем (renamed-text.txt), он будет перезаписан.









    

