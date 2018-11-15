# encoding: utf-8

# On demande de renseigner la clé privé (on peut aussi donner la clé publique a condition de decrypter plus tard avec la privée)
d = input('\nEntrez le d de votre cle privee : ')
n = input('\nEntrez le n de votre cle privee : ')

#On demande le nombre a crypté
nombre = raw_input('\nEntrez le nombre a crypte : ')

# On recuperer l'unicode du nombre
nbc = ord(nombre)

# On le crypte
crypt = pow(nbc,d)%n

# si la taille du bloc crypter est superieur a n c'est impossible
if nbc > n :
    print "Cryptage impossible"

# On affiche le bloc crypté
print "\n message crypte : ",crypt,

raw_input('\n\nFin\n\n')
