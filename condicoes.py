n1 = 2
n2 = 7
n3 = 8
n4 = 9

nota = n1 + n2 + n3 + n4
media = nota/4

if media>=7:
    print(media, ' - Aprovado')
elif media <5:  # if ternário
    print(media, ' - Reprovado')
else:
    print(media, ' - Em recuperação')