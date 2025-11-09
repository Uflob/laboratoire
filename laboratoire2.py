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
    return {}


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