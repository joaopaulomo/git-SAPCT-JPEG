def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def potencia(a, pot):
    return a ** pot

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"
