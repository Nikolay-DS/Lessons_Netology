# -*- coding: utf-8 -*-

import requests
from pprint import pprint
import time
import json

VERSION = '5.65'
USER_ID = ''
token = ''


def my_friends(VERSION):
    params = {
        'user_id': '',
        'v': VERSION,
        'extended': 1,
        'fields': 'bdate'
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()

print(my_friends(VERSION).keys())
r = my_friends(VERSION)['response']['items']
pprint(r)
print('was ', len(r))
for v in r:
    if 'deactivated' in v.keys():
        r.remove(v)
print('became ', len(r))
friends_id = [x['id'] for x in r]
print('became friends', len(friends_id))


def my_groups(token, VERSION):
    params = {
        'access_token': token,
        'user_id': '',
        'v': VERSION,
        'extended': 1,
        'fields': 'members_count'
    }
    response = requests.get('https://api.vk.com/method/groups.get', params)
    return response.json()

pprint(my_groups(token, VERSION))
rr = my_groups(token, VERSION)['response']['items']

print('groups was ', len(rr))
for v in rr:
    if 'deactivated' in v.keys():
        rr.remove(v)
my_list_groups = [x['id'] for x in rr]
my_list_groups_by_id = [[x['id'], x['name'], x['members_count']] for x in rr]
print('groups became {}'.format(len(my_list_groups)))
print(my_list_groups_by_id)


def get_friends_groups(friend_id, token, VERSION):
    params = {
        'access_token': token,
        'user_id': friend_id,
        'v': VERSION,
        'extended': 1,
        'fields': 'members_count',
    }
    response = requests.get('https://api.vk.com/method/groups.get', params)
    return response.json()
    

i = 1
group_friends_final = []
for friend_id in friends_id:
    if i % 3 == 0:
        time.sleep(1)
    print('...{} %...'.format(round(i*100/len(friends_id), 2)), '№{} friend id {}'.format(i, friend_id))
    i += 1
    try:
        group_friends = get_friends_groups(friend_id, token, VERSION)['response']['items']
    except Exception:
        print('error................................................{}'.format(friend_id))
    print(len(group_friends))
    for v in group_friends:
        if 'deactivated' in v.keys():
            group_friends.remove(v)
            group_friends_final.append(group_friends)
        else:
            group_friends_final.append(group_friends)


def xxx(group_friends_final):
    friends_group_list = []
    for x in group_friends_final:
        for y in x:
            if 'members_count' in y.keys():
                friends_group_list.append(y['id'])
    return friends_group_list

# pprint(set(sorted(xxx(group_friends_final))))
pprint('Общее число групп друзей {}'.format(len(set(sorted(xxx(group_friends_final))))))
pprint('Кол-во групп шпион {}'.format(len(sorted(set(my_list_groups) - set(sorted(xxx(group_friends_final)))))))
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
super_final = sorted(set(my_list_groups) - set(sorted(xxx(group_friends_final))))

output_list = []
for x in super_final:
    for y in my_list_groups_by_id:
        if x == y[0]:
            output_group = {'id': y[0], 'name': y[1], 'members_count': y[2]}
            output_list.append(output_group)
js = json.dumps(output_list, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))
with open('groups_demo.json', 'w+', encoding="utf-8") as f:
    f.write(js)
    f.close()
