# encoding: utf-8
import random
from math import sqrt

# Fonction verifie si un nombre est premier
def prime(x):
    if x%2==0:return False
    elif any(x%i==0 for i in xrange(3,int(sqrt(x))+1,2)):return False
    else:return True

# On choisi au hasard notre p, un nombre premier entre 3000 et 3200

prime_list=[x for x in xrange(10,100) if prime(x)]

p = random.choice(prime_list)

# On choisi au hasard notre q, un nombre premier entre 4900 et 5000

prime_list=[x for x in xrange(100,200) if prime(x)]

q = random.choice(prime_list)

# On affiche nos deux notre premier generé
print "\nNombre premier p genere = ",p,
print "\nNombre premier q genere = ",q,


# Fonction qui donne le PGCD de a et b

def pgcd(a,b):
    # L'algo PGCD
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a;

# On calcul n
n = p*q

# On affiche n

print "\nn = ",n,

# On calcul phi(n)
phiden = (p-1)*(q-1)

# On affiche phi(n)

print "\nphi de n = ",phiden,


i = 0
pgcdegal1 = 0
e = 0

#On boucle jusqu'a que le pgcd de e et phi(n) donne 1
while pgcdegal1 != 1 :
    while i == 0 :
        if((p < e)and(q < e)and(e < phiden)) :
            i = 1
        e = e + 1
    pgcdegal1 = pgcd(e,phiden)

# On affiche notre cle publique
print "\nLa cle publique est (e,n)(",e,",",n,")"

# On la sauvegarde dans clepublique.txt
fichier = open("clepublique.txt", "w")
fichier.write(str(e)+","+str(n))
fichier.close()


# On calcul d
d = 0
i = 0

while i == 0:
	if((e * d % phiden == 1)and(p < d)and(q < d)and(d < phiden)):
	    i = 1
	d = d + 1
d = d - 1

# On affiche la cle privé
print "\nLa cle privee est (d,n)(",d,",",n,")"
# On la sauvegarde dans cleprive.txt
fichier = open("cleprive.txt", "w")
fichier.write(str(d)+","+str(n))
fichier.close()

print "\nUn fichier a ete creer pour le couple de cle"

raw_input('\n\nFin\n\n')
