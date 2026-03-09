class Cat:
    def __init__(self, name, age, power, health=100, lives=9):
        self.name = name
        self.age = age
        self.power = power
        self.health = health
        self.lives = lives

    def meow(self):
        print(f'{self.name} говорит мяу!')
    
    def hit(self, other):  # удар лапой
        other.health -= self.power
        if other.is_dead():
            other.resurrect()
    
    def is_dead(self):
        return self.health <= 0
    
    def is_absolutely_dead(self):
        return (self.lives <= 0) or (self.lives == 0 and self.health <= 0)
    
    def _resurrect(self):
        if self.is_dead():
            if self.lives > 0:
                self.health = 100
                self.lives -= 1
            else:
                pass
                #print(f'{self.name} не может быть воскрешен. У него кончились жизни!')
    
                  
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
        
    def __lt__(self, other):      #less, than - менее чем
        return self.power < other.power
       



from random import choice
# dunder-методы(double under)
wins = dict()
wins['Мурка'] = 0
wins['Барсик'] = 0
wins['Валера'] = 0



for _ in range(1000):
    murka = Cat('Мурка', 5, 100)
    barsik = Cat('Барсик', 10, 95)
    maksik = Cat('Валера', 13, 28, 78, 12)


    our_cats = [murka, barsik, maksik]

    while len(our_cats) > 1:
        cat1 = choice(our_cats)
        cat2 = choice(our_cats)
        if cat1 != cat2:
            #print(f'{cat1.name} бьет {cat2.name}!')
            #print(f'{cat2.name} имеет {cat2.health} здоровья и {cat2.lives} жизней')
            cat1.hit(cat2)
            if cat2.is_absolutely_dead():
                #print(f'{cat2.name} выходит из игры в связи со смертью')
                our_cats.remove(cat2)

    wins[our_cats[0].name] += 1

print(wins)