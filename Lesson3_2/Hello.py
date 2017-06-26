from collections import OrderedDict
import requests


d = OrderedDict([
    ('hello', 'world'),
    ('another', 'hello')
])

rifle = requests.get('https://yandex.ru')

print(d.keys())
print(rifle.text)
