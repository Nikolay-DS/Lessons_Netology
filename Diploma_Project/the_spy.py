# -*- coding: utf-8 -*-


from main_functions import get_friends, get_friends_groups
from main_functions import get_groups_list_full
from pprint import pprint
import json
from termcolor import colored


VERSION = '5.65'
USER_ID = input('Введите ID пользователя: ')
TOKEN = ''  # TOKEN
pprint(get_friends(USER_ID, TOKEN))


def write_to_file(user_id, version, token):
    user_group_id_full = get_groups_list_full(user_id, version, token)
    user_group_id = [x[0] for x in user_group_id_full]
    super_final = sorted(set(user_group_id) - get_friends_groups(user_id, version, token))
    output_list = []
    for x in super_final:
        for y in user_group_id_full:
            if x == y[0]:
                output_group = {'id': y[0], 'name': y[1], 'members_count': y[2]}
                output_list.append(output_group)
    js = json.dumps(output_list, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))
    with open('groups.json', 'w+', encoding="utf-8") as f:
        f.write(js)
    pprint(output_list)
    print(colored('groups.json successfully created', 'green'))


if __name__ == '__main__':
    write_to_file(USER_ID, VERSION, TOKEN)
