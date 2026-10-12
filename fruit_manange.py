import json

def ouvrir_inventaire(path ="data/inventaire.json"):
    with open(path, 'r', encoding='utf-8') as fichier:
        json.load(fichier)
        
        
        
def ecrire_inventaire(inventaire, path ="data/inventaire.json"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(inventaire,fichier, ensure_ascii=False, indent=4 )
        
def ouvrir_tresoreries(path ="data/inventaire.json"):
    with open(fichier, 'w', encoding='utf-8') as fichier:
        tresoreries = json.load(fichier)
    return tresoreries
        

def ecrire_tresoreries(tresorerie, path = "data/tresorerie.txt"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)
        
def afichier_tresorerie(tresorerie):
    print(f"Tresorerie actuelle :{tresorerie: .2f} $")
    
def afficher_inventaire(inventaire):
    print(f"inventaire actuel de la plantation")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite}")
        
        
def recolter(inventaire, fruit, quantite):
    
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"recolter {quantite} {fruit} supplmentaire")
    
def vendre(inventaire, fruit, quantite, tresorerie):
    if inventaire.get(fruit, 0) > quantite:
        inventaire[fruit] -= quantite
        tresorerie += 1 * quantite
        print(f"Vendu {quantite} {fruit}")
        return(inventaire,tresorerie)
    else:
        print(f" pas assez de {fruit} pour vendre {quantite} unités")
        


if __name__ == "__main__":
    inventaire = ouvrir_inventaire("")
    tresororie = ouvrir_tresoreries()
    afichier_tresorerie(tresororie)
    afficher_inventaire(inventaire)
    
    recolter(inventaire, "bananes", 10)
    inventaire, tresororie = vendre(inventaire,"bananes", 5)
    ecrire_inventaire(inventaire)
    ecrire_tresoreries(tresororie)
    
   # afficher_inventaire(inventaire)