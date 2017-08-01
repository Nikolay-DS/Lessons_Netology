from urllib.parse import urlencode

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.65'
APP_ID = ''
USER_ID = ''


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

token = ''
