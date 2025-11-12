from laboratoire2_json import *
from menu_simple2 import *


  
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
        if nom not in labo:
            raise AbsentException
        changer_bureau(labo, nom, nouveau_bureau)
        print("Modification effectuée")
    except AbsentException:
        print("Nom inconnu")


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




def importer_fichier_csv(labo):
    nom_fichier = input("Nom du fichier CSV à importer ? ")
    rapport = importer_csv(labo, nom_fichier)
    print("\nRapport d’import :")
    print(rapport)
    sauvegarde_data(labo)
    print("Les données importées ont été sauvegardées.")




def main():
    labo = laboratoire()  

    menu = Menu()
    ajouter_entree(menu, "Enregistrer une arrivée", gerer_arrivee, labo)
    ajouter_entree(menu, "Enregistrer un départ", gerer_depart, labo)
    ajouter_entree(menu, "Modifier un bureau", modifier_bureau, labo)
    ajouter_entree(menu, "Modifier un nom", modifier_nom, labo)
    ajouter_entree(menu, "Présence d'une personne", verifier_membre, labo)
    ajouter_entree(menu, "Obtenir le bureau d’un membre", verifier_bureau, labo)
    ajouter_entree(menu, "Obtenir le listing complet", listing_complet, labo)
    ajouter_entree(menu, "Afficher l’occupation des bureaux", liste_bureaux, labo)
    ajouter_entree(menu, "Importer un fichier CSV et afficher les modifications", importer_fichier_csv, labo)

    gerer(menu)  
    sauvegarde_data(labo)  
    print("\nLes données ont été sauvegardées.")


if __name__ == "__main__":
    main()

