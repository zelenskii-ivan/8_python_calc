# Модуль для выполнения опреаций
import sympy
from sympy.solvers import solve
from sympy import Symbol
def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    expr = sympy.simplify(expr)
    return expr


def solve_eq(expr: str) -> str:                    # x**3 - 8 = 0 -> "2"
                                                    # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    x = Symbol('x')
    try:
        ans = sympy.solve(expr, x)
        return ans
    except ValueError:
        print('Некорректный ввод. Введите уравнение без знака')
    


def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен""" 
    x = Symbol('x') 
    expr = sympy.simplify(expr)
    return expr