class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Mammals(Animal):
    legs = 4
            

    def print_mammal(self):
        print("Я млекопитающее и у меня {} лапы".format(self.legs))


class Birds(Animal):
    legs = 2


    def print_bird(self):
        print("Я птица и у меня {} лапы".format(self.legs))


class Cow(Mammals):
    voice = 'МУУУУУУУУУ'


class Goat(Mammals):
    voice = 'Бе-е-е-е'


class Sheep(Mammals):
    voice = 'М-м-м-м-б-е-е-а-а'


class Pig(Mammals):
    voice = 'Хрю-хрю'
    

class Duck(Birds):
    voice = 'Кря-кря'


class Chicken(Birds):
    voice = 'Ко-ко-ко'


class Goose(Birds):
    voice = 'Га-га-га'
    

cow = Cow('Буренка', 5)
cow.print_mammal()
print('Меня зовут {}.'.format(cow.name), 'Мне {}.'.format(cow.age), cow.voice)

goat = Goat('Коза', 2)
goat.print_mammal()
print('Я {}.'.format(goat.name), 'Мне {}.'.format(goat.age), 'Я говорю {}'.format(goat.voice))

duck = Duck('Дональд', 3)
duck.print_bird()
print('Я {}.'.format(duck.name), 'Мне {}.'.format(duck.age), 'Я говорю {}'.format(duck.voice))