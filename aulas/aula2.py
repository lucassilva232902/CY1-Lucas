#string → textos

#uma palavra
string1 = "oi"

string2 = "oi,tudo bem"

string3 = 'Ctrl+play - escola de programação e robótica'

print(string1)
print(string2)
print(string3)

# função len() → verifica a quantidader de caracteres

print(len(string3))

nome = 'lucas silva martins da costa'

print(nome[13])

print(nome[:10])

print(nome[:-1])

print(nome[:12])

print(nome[::2])

email = 'fulano@ctrplay.com.br'
print(email,find('@'))
pos = email.find('@')
print (email[:pos])

print(email.count('.'))

nome = 'josé'
sobrenome = 'bond'
print(nome+sobrenome)
print(nome*5)
media = 6.5
print('A média do '+nome+' foi de '+str(media))
print('Amédia do',nome,'foide',media)