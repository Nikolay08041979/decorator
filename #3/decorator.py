from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            call_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            func_name = old_function.__name__
            func_args = args
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(
                    f'Дата и время вызова функции:{call_time}, \n'
                    f'Имя функции: {func_name}, \n'
                    f'Аргументы, с которыми вызывалась функция: {func_args}, \n'
                    f'Возвращаемое значение: {result}\n')
        return new_function
    return __logger