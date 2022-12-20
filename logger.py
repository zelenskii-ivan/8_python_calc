# Модуль для записи резуьтатов вычислений
import csv

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('book.csv', 'a', encoding='utf-8') as book:
        book.write(f'{expr} | {result}\n')


def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    global book
    book = open('book.csv', 'r', encoding='utf-8')
    file_reader = csv.DictReader(book, delimiter= "|")
    return file_reader  