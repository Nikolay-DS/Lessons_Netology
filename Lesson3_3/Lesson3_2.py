import requests
import glob
import os.path

API_KEY = 'trnsl.1.1.20170627T164346Z.d63afd9e60412866.bfbdb111b490e64e1cb8454f78eb42a9b448638c'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def choose_language(to_lang):
    """
    Возможность выбора языка для перевода
    согласно API Yandex translate
    параметр можем вводить через input
    """
    trans_lang = to_lang
    return trans_lang


def get_translation(text):
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
        lang='{}'.format(choose_language('ru')),
    )

    response = requests.get(url=URL, params=params)
    return response


def read_and_write_translation():
    files = glob.glob(os.path.join('*.txt'))
    for file in files:
        # print('texts    ', file)
        with open(file, 'r') as f:
            text = f.read()
            resp = get_translation(text)
            with open('{}-{}.txt'.format(file.replace(".txt", ""), choose_language('ru')), 'w') as f:
                res_dict = resp.json()
                f.write(str(res_dict['text']))
                f.close()
        # print(str(res_dict['text']))


read_and_write_translation()