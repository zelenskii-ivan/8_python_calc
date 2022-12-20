# Модуль для ввода/вывода информации
m = 0

def choose() -> str:
    """Выбор режима работы приложения"""
    print ('Выберите режим работы приложения(введите соответствующий номер):')
    print ('1) решение примера\n2) решение уравнений\n3) упрощение многочленов')
    print ('4) история вычислений\n')
    global m
    m = str(input())
    return m


def get_expr() -> str:
    """Запрашивает у пользователя задачу"""
    
    if m == '1':
        print ('Введите пример:\n')
        ex = str(input())
        return ex
    if m == '2':
        print ('Введите линейное уравнение:\n')
        ex = str(input())
        return ex
    if m == '3':
        print ('Введите многочлен, который нужно упростить:\n')
        ex = str(input())
        return ex
    # print ('Введите пример:\n')
    # ex = str(input())
    # return ex
    

def show_res(res: str):
    """Выводит результат"""
    print (f'Ответ: {res}\n')


def erorr_mode():
    """Выводит сообщение об ошибке выбора режима"""
    print('Некорректный ввод')


def show_history(history: str):
    """Выводит истроию оперций"""
    print()
    print('Журнал вычислений:\n')
    count = 0
    for row in history:
        print(f'{row["Пример"]} = {row["Решение"]}')
        count += 1
    print(f'Всего вычислений: {count}')