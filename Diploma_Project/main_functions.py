import requests
import time
from termcolor import colored

API = 'https://api.vk.com/method/'


def do_request(foo):
    try:
        foo.raise_for_status()
        return foo
    except requests.exceptions.RequestException as e:
        print(e)
        time.sleep(1)
        print('')
        foo.raise_for_status()
        return foo
    except Exception as e:
        print('We are the------------{}'.format(e))


def get_friends(user_id, version):
    params = {
        'user_id': user_id,
        'v': version,
        'extended': 1,
        'fields': 'bdate'
    }
    response = requests.get(API + 'friends.get', params)
    do_request(response)
    return response.json()
    

def get_groups(user_id, version, token):
    params = {
        'access_token': token,
        'user_id': user_id,
        'v': version,
        'extended': 1,
        'fields': 'members_count',
    }
    response = requests.get(API + 'groups.get', params)
    do_request(response)
    return response.json()


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
        print('...{} %...'.format(round((i+1)*100/len(friends_id), 2)),
              '№{} friend id {}'.format((i+1), friend_id))
        try:
            group_friends = get_groups(friend_id, version, token)['response']['items']
            print('{} groups for user id {}'.format(len(group_friends), friend_id))
            print('------------------------------------------------------------------------------')
        except Exception as e:
            print('Error in {}'.format(e))
            try:
                error_message = get_groups(friend_id, version, token)
                print(colored(error_message['error']['error_msg'], 'red'))
                if error_message['error']['error_msg'] == 'Too many requests per second':
                    time.sleep(1)
                    print('...........')
                    try:
                        group_friends = get_groups(friend_id, version, token)['response']['items']
                        print('2nd trying {} groups for user id {}'.format(len(group_friends), friend_id))
                    except Exception as e:
                        print('Error in {}'.format(e))
            except Exception as e:
                print('Another Error is {}'.format(e))
            print('------------------------------------------------------------------------------')
        for v in group_friends:
            if 'deactivated' not in v.keys():
                group_friends_final.append(v['id'])
    friends_group_list = [x for x in group_friends_final]
    return set(sorted(friends_group_list))
