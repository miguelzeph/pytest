from math_functions import fib, next_collatz_element


def test_fib_basic_initial():
    assert fib(0) == 0
    assert fib(1) == 1


def test_fib_2():
    assert fib(2) == 1


def test_fib_3():
    assert fib(3) == 2


def test_collatz_1():
    assert next_collatz_element(1) == 4


def test_collatz_2():
    assert next_collatz_element(2) == 1

# Vou errar neste por querer, ele mostra a resposta no campo vermelho
# Exemplo, eu não sei quando vai dar next_collatz_element(4)... ele mostra que é 2
# Nosso exemplo abaixo vai dar FAILED pois deveria ser 2 no lugar do 1.
def test_collatz_3():
    assert next_collatz_element(4) == 1
