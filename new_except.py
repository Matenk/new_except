class InvalidDataException(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info

class ProcessingException(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info
def func(name, age, hobby, num1, num2):
        if age < 18:
            raise InvalidDataException('Вход запрещен', {'age' : age})
        if num2 == 0:
            raise ProcessingException('Что-то не так', 'на 0 нельзя')
        return name, age, hobby, num1 / num2


def func1():
    result_func = func('Serge', 18, 'Python', 10, 2)
    return result_func

try:
    total = func1()
    print(total)
except InvalidDataException as e:
        print('Ты ещё слишком молод, но сегодня ты можешь войти.', e.info)
except ProcessingException as x:
        print('Мы не смогли поделить, но продолжаем пробовать.', x.info)



