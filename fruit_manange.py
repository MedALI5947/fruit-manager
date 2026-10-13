import json


def ouvrir_prix(path="data/prix.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        prix = json.load(fichier)
        return prix

def ouvrir_inventaire(path="data/inventaire.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        return json.load(fichier)



def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def ouvrir_tresoreries(path="data/tresorerie.txt"):
    with open(path, "r", encoding="utf-8") as fichier:
        return json.load(fichier)


def ecrire_tresoreries(tresorerie, path="data/tresorerie.txt"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)


def afficher_tresorerie(tresorerie):
    print(f"Trésorerie actuelle : {tresorerie:.2f} $")


def afficher_inventaire(inventaire):
    print("Inventaire actuel de la plantation")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite}")


def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"Récolté {quantite} {fruit} supplémentaires")


def vendre(inventaire, fruit, quantite, tresorerie, prix ):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += prix.get(fruit, 0) * quantite # Prix : 1 $ par unité
        print(f"Vendu {quantite} {fruit}")
    else:
        print(f"Pas assez de {fruit} pour vendre {quantite} unités")

    return inventaire, tresorerie


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresoreries()
    prix = ouvrir_prix()

    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)

    recolter(inventaire, "bananes", 10)
    inventaire, tresorerie = vendre(
        inventaire, "bananes", 5, tresorerie,prixp
    )

    ecrire_inventaire(inventaire)
    ecrire_tresoreries(tresorerie)

    afficher_inventaire(inventaire)
    afficher_tresorerie(tresorerie)