from laboratoire2 import *

'''
Interface sur la labo avec menu textuel.
'''

def afficher_menu():
    print("1- Enregistrer une arrivée ")
    print("2- Enregistrer un départ ")
    print("3- Modifier un bureau ")
    print("4- Modifier un nom ")
    print('5- Présence d\'une personne ')
    print("6- Obtenir le bureau d\'un membre ")
    print("7- Obtenir le listing complet ")
    print("8- Afficher l\'occupation des bureaux ")
    print("0- Quitter ")



def demander_choix():
    return int(input("Votre choix: "))

def gerer_arrivee(labo):
    try:
        nom = input("Nom ? ")
        if nom in labo:
            raise PresentException
        bureau = input("Bureau ? ")
        enregistrer_arrivee(labo, nom, bureau)
    except PresentException:
        print("Impossible: déjà là ")


def gerer_depart(labo):     
    try:
        nom = input("Nom ? ")
        enregistrer_depart(labo, nom)
    except AbsentException:
        print("Nom inconnu")


def modifier_bureau(labo):    
    try:
        nom = input("Nom ? ")
        nouveau_bureau = input("Nouveau bureau ? ")
        changer_bureau(labo, nom, nouveau_bureau)
        print ("Modification effectuée")
    except AbsentException:
        print("Nom iconnu")


def modifier_nom(labo):      
    ancien_nom = input("Nom actuel ? ")
    nouveau_nom = input("Nouveau nom ? ")
    changer_nom(labo,ancien_nom,nouveau_nom)
    print ("Modification effectuée")


def verifier_membre(labo):      
    nom = input("Nom ? ")
    reponse = est_presente(labo,nom)
    if reponse == True:
        print("oui")
    else:
        print("non")


def verifier_bureau(labo):      
    nom = input("Nom ? ")
    bureau = check_bureau(labo,nom)
    print (bureau)


def listing_complet(labo):
    for nom, bureau in liste(labo):
        print(f"{nom} → {bureau}")


def liste_bureaux(labo):
    occupation = occupation_bureaux(labo)
    for bureau in sorted(occupation):
        print(f"{bureau}: " )
        for nom in occupation[bureau]:
            print(f"- {nom}")


def traiter_choix(choix, labo):
    if choix == 1:
        gerer_arrivee(labo)
    elif choix == 2:
        gerer_depart(labo)
    elif choix == 3:
        modifier_bureau(labo)
    elif choix == 4:
        modifier_nom(labo)
    elif choix == 5:
        verifier_membre(labo)
    elif choix ==6:
        verifier_bureau(labo)
    elif choix ==7:
        listing_complet(labo)
    elif choix == 8:
        liste_bureaux(labo)
    elif choix == 0:
        print("Quitter")
    else :
        print("Choix invalide")



def main():
    quitter = False
    labo = laboratoire()
    while not quitter:
        afficher_menu()
        choix = demander_choix()
        traiter_choix(choix, labo)
        quitter = choix == 0


if __name__ == '__main__':
    main()