#1 CREATION DES VARIABLES 
#2 CREATION DE LA FONCTION : def/input
#3 AJOUT DE LA CONDITION if elif else
#4 CREATION DE LA BOUCLE WHILE
#5 AJOUT DE NOMBRE ALEATOIR : random
#6 AJOUT DU CAS D'ERREUR


import random
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QURSTION = 4

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    operateur = "+"
    if o == 1:
        operateur = "*"
    reponser_int = 0
    while reponser_int == 0:

        reponser_str = input(f"Calculez {a} {operateur} {b} = ")
        try:
            reponser_int = int(reponser_str)
        except:
            print("ERROR: vous devez entre un nombre. Réessayez")
    calcul = a+b
    if o == 1:
        calcul = a*b
    if reponser_int == calcul:
        # print("Réponse correcte")
        return True
        #print("Réponse incorrecte")
    return False
    
nb_points = 0  
for i in range(0, NB_QURSTION):
    print(F"Question n°{i+1} sur {NB_QURSTION}")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrecte")
        
print(f"Votre point est {nb_points}/{NB_QURSTION}")
moyenne = int(nb_points/2)
if nb_points == NB_QURSTION:
    print("Excellent")
elif nb_points == 0:
    print("Révise vos maths")
elif nb_points  > moyenne:
    print("Pas mal")
else:
    print("Peut mieux faire")