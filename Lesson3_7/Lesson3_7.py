from urllib.parse import urlencode
import requests
import pprint

AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
APP_ID = '8706984f710041f7899556638efa1987'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))

"""
new metrik

Права:
Создание счётчиков, изменение параметров своих и доверенных счётчиков
Получение статистики, чтение параметров своих и доверенных счётчиков
ID: 8706984f710041f7899556638efa1987
Пароль: 0f177c2c5dff4b26851e566d6fd4f26c
Callback URL: https://oauth.yandex.ru/verification_code
TOKEN : AQAAAAAD5DaCAARocFMjT2ypSErWjmeODhXT2xk

"""

TOKEN = 'AQAAAAAD5DaCAARocFMjT2ypSErWjmeODhXT2xk'


class MetrikaBase:
    API_MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    API_STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/'
    token = None

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {0}'.format(self.token),
            'Content-Type': 'application/json'
        }


class YandexMetrika(MetrikaBase):

    def get_counters(self):
        headers = self.get_headers()
        r = requests.get(self.API_MANAGEMENT_URL + 'counters', headers=headers)
        return [
            Counter(self.token, counter['id']) for counter in r.json()['counters']
        ]


class Counter(MetrikaBase):

    def __init__(self, token, counter_id):
        self.counter_id = counter_id
        super().__init__(token)

    def get_visits(self):
        headers = self.get_headers()
        params = {
            'id': self.counter_id,
            'metrics': 'ym:s:visits'
        }
        r = requests.get(self.API_STAT_URL + 'data', params, headers=headers)
        return r.json()['data'][0]['metrics']

    def get_pageviews(self):
        headers = self.get_headers()
        params = {
            'id': self.counter_id,
            'metrics': 'ym:s:pageviews'
        }
        r = requests.get(self.API_STAT_URL + 'data', params, headers=headers)
        return r.json()['data'][0]['metrics']

    def get_users(self):
        headers = self.get_headers()
        params = {
            'id': self.counter_id,
            'metrics': 'ym:s:users'
        }
        r = requests.get(self.API_STAT_URL + 'data', params, headers=headers)
        return r.json()['data'][0]['metrics']


metrika = YandexMetrika(TOKEN)
print(metrika.get_counters())
counters = metrika.get_counters()
for counter in counters:
    print(counter.get_visits())
    print(counter.get_pageviews())
    print(counter.get_users())



