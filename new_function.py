def greeting(mr_or_mrs, name='Friend'):
    print(f'Hi, {mr_or_mrs} {name}!')
    print('How are u?')
    return 'Foo'
foo = greeting(name='Sergey', mr_or_mrs='mr.')
print(foo)

def add(x, y):
    return x+y

foo = add(10, -33)
print(foo)

def function_name(param1, param2=None):
    result = param1 + param2
    return result  # Структура функции