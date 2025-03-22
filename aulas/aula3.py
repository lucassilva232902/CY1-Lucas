#region Criação, Adição e Remoção de Lista

# para criar uma lista no pytom basta declarar o nome e após o = usar o símbolo de colchetes

convidados = ['Pedro','Lucas','Sebastian','Júlia','Leonan','Magnum']
print(convidados)

#os índices em pytom basta colocar o valor dentro de []
print('primeiro convidado da festa: '+convidados[0])
print('penúltimo convidado da festa: '+convidados[-2])

#substituindo o primeiro intem
convidados[0] = 'isabella'
print(convidados)

#adicionando um item na lista, sempre vai para o final dela;
convidados.append('Pedro')
print(convidados)

# se eu quiser adicionar em um local expecífico da lista
convidados.insert(0,'Antônio')
print(convidados)

#eliminar um item da lista
del convidados[0]
print(convidados)

#exclui o item na lista mas salva em uma variável
convidadosRemovido = convidados.pop()
print(convidados)
print(convidadosRemovido)

convidadosRemovido = convidados.pop(0)
print(convidados)
print(convidadosRemovido)

#exclui por um item específico
viajando = 'Leonan'
convidados.remove(viajando)
print(convidados)
print(viajando+' não vai a festa, pois está viajando')
#endregion

#region organizando item na lista

#sorted() → ele organiza a lista em ordem alfabética apenas para exibição
print(sorted(convidados))
print(convidados)
print(sorted(convidados,reverse=True))
print(convidados)

#sort() → ele organiza a lista em ordem alfabética porém de fato altera a lista
#convidados.sort()
print(convidados)
#para fazer invertido basta colocar reverse+True dentro do()
#reverse() → inverte a lista sem organizar em ordem alfabética
convidados.reverse()
print(convidados)
#endregion

#region funções úteis



#exibir o tamanho de uma lista
print(len(convidados))
numeros = list(range(1,5))
print(min(numeros))

#maior valor

print(max(numeros))

#fatia de uma lista
print(convidados[1:3])

#para copiar uma lista
convidados2 = convidados[:]
print(convidados2)
#endregion

#region Matrizes





timesXpessoas = [['Palmeiras','Flamengo','Sport','Galo','Bruzeiro'],['José','Maria','Tiago','Lucas','Luana']]
print(timesXpessoas)

#para exibir uma lista específica
print(timesXpessoas[0][3])
print(timesXpessoas[1][3])

#endregion