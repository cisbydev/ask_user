# PROJECT QUI DEMANDER L'INFORMATION D'UN USER

# 1 Creation de la variable nom

nom = ""
while nom == "":
    nom = input("Quel est votre nom ? : ")

age = 0

while age == 0:
    age_str = input("Quel est votre age ? : ")
    try:
        age = int(age_str)
    except:
        print("ERREUR: vous devez entre un nombre pour l'age")
    else:
        print(f"Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
        print("L'annee prochaine vous aurez " + str(age + 1) + " ans")


