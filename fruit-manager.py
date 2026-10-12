inventaire = {"bananes" : 120,
               "mangues" : 85,
               "ananas": 45,
               "noix e coco": 60,
               "papayes":30
               }



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
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 10)
    vendre(inventaire,"bananes", 5)
    afficher_inventaire(inventaire)