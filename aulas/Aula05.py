#Estrutura de Repetição

#existe dois tipos de extruturas de repetição o For e o While→ Para e Enquanto

#region For

'''A estrutura do for atua como um literador em python, isto é, um objetivo que percorre itens que estão em sequência e retorna os dados desses itens de maneira sucessiva, um elemento de cada vez.

# Estrutura:

for item in objeto:
    codigos que vão se repetir


'''
#Exemplo

#exibir o dobro do valor dos números pares encontrados na lista de 1 a 20
# % = resto da divisão
listaNumeros = range(1,21)
for num in listaNumeros:
    if num % 2 ==0:
        print('O número par é:',num,'o seu dobro:',num*2)

#imprime a string em coluna
for letra in 'Ctrl+Play':
    print(letra)


#endregion

#region While
#A instrução while em python é uma das formas mais gerais de executar literações. Ela executa repetidamente um trecho de código enquanto uma condição for verdadeira
'''
Extrutura:

while condição:
    código que vai se repetir
'''
x = 0
while x < 5:
    print('o valor de x:',x)
    print(' x ainda é menor que 5, vamos somar 1')
    x+=1 #mesma coisa de fazer x=x+1
else:
    print('FIM')

    
#endregio
