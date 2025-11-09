from laboratoire2 import *

'''
menu est une liste d'intitulés
'''
def Menu():
    return []

def ajouter_entree(menu,intitulé,fn, *parametres):
    menu.append((intitulé, fn, parametres))


def traiter(menu,choix):
    assert 0<= choix <= len(menu)
    if choix != 0:
        _, fn, parametres = menu[choix-1]
        fn(*parametres)


def selection(menu):
    while True :
        try:
            numero = int(input("Votre choix"))
            if 0 <= numero <= len(menu):
                return numero
            else:
                print("Pas un numéro du menu")
        except ValueError:
            print ("Incorrect...")


def afficher_menu (menu):
    for indice, (intitulé,_,_) in enumerate(menu,1):
        print(f"{indice:2d} - {intitulé}")
    print(f"{0:2} - Quitter")


def gerer (menu):
    quitter = False
    while not quitter :
        afficher_menu(menu)
        choix = selection(menu)
        traiter(menu, choix)
        quitter = choix == 0


def verifier_presence(labo):
    nom = input("Nom ?")
    response = est_presente(labo,nom)
    print("oui, presente" if response else "non, inconue")


if __name__ == "__main__" :

    def afficher_bonjour():
        print("Bonjour")

    def afficher_bye():
        print("Bye")
        

    menu2 = Menu()
    ajouter_entree(menu2,"Bonjour", afficher_bonjour)
    ajouter_entree(menu2,"Bye", afficher_bye)
    print("menu2 =", menu2)
    
    gerer(menu2)



   

    