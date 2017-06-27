import json


def create_menu_from_file():
	with open('/Users/nicolas13/Lessons_Netology/Lesson2_2/Lesson2_2.json') as f:
		cook_book = json.load(f)
		return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_menu_from_file()
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
		        new_shop_list_item = dict(ingridient)
		        new_shop_list_item['quantity'] *= person_count
		        #print(new_shop_list_item)
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