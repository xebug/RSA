# encoding: utf-8


print "Attaque brute en factorisant n"
print "A utiliser si vous ne connaissez pas la clé mais juste n."

n = input('\nEntrez le n : ')


chiffre=2
while 1:
    while n%chiffre!=0 :
        chiffre=chiffre+1
    if n/chiffre==1 :
        print "p:", chiffre,
        break
    print "q:", chiffre,
    q=chiffre
    n=n/chiffre;



# On bloque le programme avant la fermeture
raw_input('\n\nFin\n\n')
