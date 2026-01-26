#1 CREATION DES VARIABLES
#2 CREATION DE LA FONCTION : def/input
#3 AJOUT DE LA CONDITION  : if, elif, else
#4 AJOUT DE LA BOUVLE : while 
#5 AJOUT LE CAS D'ERREUR : try/except
#6 AJOUT LE NOMBRE ALEATOIR : random
#6 AJOUT LE NOMBRE DE LIMITER 

import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIE = 4


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique entre ({nb_min} et {nb_max})? : ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERROR: vous devez un nombre. Réessayez")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERROR: le nombre magique doit etre entre ({nb_min} et {nb_max}). Réessayez")
                nombre_int = 0
    return nombre_int


    # AVEC LA BOUCLE WHILE
# nombre = 0
# vie = NB_VIE
# while not nombre == NOMBRE_MAGIQUE and vie > 0:
#     print(f"il vous restez {vie} vies")
#     nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
#     if nombre == NOMBRE_MAGIQUE:
#         print("Bravo vous avez gagne")
#     elif nombre > NOMBRE_MAGIQUE:
#         print("le nombre magique est petit")
#
#     else:
#         print("le nombre magique est grand")
#
# if vie == 0:      
#     print(f"Vous avez perdu le nombre magique etait {NOMBRE_MAGIQUE}")


        # AVEC LA BOUCLE FOR
gagne = False
for i in range(0, NB_VIE):
    vie = NB_VIE-i
    print(f"il vous restez {vie} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo vous avez gagne")
        gagne = True
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre magique est petit")
    else:
        print("le nombre magique est grand")
 
if not gagne:
    print(f"Vous avez perdu le nombre magique etait {NOMBRE_MAGIQUE}")