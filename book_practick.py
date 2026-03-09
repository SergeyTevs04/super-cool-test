# # Кортежи 

# # marx_tuple = ('Groucho', 'Chiko', 'Harpo')
# # a, b, c = marx_tuple
# # print(c)

# # password = 'swordfish'
# # icecream = 'tuttifrutti'
# # password, icecream = icecream, password
# # print(icecream)

# # # marx_tuple = ['Groucho', 'Chiko', 'Harpo']
# # print(('Groucho', 'Chiko', 'Harpo') * 3)

# # a = (7, 2, )
# # b = (7, 2, 9)
# # print(a == b)

# # words = ('fresh', 'out', 'of', 'ideas')
# # for word in words:
# #     print(word)

# # t1 = ('fee', 'fie', 'foe')
# # t2 = ('flop',)
# # print(id(t1))
# # t1 += t2
# # print(id(t1))
# # print(t1)

# # Списки 

# # empty_list = []
# # weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# # big_birds = ['emu', 'octrich', 'cassowary']
# # leap_years = [2000, 2004, 2008]
# # randomness = ['Punxsatawney', {'groundhog': 'Phil'}, 'Feb. 2']

# # another_empty_list = list()
# # print(another_empty_list)

# # print(list('cat'))

# # a_tuple = ('ready', 'fair', 'aim')
# # print(list(a_tuple))

# # talk_like_a_pirate_day = '9/19/2019'
# # print(talk_like_a_pirate_day.split('/'))

# # split_me = 'a/b//c/d///e'
# # print(split_me.split('/'))

# marxes = ['Groucho', 'Chiko', 'Harpo']
# # marxes.reverse()
# print(marxes[-6:-4])

# marxes.append('Zeppo')
# print(marxes)

# # marxes.insert(10, 'Gummo')
# print(marxes)

# print(['blah'] * 3)

# others = ['Gummo', 'Karl']
# # marxes.extend(others)
# marxes += others
# print(marxes)

# # marxes[2] = 'Wanda'
# print(marxes)

# numbers = [1, 2, 3, 4]
# # numbers[1:3] = [8, 9]
# # numbers[1:3] = [8, 9, 10]
# # numbers[1:3] = []
# # numbers[1:3] = (98, 99, 100)
# numbers[1:3] = 'wat?'
# print(numbers)

# del marxes[-1]
# del marxes[1]
# print(marxes)

# cheeses = ['brie', 'gjetost', 'havarti']
# for cheese in cheeses:
#     if cheese.startswith('x'):
#         print('I won\'t eat anything that starts with "x"')
#         break
#     else:
#         print(cheese)
# else:
#     print('Didn\'t find anything that started with "x"')

# cheeses = []
# for cheese in cheeses:
#     print('This shop has some lovely', cheese)
#     break
# else:
#     print('This is not much of a cheese shop, is it?')

# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['cofee', 'tea', 'beer']
# desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#     print(day, ': drink', drink, 'eat', fruit, 'enjoy', dessert)

# english = 'Monday', 'Tuesday', 'Wednesday'
# french = 'Lundi', 'Mardi', 'Mercredi'
# print(dict(zip(english, french)))

# number_list = []
# for number in range(1, 6):
#     number_list.append(number)
# print(number_list)

# number_list = list(range(1, 6))
# print(number_list)

# number_list = [number-1 for number in range(1, 6)]
# print(number_list)

# a_list = [number for number in range(1, 6) if number % 2 == 0]
# print(a_list)

# a_list = []
# for number in range(1, 6):
#     if number % 2 == 0:
#         a_list.append(number)
# print(a_list)

# rows = range(1, 4)
# cols = range(1, 3)
# cells = [(col,row) for col in cols for row in rows]
# for row, col in cells:
#     print (row, col)

# small_birds = ['hummingbird', 'finch']
# extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
# carol_birds = [3, 'French hens', 2, 'turtledoves']
# all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

# print(all_birds[1][1])

# Упражнения 
# 7.1
# yers_list = [2004, 2005, 2006, 2007, 2008, 2009]
# 7.2
# print(yers_list[3])
# 7.3
# print(yers_list[-1])
# 7.4
# things = ['mozzarella', 'cinderella', 'salmonela']
# print(things[2].capitalize())
# print(things[2])

# things[0] = things[0].upper()
# print(things)

# del things[1]
# print(things)

# 7.9
# surprise = ['Groucho', 'Chiko', 'Harpo']
# surprise[2] = surprise[2].lower() # ?
# print(surprise.insert())

# 7.10
# even = [x for x in range(10) if x % 2 == 0]
# print(even)

# 7.11
# start1 = ['fee', 'fie', 'foe']
# rhymes = [
#     ('flop', 'get a mop'),
#     ('fope', 'turn the rope'),
#     ('fa', 'get your ma'),
#     ('fudge', 'call the judge'),
#     ('fat', 'pet the cat'),
#     ('fog', 'wolk the dog'),
#     ('fun', 'say we\'re done')
#     ]
# start2 = 'Someone better'

# start1_caps = ' '.join([word.capitalize() + '!' for word in start1])
# for first, second in rhymes:
#     print(f'{start1_caps} {first.capitalize()}!')
#     print(f'{start2} {second}.')

# accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
# for card, contents in accusation.items():
#     print('Card', card, 'has the contents', contents)

# word = 'letters'
# letter_counts = {letter: word.count(letter) for letter in set(word)}
# print(letter_counts)

# vowels = 'aeioe'
# word = 'onomatopoeia'
# vowel_counts = {letter: word.count(letter) for letter in word if letter in vowels}
# print(vowel_counts)
# a_set = {number for number in range(1,6) if number % 3 == 1}
# print(a_set)

# marxes = ['Grouncho', 'Chiko', 'Harpo']
# pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
# stooges = ['Moe', 'Curly', 'Larry']

# dict_of_lists = {'Marxes': marxes,
#                  'Pythons': pythons,
#                  'Stooges' :stooges
# }
# print(dict_of_lists)

# houses = {
#     (44.79, -93.14, 285): 'My House',
#     (38.89, -77.03, 13): 'The White House'
# }
# print(houses)

# Упражнения 
# 8.6
# life = {
#     'animals': {
#         'cats': [
#             'Henri', 'Grumpy', 'Lucy'
#             ],
#         'octopi':{},
#         'emus': {}
#         },
#     'plants': {},
#     'other': {}
#     }


# # # 8.7
# print(life.keys())

# # # 8.8
# print(life['animals'].keys())

# # # 8.9
# print(life['animals']['cats'])

# # 8.10
# squares = {k: k**2 for k in range(10)}
# print(squares)

# # 8.11
# odd = {number for number in range(10) if not number % 2 == 0} # Или можно было if number % 2 == 1
# print(odd)


# # 8.12 ?
# for x in range(10):
#     print('got', x)

# # 8.13
# a = ('optimist', 'pessimist', 'troll')
# b = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
# print(dict(zip(a,b)))

# # 8.14
# titles = ['Creature of Habit', 'Crewel Fate', 'Sharks on a Plane']
# plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
# movies = dict(zip(titles, plots))
# print(movies)

# Глава 9

# def do_nothing():
#     pass
# print(do_nothing())

# def make_a_sound():
#     print('quack')
# make_a_sound()

# def agree():
#     return True
# if agree():
#     print('Splendid')
# else:
#     print('That was unexpected.')

# def echo(anything):
#     return print(anything + ' ' + anything)
# echo('Ramplestilstkin')

# def commentary(color):
#     if color == 'red':
#         return 'It\'s a tomato!'
#     elif color == 'green':
#         return 'It\'s a green pepper'
#     elif color == 'bee purple':
#         return 'I don\'t know what it is, but only bees can see it.'
#     else:
#         return 'I\'ve never heard of the color ' + color + '.'

# comment = commentary('blue')
# print(comment)

# thing = None
# if thing is None:
#     print('It\'s nothing')
# else:
#     print('It\'s something')

# def whatis(thing):
#     if thing is None:
#         print(thing, 'is None')
#     elif thing:
#         print(thing, 'is True')
#     else:
#         print(thing, 'is False')
# whatis(0.0)

# def menu(wine, entree, dessert='pudding'):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}
# print(menu('chardonnay', 'chiken', 'fdffdf'))

# def buggy(arg, result=[]):
#     result.append(arg)
#     print(result)
# buggy('a')
# buggy('b')

# def works(arg):
#     result = []
#     result.append(arg)
#     return result
# print(works('a'))
# print(works('b'))





