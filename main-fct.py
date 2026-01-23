#1 PROJECT QUI DEMANDER L'INFORMATION D'UN USER ; NOM ET AGE
# VERSION SIMPLE 
#2 AMELIORATION DU PROJET AVEC LA FONCTION ET PARAMETRE


# 1 Creation de la variable nom/while
# 2 fct damander nom

def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est votre nom ? : ")
    return nom

# 1 Creation de la variable age/while
# 2 fct demander l'age
def demander_age():
    age = 0
    while age == 0:
        age_str = input("Quel est votre age ? : ")
        try:
            age = int(age_str)
        except:
            print("ERREUR: vous devez entre un nombre pour l'age")
    return age
        

def afficher_informations_personne(nom, age):
    print(f"Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'annee prochaine vous aurez " + str(age + 1) + " ans")  

# nom1 = demander_nom()
# nom2 = demander_nom()


# age1 = demander_age()
# age2 = demander_age()

# # Afficher
# # fct afficher informations personne

# afficher_informations_personne(nom1, age1)
# afficher_informations_personne(nom2, age2)


for i in range(0,2):
    nom = demander_nom()
    age = demander_age()
    afficher_informations_personne(nom, age)
