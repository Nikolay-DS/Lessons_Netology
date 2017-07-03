import osa


def user_input_route():
    input_user = input("Введите путь к файлу: ")
    return input_user


def data_from_file(input_user):
    with open(str(input_user), 'r') as f:
        data_list = []
        i = 0
        for line in f:
            data_list.append(line.strip())
            data_list[i] = data_list[i].split(" ")
            i += 1
        if len(data_list[0]) == 2:
            return print("Средняя температура по Цельсию: {}".format(average_temperature(data_list)))
        elif len(data_list[0]) == 3 and len(data_list[0][2]) == 3:
            return print("Сумма перелета: {}".format(count_of_flyes(data_list)), "Рублей")
        else:
            return print("Cуммарное расстояние пути в километрах с точностью до сотых: {}".format(whole_trip_metrics(data_list)),
          "км")


def average_temperature(data_list):
    average = 0.0
    for num in data_list:
        average += int(num[0])
    average = average / len(data_list)

    return round(temperature_in_celsius(average), 2)


def temperature_in_celsius(average):
    URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'

    client = osa.client.Client(URL)

    response = client.service.ConvertTemp(Temperature=average,
                                          FromUnit='degreeFahrenheit',
                                          ToUnit='degreeCelsius')
    return response


def count_of_flyes(data_list):
    counter = 0.0
    for b, c in enumerate(data_list):
        currency_fly = str(c[2])
        amount_fly = float(str(c[1]).replace(',', ""))
        counter += int(convert_currency(currency_fly, amount_fly))
    return counter


def convert_currency(currency_fly, amount_fly):
    URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'

    client2 = osa.client.Client(URL)

    response2 = client2.service.ConvertToNum(fromCurrency=str(currency_fly),
                                             toCurrency='RUB',
                                             amount=float(amount_fly),
                                             rounding=False)
    return round(response2, 0)


def whole_trip_metrics(data_list):
    counter = 0.00
    for b, c in enumerate(data_list):
        counter += float(str(c[1]).replace(',', ""))
    return round(convert_metrics(counter), 2)


def convert_metrics(counter):
    URL = 'http://www.webservicex.net/length.asmx?WSDL'

    client3 = osa.client.Client(URL)

    response3 = client3.service.ChangeLengthUnit(LengthValue=float(counter),
                                                 fromLengthUnit='Miles',
                                                 toLengthUnit='Kilometers')
    return response3


data_from_file(user_input_route())