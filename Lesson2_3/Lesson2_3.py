import chardet
import json


def file_encoding():
    filename = input('Введите название файла: ')
    with open('{}'.format(filename), 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print(result)
        s = data.decode(result['encoding'])
    json_acceptable_string = s.replace("'", "")
    travel_dict = json.loads(json_acceptable_string)
    working_dict = travel_dict['rss']['channel']['item']
    return working_dict


def create_dict_from_file(working_dict):
    new_dict = {}
    new_list = []
    for words in working_dict:
        new_dict['title'] = words['title']
        new_dict['description'] = words['description']
        new_list += new_dict.values()
    separated_words = str(new_list).split()
    get_cleaned_words = []
    for word in separated_words:
        if len(word.replace(',', '').replace('/', '').replace(':', '').replace('{\'__cdata', '').replace('\'',
                                                                                                         '')) >= 6:
            get_cleaned_words.append(word)
        else:
            continue
    get_cleaned_words = sorted(get_cleaned_words, key=len, reverse=True)
    return get_cleaned_words


def analysis(get_cleaned_words):
    dct = {}
    for i in get_cleaned_words:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return sorted(dct.items(), key=lambda x: x[1], reverse=True)[:10]
    

def print_top10_frequencies(word_frequencies):
    t = 1
    print('\n ТОП 10 СЛОВ: \n')
    print(word_frequencies)


def main():
    working_dict = file_encoding()
    get_cleaned_words = create_dict_from_file(working_dict)
    word_frequencies = analysis(get_cleaned_words)
    print_top10_frequencies(word_frequencies)

main()
    