from urllib.parse import urlencode

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.65'
APP_ID = '6093812'
USER_ID = '5478103'


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

token = 'd9d8dd80590773783918eef622069c6da7a8cd9debbdfce3400e5e186e436b6980152be981dc72590cfc9'
