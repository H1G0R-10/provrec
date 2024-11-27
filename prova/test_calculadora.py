from calculadora import Calculadora

# somar --------------

def somar(a, b):
        return a + b

def test_somar():
    assert somar(5, 5) == 10
    assert somar(10, 10) == 20
    assert somar(15, 15) == 30


def test_somar_negativo():
    assert somar(-5, -5) == -10
    assert somar(-10, -10) == -20
    assert somar(-15, -15) == -30  

# subtrair --------------
def subtrair(a, b):
        return a - b

def test_subtrair():
    assert subtrair(10, 5) == 5
    assert subtrair(40, 20) == 20
    assert subtrair(50, 25) == 25


def test_subtrair_negativo():
    assert subtrair(-5, -5) == 0
    assert subtrair(-15, -10) == -5 
    assert subtrair(-50, -25) == -25 



# multiplicar --------------
def multiplicar(a, b):
        return a * b

def test_multiplicar():
    assert multiplicar(2, 15) == 30
    assert multiplicar(1, 10) == 10
    assert multiplicar(5, 2) == 10


def test_multiplicar_negativo():
    assert multiplicar(-5, -5) == 25
    assert multiplicar(-50, -50) == 2500 
    assert multiplicar(-10, -10) == 100 



# dividir --------------
def dividir(a, b):
        return a / b

def test_dividir():
    assert dividir(50, 2) == 25
    assert dividir(100, 2) == 50
    assert dividir(200, 2) == 100


def test_dividir_negativo():
    assert dividir(-20, -2) == 10
    assert dividir(-100, -5) == 20  
    assert dividir(-1000, -10) == 100  




             


        