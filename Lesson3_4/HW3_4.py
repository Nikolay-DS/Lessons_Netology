from urllib.parse import urlencode
import requests

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.65'
APP_ID = 6093812


def auth_data_check(APP_ID, VERSION):
    auth_data = {
        'client_id': APP_ID,
        'display': 'mobile',
        'response_type': 'token',
        'scope': 'friends, status, video',
        'v': VERSION,
    }
    return print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))


auth_data_check(APP_ID, VERSION)
token = ''  # из-за открытого доступа токен удален


def my_friends_response(token, VERSION):
    params = {
        'access_token': token,
        'v': VERSION,
        'fields': 'nickname',
        'count': '3',
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()


def friends_of_my_friends_resp(id_request, token):
    params = {
        'access_token': token,
        'v': VERSION,
        'user_id': id_request,
        'fields': 'nickname',
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    resp = response.json()
    return resp


def my_friends_list():
    res_dict = my_friends_response(token, VERSION)
    my_friends = res_dict['response']
    friends_list = []
    id_requests = []
    for items in my_friends['items']:
        if 'deactivated' not in items.keys():
            friends_list.append(str([items['id'], items['first_name'], items['last_name']]))
            id_requests.append(items['id'])
    return friends_list, id_requests


def my_friends_friends(id_requests):
    friends_of_friends = []
    for id_request in id_requests:
        res_fof_dict = friends_of_my_friends_resp(str(id_request), token)
        if 'error' not in res_fof_dict.keys():
            my_fof_list = res_fof_dict['response']
            for items_fof in my_fof_list['items']:
                if 'deactivated' not in items_fof.keys():
                    friends_of_friends.append(str([items_fof['id'], items_fof['first_name'], items_fof['last_name']]))
    return friends_of_friends


def matual_friends(friends_list, friends_of_friends):
    matual_friends_list = sorted(set(sorted(friends_list + friends_of_friends)))
    return matual_friends_list


print('Cписок моих друзей:\n', my_friends_list(), '\n')
print('Cписок друзей моих друзей:\n', my_friends_friends(my_friends_list()[1]), '\n')
print('Пересечение друзей друзей:\n', matual_friends(my_friends_list()[0], my_friends_friends(my_friends_list()[1])))