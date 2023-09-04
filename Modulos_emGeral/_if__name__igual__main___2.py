def soma(x: float, y: float) -> str:
    sum_ = x + y
    return f'{sum_:.2f}'


# usamos o if __name__ == '__main__':
# para fazer teste somente se executar o arquivo __main__, então quando importa-
# mos, a linha de códigos não será executada

if __name__ == '__main__':
    print(soma(20, 30))
    print(soma(20, 50))
    print(soma(70, 50))
    print(soma(70, 50.78))
    print(soma(70.456, 50.7))
    print(soma(70.456, 50))
    print(soma(70.456, 50.0022200000000000000000002))