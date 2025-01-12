class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    @staticmethod
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number not in range(1000000, 10000000):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        else:
            return True

    @staticmethod
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:

    first = Car('Model1', 1000000, 'f123dj')

except IncorrectVinNumber as exc:

    print(exc.message)

except IncorrectCarNumbers as exc:

    print(exc.message)

else:

    print(f'{first.model} успешно создан')

try:

    second = Car('Model2', 300, 'т001тр')

except IncorrectVinNumber as exc:

    print(exc.message)

except IncorrectCarNumbers as exc:

    print(exc.message)

else:

    print(f'{second.model} успешно создан')

try:

    third = Car('Model3', 2020202, 'нет номера')

except IncorrectVinNumber as exc:

    print(exc.message)

except IncorrectCarNumbers as exc:

    print(exc.message)

else:

    print(f'{third.model} успешно создан')
