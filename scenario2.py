from laboratoire2 import *

def main():
    labo = laboratoire()
    enregistrer_arrivee(labo, "Xavier", "F305")
    enregistrer_arrivee(labo, "Marc", "F305")
    enregistrer_arrivee(labo,"Aurélie", "F307")

    print(labo)

    # test de présence
    assert est_presente(labo, "Xavier")
    assert est_presente(labo, "Marc")
    assert not est_presente(labo, 'Paul')

    # test de départ
    enregistrer_depart(labo,"Marc")
    assert "Marc" not in labo

    # test changement de bureau
    changer_bureau(labo, "Xavier", "F410")
    assert labo["Xavier"] == "F410"

    # test changement de nom
    changer_nom(labo, "Xavier", "Alexandre")
    assert "Xavier" not in labo
    assert "Alexandre" in labo
    assert labo["Alexandre"] == "F410"

    # test occupation de bureau
    occupation = occupation_bureaux
    assert "F305" not in occupation
    assert "F410" in occupation

if __name__ == '__main__':
    main()