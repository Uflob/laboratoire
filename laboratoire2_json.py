import json
import csv

"""RO : Gérer les présences d'un laboratoire"""
"""R1 : Définir des exception"""

class LaboException(Exception):
    """ Généralise les exceptions du laboratoire."""
    pass
class AbsentException(LaboException):
    """ Créé une exception pour les personnes inexistante du laboratoire"""
    pass
class PresentException(LaboException):
    """ Créé une exception pour les personnes déjà présente dans le laboratoire"""
    pass

"""R1 : Initialiser le laboratoire"""

def laboratoire():
    try:
        with open("data_labo.txt", "r") as file:
            labo = json.load(file)
    except FileNotFoundError:
        labo = {}
    return labo

def sauvegarde_data(labo):
    with open("data_labo.txt", "w+") as file :
        json.dump(labo,file)


def importer_csv(labo, fichier="labo_csv.csv"):
    differences = []
    with open(fichier, newline='') as csvfichier:
        lecteur = csv.DictReader(csvfichier)
        for ligne in lecteur:
            nom = ligne["Nom"]
            bureau = ligne[" Bureau"]
            if nom not in labo:
                labo[nom] = bureau
            elif bureau != labo[nom]:
                differences.append(f"{nom} : {labo[nom]} est maintenant en {bureau}.")
    if differences:
        texte = "Voici les modifications :\n"
        for diff in differences:
            texte += "- " + diff + "\n"
        return texte




"""R1 : Gérer les arrivées et les départs"""

def enregistrer_arrivee(labo, nom, bureau):
    if nom in labo:
        raise PresentException
    labo[nom] = bureau

def enregistrer_depart(labo, nom):     
    if nom not in labo:
        raise AbsentException
    del labo[nom]


"""R1 : Gérer les modification"""

def changer_bureau(labo, nom, nouveau_bureau):
    labo[nom] = nouveau_bureau

def changer_nom(labo, ancien_nom, nouveau_nom):     
    labo[nouveau_nom] = labo[ancien_nom]
    del labo[ancien_nom]


"""R1 : Gérer les vérifications"""

def est_presente(labo, nom):
    return nom in labo

def check_bureau(labo, nom):
    return labo[nom]

def liste(labo):
    return labo.items()

def occupation_bureaux(labo):
    occupation = {}
    for nom, bureau in labo.items():
        if bureau not in occupation:
            occupation[bureau] = []
        occupation[bureau].append(nom)
    return occupation


def main():
    print('test')

if __name__ == '__main__':
    main()