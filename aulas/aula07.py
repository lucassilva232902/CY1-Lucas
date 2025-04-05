# Funções

'''

funções são algoritimos criados com objetivo de executar uma cadeia de comandos que podem/vão se repetir várias vezes no programa fazendo assim não ter a nescessidade de recriar o algoritimo toda vez que precisar repeti-lo apenas chamando a execução da função desejada.

'''

# Como criar um função. Para criar uma função basra digitar o comando "def" logo em seguida passar o nome da função colocar "()" e finalizar a linha com ":" EX.: def Pular():

#dica: tente diferenciar suas funções de variaveis como por exemplo fazendo suas funções sempre começar com letras maiúsculas e variáveis sempre com minúsculas

def Boas_vindas():
    print('bem-vindo à Ctrl+play')

# Para executar uma função basta chama-la da seguinte forma

Boas_vindas()

#Os parenteses de uma função é a região de parâmetros, que são informações que a função precisa para ser executada com por exemplo, uma função de somar necessita de dois números para poder realizar os cálculos.

def Saudacao(nome):
    print('Saudações '+nome+',como está a aula de hoje?')

Saudacao('lucas')

def Velocidade(distancia,tempo=1.5):
    velocidade = distancia/tempo
    print(f'A sua velocidade foi de {velocidade:.2f}Km/hora')

#d = int(input('Digite qual a distancia percorrida: '))
#t = int(input('Digite em quanto tempo fez o percurso: '))

#Velocidade(t,d)

#Valor arnitrário é quando você quer passar para uma função vários valores porém não sabe a quantidade exata de valores que vai passar, para isso basta colocar o'*' antes do nome do parâmetro

def prepare_acai(*ingredientes, tamanho='médio'):
    print(f'preparando um açai {tamanho}, com os seguintes ingredientes adicionais: ')
    for ingrediente in ingredientes:
        print(f'- {ingrediente}')


prepare_acai('banana','granola')
prepare_acai('morango','kiwi','leite em pó', tamanho='grande')
prepare_acai('banana',tamanho='pequeno')
prepare_acai()

#Funções compostas: são funçoes que chamam outras funções em suas definições

def Maior(lista):
    maiorValor = lista[0]
    for x in lista:
        if(x > maiorValor):
            maiorValor=x
    return maiorValor

def Menor(lista):
    menorValor = lista[0]
    for x in lista:
        if(x < menorValor):
            menorValor=x
    return menorValor


def Maior_Menor(lista):
    print(f'Maior: {Maior(lista)}')
    print(f'Menor: {Menor(lista)}')

Maior_Menor([4,5,6,2,1,3])

#Funções recursivas: São funções que d4entro da sua definição elas chamam a si mesma para ser executada

def DobraLencol(lencol:int,gaveta:int):
    if(lencol<gaveta):
        return 0
    else:
        return 1 + DobraLencol(lencol/2,gaveta)
L = DobraLencol(200,25)
print(L)