import os
import json
import sys
from datetime import datetime
WD = os.path.dirname(sys.argv[0]) # Sys.argv[0] получаем адрес файла в котором мы запустили, А os.path.dirname делает из адреса файла - только название директории(с адресом конечно). В итого получаем актуальную директорию из которой запускаем программу 
PATH_INBOX = os.path.join(WD, 'inbox') # По сути, метод os.path.join объеденяет пути указанные в параметрах и присваивает путь к переменной PATH_INBOX
PATH_PROCESSED = os.path.join(WD,'processed')
PATH_ARCHIVE = os.path.join(WD,'archive')

def get_files(path): # Создаем функция получения файлов с одним параметром 
    files = os.listdir(path) # В переменную files присваиваем список файлов от(path)
    return [os.path.join(path, x) for x in files] # Здесь мы вернем список файлов состоящий из названий файлов, которые прилеплены к адресу папки в которой они лежат
    

def process_files(files): # Создаем функцию обработки файлов от(файлов)
    full_data = {} # Создаем пустой словарь(Который будет содержать в себе результат всех файлов) в переменной full_data 
    for file in files: # Идем по каждому файлу в files
        processed_data = process_file(file) # Результат новой функции process_file от(файл), которая процессит один файл, записываем в переменную processed_data
        for k, v in processed_data.items(): # Пошли циклом по ключу и значению в преобразованном кортеже(из словаря)
            if k in full_data.keys(): # Если ключ присутствует среди ключей словаря full_data
                full_data[k] += v # То мы к уже существующему ключу(то есть к ему значению!) прибавляем значение из нашего преобразованного кортежа
            else: # Если нет этого ключа
                full_data[k] = v # То в словаре full_data создаем этот ключ(из кортежа) и присваиваем ему значение(тоже из кортежа)
        archive(file) # И этот файл становится аргументом к функции архивации
    return full_data # Функция возвращает словарь full_data

def archive(file, to_dir=PATH_ARCHIVE): # Создаем функцию архивации файла, она будет переносить файл из одной папки в другую 
    filename = os.path.basename(file) # Принимаем на входе адрес файла и возвращаем на выходе именно файл(название) и записываем результат в перменную filename
    os.replace( # Перемещаем этот файл в другой каталог(В нашем случае в архив)
        file,
        os.path.join(to_dir, filename)
    )


# {
#   "timestamp": "2023-08-18 09:15:25",
#   "user_id": "U12345",
#   "item": "The Great Gatsby",
#   "quantity": 1,
#   "total_price": "$20.00"
# }

def process_file(file): # Создаем функцию, которая процессит файл от(файл)
    output = {}
    with open(file, 'r') as f: # Открываем файл на чтение от(файл)
        for line in f: # Бежим по строкам в этом файле
            data = json.loads(line) # Преобразую строку(которая в json формате) в словарь(Питоновский объект) и записываю в переменную data
            item = data['item'] # Находим в строках ключ 'item' и записываем их в переменную item
            quantity = data['quantity'] # Находим в строках ключ 'quantity' и записываем их в перменную quantity
            if item in output.keys(): # Среди ключей словаря output.keys(), присутствует ключ переменной item?
                output[item] += quantity # То прибавь к этому ключу еще значение от переменной quantity(тут тоже лежит значение)
            else: # Если нет этого ключа среди ключей словаря output.keys()
                output[item] = quantity # То создай ключ(item) и присвой ему значение переменной(quantity, которая тоже является каким-то ключом со значением)
    return output # Возвращай этот словарь 

def save_data(data, dir=PATH_PROCESSED): # Создаем функцию сохранения данных(В качестве параметров указываем 1 - какие даные, 2 - куда сохраняем(Значением по умолчанию ставлю название папки))
    now = str(datetime.now()) # В переменную now запихиваем строку из преобразованного объекта времени 
    path = os.path.join(dir, now + '_processed.json') # Присоединяем каталог и переменную со времнем к переменной path
    with open(path, 'w') as f:
        json.dump(data, f) # Записываем файл в json формат


def main():
    files = get_files(PATH_INBOX) # В переменную files засунули функцию получение_файлов(от какой директории)
    if len(files) > 0: # Пишем - если там какие то файлы есть
        processed_data = process_files(files) # В переменную processed_data засунули функцию обработки(от файлов)
        save_data(processed_data)
    print(f'{datetime.now()} - {len(files)} processed') # В такое то время программа закончила выполняться и она обработала столько-то файлов 

# if __name__ == '__main__': # ?
#     main()

