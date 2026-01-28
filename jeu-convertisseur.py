# Jeu convertisseur d'une valeur pouce vers cm et cm vers pouce
#1 CREATION DES VARIABLES
#2 CREATION DE CONDITION : if, elif, else
#3 FACTORISER LE PROGRAMME AVEC LA FONCTION : def 
#4 CREATION D'UNE OPTION POUR QUITTER
#5 AJOUT LE CAS D'ERREUR


pouce = 2.54
cm = 0.394
#fonction
def demander_converssioin(unit1: str, unit2: str, facteur: float):
        valeur_str = input(f"Entrez une valeur en {unit1} vers {unit2} ou (q pour quitter): ")
        if valeur_str == "q":
            return True
        try:
            valeur_float = float(valeur_str)
        except ValueError:
            print("ERROR : vous devez entrer une valeur numerique ")
            print("Utilisez le point virgule pour le decimal")
            return demander_converssioin(unit1,unit2 ,facteur)
            
        resultat = round(valeur_float * facteur, 2)
        print(f"Resultat de la converssion {valeur_float} pouce vers cm est : {resultat} cm")
        return False
#menu
while True:
    print("Ce programme convertie une valeur de pouce vers cm et cm pouce ")
    print("1 --> Pouce vers cm")
    print("1 --> Cm vers pouce")
    choix = input("Souhaitez-vous convertir une valeur (1 ou 2): ")
    if choix == "1" or choix == "2":
        break
    print("ERROR: vous devez choisir 1 ou 2")

while True:
    if choix == "1":
        if demander_converssioin("pouce", "cm", 2.54):
            break
    elif choix == "2":
        if demander_converssioin("cm", "pouce", 0.394):
            break
    
    
print("MERCI")