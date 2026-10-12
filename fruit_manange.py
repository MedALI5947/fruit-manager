import json

def ouvrir_inventaire(chemin):
    with open( chemin, 'r', encoding='utf-8') as fichier:
        json.load(fichier)
        
        
        
def ecrire_inventaire(inventaire, chemin):
    with open( chemin, 'w', encoding='utf-8') as fichier:
        json.dump(inventaire,fichier, ensure_ascii=False, indent=4 )
        

def afficher_inventaire(inventaire):
    print(f"inventaire actuel de la plantation")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite}")
        
        
def recolter(inventaire, fruit, quantite):
    
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"recolter {quantite} {fruit} supplmentaire")
    
def vendre(inventaire, fruit, quantite):
    if inventaire.get(fruit, 0) > quantite:
        inventaire[fruit] -= quantite
        print(f"Vendu {quantite} {fruit}")
    else:
        print(f" pas assez de {fruit} pour vendre {quantite} unités")
        


if __name__ == "__main__":
    inventaire = ouvrir_inventaire("data/inventaire.json")
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 10)
    vendre(inventaire,"bananes", 5)
    afficher_inventaire(inventaire)