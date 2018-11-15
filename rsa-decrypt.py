# encoding: utf-8

# On demande de renseigner la clé publique (on peut aussi donner la clé privée a condition d'avoir crypter avec la publique)
e = input('\nEntrez le e de la cle publique : ')
n = input('\nEntrez le n de la cle publique : ')

# On demande le bloc a decrypter
nombre = input("\nEntree le bloc a decrypte :")
# On decrypte et on se retrouve avec le nombre sous unicode
ascii = (pow(nombre,e)%n)
#On affiche le nombre sans l'unicode avec la fonction chr() qui est l'inverse de ord()
print "nombre :",chr(ascii),

raw_input('\n\nFin\n\n')
