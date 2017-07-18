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
    species = 'Корова'
    
    
    def print_cow_message(self):
        print('Меня зовут {}.'.format(self.name), 'Я - {}.'.format(self.species), 'Мне {}.'.format(self.age), '{}'.format(self.voice))


class Goat(Mammals):
    voice = 'Бе-е-е-е'
    species = 'Коза'
    
    
    def print_cow_message(self):
        print('Меня зовут {}.'.format(self.name), 'Я - {}.'.format(self.species), 'Мне {}.'.format(self.age), '{}'.format(self.voice))


class Sheep(Mammals):
    voice = 'М-м-м-м-б-е-е-а-а'
    species = 'Овца'
    
    
    def print_cow_message(self):
        print('Меня зовут {}.'.format(self.name), 'Я - {}.'.format(self.species), 'Мне {}.'.format(self.age), '{}'.format(self.voice))


class Pig(Mammals):
    voice = 'Хрю-хрю'
    species = 'Свинья'
    
    
    def print_cow_message(self):
        print('Меня зовут {}.'.format(self.name), 'Я - {}.'.format(self.species), 'Мне {}.'.format(self.age), '{}'.format(self.voice))

class Duck(Birds):
    voice = 'Кря-кря'
    species = 'Утка'
    
    
    def print_cow_message(self):
        print('Меня зовут {}.'.format(self.name), 'Я - {}.'.format(self.species), 'Мне {}.'.format(self.age), '{}'.format(self.voice))

class Chicken(Birds):
    voice = 'Ко-ко-ко'
    species = 'Курица'
    
    
    def print_cow_message(self):
        print('Меня зовут {}.'.format(self.name), 'Я - {}.'.format(self.species), 'Мне {}.'.format(self.age), '{}'.format(self.voice))

class Goose(Birds):
    voice = 'Га-га-га'
    species = 'Гусь'
    
    
    def print_cow_message(self):
        print('Меня зовут {}.'.format(self.name), 'Я - {}.'.format(self.species), 'Мне {}.'.format(self.age), '{}'.format(self.voice))   


cow = Cow('Буренка', 5)
cow.print_cow_message()
cow.print_mammal()
print('Меня зовут {}.'.format(cow.name), 'Мне {}.'.format(cow.age), cow.voice)

goat = Goat('Коза', 2)
goat.print_mammal()
print('Я {}.'.format(goat.name), 'Мне {}.'.format(goat.age), 'Я говорю {}'.format(goat.voice))

duck = Duck('Дональд', 3)
duck.print_bird()
print('Я {}.'.format(duck.name), 'Мне {}.'.format(duck.age), 'Я говорю {}'.format(duck.voice))