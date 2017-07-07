class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Mammals(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.legs = 4

    def print_mammal(self):
        print("Я млекопитающее и у меня {} лапы".format(self.legs))


class Birds(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.legs = 2

    def print_bird(self):
        print("Я птица и у меня {} лапы".format(self.legs))


class Cow(Mammals):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.voice = 'МУУУУУУУУУ'


class Goat(Mammals):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.voice = 'Бе-е-е-е'


class Sheep(Mammals):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.voice = 'М-м-м-м-б-е-е-а-а'


class Pig(Mammals):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.voice = 'Хрю-хрю'


class Duck(Birds):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.voice = 'Кря-кря'


class Chicken(Birds):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.voice = 'Ко-ко-ко'


class Goose(Birds):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.voice = 'Га-га-га'


cow = Cow('Буренка', 5)
cow.print_mammal()
print('Я {}.'.format(cow.name), 'Мне {}.'.format(cow.age), 'Я говорю {}'.format(cow.voice))

goat = Goat('Коза', 2)
goat.print_mammal()
print('Я {}.'.format(goat.name), 'Мне {}.'.format(goat.age), 'Я говорю {}'.format(goat.voice))

duck = Duck('Дональд', 3)
duck.print_bird()
print('Я {}.'.format(duck.name), 'Мне {}.'.format(duck.age), 'Я говорю {}'.format(duck.voice))