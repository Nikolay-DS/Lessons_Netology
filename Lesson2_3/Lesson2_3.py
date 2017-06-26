import chardet
import json


def file_encoding():
    with open('newsafr.json', 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print(result)
        s = data.decode(result['encoding'])

    json_acceptable_string = s.replace("'", "")
    travel_dict = json.loads(json_acceptable_string)
    working_dict = travel_dict['rss']['channel']['item']
    return working_dict


def create_dict_from_file():
    new_dict = {}
    new_list = []
    for words in file_encoding():
        new_dict['title'] = words['title']
        new_dict['description'] = words['description']
        new_list += new_dict.values()
    separated_words = str(new_list).split()
    final_word = []
    for word in separated_words:
        if len(word.replace(',', '').replace('/', '').replace(':', '').replace('{\'__cdata', '').replace('\'',
                                                                                                         '')) >= 6:
            final_word.append(word)
        else:
            continue
    final_word = sorted(final_word, key=len, reverse=True)
    return final_word


dct = {}


def analysis():
    for i in create_dict_from_file():
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct


def invert_dict_non_unique(d):
    newdict = {}
    for k, v in iter(d.items()):
        newdict.setdefault(v, []).append(k)
    return newdict


def top_ten():
    t = 1
    print('\n ТОП 10 СЛОВ: \n')
    for i in sorted(invert_dict_non_unique(analysis()), reverse=True):
        if t <= 10:
            t = 1 + t
            print("'{}':{}".format(i, invert_dict_non_unique(dct)[i]))
        else:
            break


top_ten()
