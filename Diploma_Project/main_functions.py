import requests
import time
from termcolor import colored


def get_friends(USER_ID, VERSION):
    params = {
        'user_id': USER_ID,
        'v': VERSION,
        'extended': 1,
        'fields': 'bdate'
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()
    

def get_groups(USER_ID, VERSION, TOKEN):
    params = {
        'access_token': TOKEN,
        'user_id': USER_ID,
        'v': VERSION,
        'extended': 1,
        'fields': 'members_count',
    }
    response = requests.get('https://api.vk.com/method/groups.get', params)
    return response.json()


def get_friends_id_list(USER_ID, VERSION):
    try:
        resp = get_friends(USER_ID, VERSION)['response']['items']
    except Exception as e:
        print(e)
        try:
            resp = get_friends(USER_ID, VERSION)['response']
        except Exception as e:
            print(e)
    try:
        friends_id = [x['id'] for x in resp]
    except Exception as e:
        print(e)
        try:
            friends_id = [x['uid'] for x in resp]
        except Exception as e:
            print(e)
    print('№ of friends', len(friends_id))
    return friends_id


def get_groups_list(USER_ID, VERSION, TOKEN):
    resp = get_groups(USER_ID, VERSION, TOKEN)['response']['items']
    my_list_groups = [x['id'] for x in resp]
    print('№ of groups {}'.format(len(my_list_groups)))
    return my_list_groups
    

def get_groups_list_full(USER_ID, VERSION, TOKEN):
    resp = get_groups(USER_ID, VERSION, TOKEN)['response']['items']
    my_list_groups_by_id = [[x['id'], x['name'], x['members_count']] for x in resp]
    return my_list_groups_by_id


def get_friends_groups(USER_ID, VERSION, TOKEN):
    friends_id = get_friends_id_list(USER_ID, TOKEN)
    group_friends_final = []
    error_catch = []
    friends_group_list = []
    for i, friend_id in enumerate(friends_id):
        if (i+1) % 3 == 0:
            time.sleep(1)
        print('...{} %...'.format(round((i+1)*100/len(friends_id), 2)),
         '№{} friend id {}'.format((i+1), friend_id))
        try:
            group_friends = get_groups(friend_id, VERSION, TOKEN)['response']['items']
            print('{} groups for user id {}'.format(len(group_friends), friend_id))
            print('------------------------------------------------------------------------------')
        except Exception:
            error_message = get_groups(friend_id, VERSION, TOKEN)['error']['error_msg']
            print(colored('error for user id {}. The reason: {}'.format(friend_id, error_message), 'red'))
            print('------------------------------------------------------------------------------')
            error_catch.append(friend_id)
        for v in group_friends:
            if 'deactivated' in v.keys():
                group_friends.remove(v)
                group_friends_final.append(group_friends)
            else:
                group_friends_final.append(group_friends)
    for x in group_friends_final:
        for y in x:
            friends_group_list.append(y['id'])
    print(colored('Quantity of errors: {}'.format(len(error_catch)), 'red'))
    return set(sorted(friends_group_list))
