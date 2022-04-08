from py_exchangeratesapi import Api

class APIException(Exception):
    pass

api = Api('4b13acedddbf5788a50e4ec36ecf1093')

exchanges = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}

class Convertor:
    @staticmethod
    def get_price(list=[]):
        amount = list[0]
        base = list[1]
        sym = list[2]



        try:
            base_key = exchanges[base.lower()]
            print(base_key)
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        if base_key != 'EUR':
            raise APIException(f"В бесплатной версии бота базовая валюта:Евро не меняется!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        price = round(api.convert(amount, base_key, sym_key), 3)
        message = f"Цена {amount} {base} в {sym} : {price}"
        return message

# print(api.convert(10.0, "EUR", 'USD'))
# c = Convertor()
# print(c.get_price(['10', 'доллар', 'евро']))