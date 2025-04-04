print('Verificação de idade!\n')

idade = int(input('Digite aqui sua idade\n'))

if idade >= 18:
    print('Você pode comprar goró!')
else: 
    print('Você não tem idade para compra de goró!')


print('Retorna o maior número digitado!')

n1 = int(input('Digite aqui o primeiro número: '))
n2 = int(input('Digite aqui o segundo número: '))
n3 = int(input('Digite aqui o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O número maior é: {n1} (primeiro número)')
elif n2 > n1 and n2 > n3:
    print(f'O número maior é: {n2} (segundo número)')
elif n3 > n1 and n3 > n2:
    print(f'O número maior é: {n3} (terceiro número)')
else:
    print('Existe um empate entre os maiores números.')


print('Calcula valores\n')

print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')

opcao_escolhida = int(input('Digite aqui a opção escolhida: \n'))

def Soma():
    som1 = int(input('Digite aqui o primeiro número que deseja somar: '))
    som2 = int(input('Digite aqui o segundo número que deseja somar: '))
    soma = som1 + som2
    print(f'O resultado dessa operação é: {soma}')

def Subtracao():
    sub1 = int(input('Digite aqui o primeiro valor: '))
    sub2 = int(input('Digite aqui o segundo valor: '))
    subtracao = sub1 - sub2
    print(f'O resultado dessa operação é: {subtracao}')

def Multiplica():
    mul1 = int(input('Digite aqui o primeiro valor: '))
    mul2 = int(input('Digite aqui o segundo valor: '))
    multiplica = mul1 * mul2
    print(f'O resultado dessa operação é: {multiplica}')

def Divide():
    div1 = int(input('Digite aqui o primeiro valor: '))
    div2 = int(input('Digite aqui o segundo valor: '))
    if div2 != 0:
        divisao = div1 / div2 
        print(f'O resultado dessa operação é: {divisao}')
    else:
        print('Não é possível dividir por zero.')

print('Qual operação deseja realizar?')
print('[1] Soma')
print('[2] Subtração')
print('[3] Multiplicação')
print('[4] Divisão')

opcao_escolhida = input('Digite a opção desejada: ')

if opcao_escolhida == '1':
    Soma()
elif opcao_escolhida == '2':
    Subtracao()
elif opcao_escolhida == '3':
    Multiplica()
elif opcao_escolhida == '4':
    Divide()
else:
    print('Opção inválida. Tente novamente.')