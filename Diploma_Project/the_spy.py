# -*- coding: utf-8 -*-

from main_functions import *
from pprint import pprint
import json
from termcolor import colored


VERSION = '5.65'
USER_ID = input('Введите ID пользователя: ')
TOKEN = ''  # TOKEN
pprint(get_friends(USER_ID, TOKEN))


def write_to_file(USER_ID, VERSION, TOKEN):
    user_group_id = get_groups_list(USER_ID, VERSION, TOKEN)
    user_group_id_full = get_groups_list_full(USER_ID, VERSION, TOKEN)
    super_final = sorted(set(user_group_id) - get_friends_groups(USER_ID, VERSION, TOKEN))
    output_list = []
    for x in super_final:
        for y in user_group_id_full:
            if x == y[0]:
                output_group = {'id': y[0], 'name': y[1], 'members_count': y[2]}
                output_list.append(output_group)
    js = json.dumps(output_list, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))
    with open('groups.json', 'w+', encoding="utf-8") as f:
        f.write(js)
        f.close()
    pprint(output_list)
    print(colored('groups.json successfully created', 'green'))


write_to_file(USER_ID, VERSION, TOKEN)
