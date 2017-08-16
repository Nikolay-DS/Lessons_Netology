import requests
import time
from termcolor import colored

API = 'https://api.vk.com/method/'
TOO_MANY_REQUEST = 6


def do_request(url, params):
    while True:
        response = requests.get(url, params)
        print(colored('status code is [{}]'.format(response.status_code), 'yellow'))
        json_resp = response.json()
        if 'response' in json_resp:
            print(colored('done', 'green'))
            return json_resp
        elif json_resp['error']['error_code'] == TOO_MANY_REQUEST:
            print(colored(json_resp['error']['error_msg'], 'red'))
            print(colored('Please, waiting for 1 second', 'yellow'))
            time.sleep(1)
            print(colored('Retrying...', 'blue'))
            continue
        else:
            print(colored(json_resp['error']['error_msg'], 'red'))
            return json_resp


def get_friends(user_id, version):
    params = {
        'user_id': user_id,
        'v': version,
        'extended': 1,
        'fields': 'bdate'
    }
    response = do_request(API + 'friends.get', params)
    return response
    

def get_groups(user_id, version, token):
    params = {
        'access_token': token,
        'user_id': user_id,
        'v': version,
        'extended': 1,
        'fields': 'members_count',
    }
    response = do_request(API + 'groups.get', params)
    return response


def get_friends_id_list(user_id, version):
    resp = get_friends(user_id, version)['response']['items']
    try:
        friends_id = [x['id'] for x in resp]
        print('№ of friends', len(friends_id))
        return friends_id
    except Exception as e:
        print(e)


def get_groups_list(user_id, version, token):
    resp = get_groups(user_id, version, token)['response']['items']
    my_list_groups = [x['id'] for x in resp]
    print('№ of groups {}'.format(len(my_list_groups)))
    return my_list_groups
    

def get_groups_list_full(user_id, version, token):
    resp = get_groups(user_id, version, token)['response']['items']
    my_list_groups_by_id = [[x['id'], x['name'], x['members_count']] for x in resp]
    return my_list_groups_by_id


def get_friends_groups(user_id, version, token):
    friends_id = get_friends_id_list(user_id, token)
    group_friends_final = []
    for i, friend_id in enumerate(friends_id):
        print('...{} %...'.format(round((i + 1) * 100 / len(friends_id), 2)),
              '№{} friend id {}'.format((i + 1), friend_id))
        try:
            group_friends = get_groups(friend_id, version, token)['response']['items']
            print('{} groups for user id {}'.format(len(group_friends), friend_id))
            print('------------------------------------------------------------------------------')
        except Exception as e:
            print('------------------------------------------------------------------------------')
        for v in group_friends:
            if 'deactivated' not in v:
                group_friends_final.append(v['id'])
    friends_group_list = [x for x in group_friends_final]
    return set(sorted(friends_group_list))
