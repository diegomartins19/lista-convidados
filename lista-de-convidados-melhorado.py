numero_de_convidados = input('Quantas pessoas vao pra festa? ')
lisa_de_convidados = []

i = 1
while i <= int(numero_de_convidados):
    nome_de_convidado = input('Coloque o nome do convidado ' + str(i)+ ': ')
    lisa_de_convidados.append(nome_de_convidado)
    i += 1
print('Serao chamados ' + numero_de_convidados , 'convidados')
print('\nLISTA DE CONVIDADOS')
for convidado in lisa_de_convidados:
    print(convidado)

opcao_1 = str(input('Quer quer adicionar mais alguem?'))

if opcao_1 == 'sim':
    lisa_de_convidados.append(input('Escreva o nome para adicionar: '))
    print('\nSerao Chamados ' + numero_de_convidados, 'convidados')
    print('\nLista de convidados')

    for convidado in lisa_de_convidados:
        print(convidado)

opcao_2 = str(input('QUer remover alguem?'))
print('\n')

if opcao_2 == 'sim':
    lisa_de_convidados.remove(input('Escreva o nome para remover:  '))
    print('\nSerao Chamados ' + numero_de_convidados, 'convidados')
    print('\nLista de convidados')

    for convidado in lisa_de_convidados:
        print(convidado)

opcao_3 = str(input('Quer sair? '))
if opcao_3 == 'sim':
    exit(input('Escreva 0 para sair: '))


print('\nSerao Chamados ' + numero_de_convidados, 'convidados')
print('\nLista de convidados')

for convidado in lisa_de_convidados:
    print(convidado)

