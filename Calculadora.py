cont = 0
while cont < 10:
    menu = input('''Calculadora
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    ''')

    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    if menu == '1':
        soma = n1 + n2
        print(soma)

    elif menu == '2':
        sub = n1 - n2
        print(sub)
    elif menu == '3':
        mult = n1 * n2
        print(mult)
    elif menu == '4':
        div = n1 / n2
        print(div)
