def create_menu_from_file():
    with open('Lesson2_1.txt', 'r') as f:
        cook_book = {}
        for line in f:
            ingrid_string_list = []
            dish = line.strip()
            quantity_of_ingrid = f.readline().strip()
            ingrid_from_file = f.readline()
            while ingrid_from_file.strip():
                ingrid = ingrid_from_file.rstrip()
                ingrid_string = ingrid.split(' | ')
                ingrid_string_list.append({'ingridient_name': ingrid_string[0],
                                           'quantity': int(ingrid_string[1]), 'measure': ingrid_string[2]})
                cook_book[dish] = ingrid_string_list
                ingrid_from_file = f.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_menu_from_file()
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))

def create_shop_list():
    person_count = int(input('введите количество человек: '))
    dishes = input('введите блюда (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()