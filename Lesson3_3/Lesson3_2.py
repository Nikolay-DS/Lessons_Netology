import requests
import glob
import os.path

API_KEY = 'trnsl.1.1.20170713T222240Z.c3c095681a918beb.85b99b091d01a616dc5ff39888a2d258af0ae3f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def get_translation(text, lang_input):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
key=<API-ключ>
 & text=<переводимый текст>
 & lang=<направление перевода>
 & [format=<формат текста>]
 & [options=<опции перевода>]
 & [callback=<имя callback-функции>]
    """
    params = dict(
        key=API_KEY,
        text=text,
        lang=lang_input,
    )

    response = requests.get(url=URL, params=params)
    return response


def read_and_write_translation():
    files = glob.glob(os.path.join('*.txt'))
    for file in files:
        with open(file, 'r') as f:
            text = f.read()
            resp = get_translation(text, lang_input='ru') # можно lang_input = input('Insert the translation\'s lang: ')
            with open('{}-translate.txt'.format(file.replace(".txt", "")), 'w') as f:
                res_dict = resp.json()
                f.write(str(res_dict['text']))
                f.close()

read_and_write_translation()