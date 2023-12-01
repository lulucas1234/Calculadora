numero1 = 0
numero2 = 0
resultado = 0
operacao = ''

while True:

    numero1 = int(input('Digite um numero1:'))
    operacao = input('Digite a operação:')
    numero2 = int(input('Digite um numero2:'))

    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '/':
        resultado = numero1 / numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    else:
        resultado = 'Operação invalida'

    print(str (numero1) + '' + str(operacao) + '' + str(numero2) + '=' + str(resultado))