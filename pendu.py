### Pendu
from random import *

tabmot=["banane","carotte","distinction","maison","ordinateur","arcane","disparite","constitution","patricide","karate"]
mot_a_remplir=""
###alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


dessin=[[["          "],
        ["          "],
        ["          "],
        ["          "],
        ["          "],
        ["▬▬▬▬▬▬▬▬▬▬"]],
        
        [["          "],
        ["    |     "],
        ["    |     "],
        ["    |     "],
        ["    |     "],
        ["▬▬▬▬▬▬▬▬▬▬"]],

        [["     ___  "],
        ["    /     "],
        ["    |     "],
        ["    |     "],
        ["    |     "],
        ["▬▬▬▬▬▬▬▬▬▬"]],

        [["     ___  "],
        ["    /  |  "],
        ["    |     "],
        ["    |     "],
        ["    |     "],
        ["▬▬▬▬▬▬▬▬▬▬"]],


        [["     ___  "],
        ["    /  |  "],
        ["    |  ☺  "],
        ["    |     "],
        ["    |     "],
        ["▬▬▬▬▬▬▬▬▬▬"]],


        [["     ___  "],
        ["    /  |  "],
        ["    |  ☺  "],
        ["    |  O  "],
        ["    |     "],
        ["▬▬▬▬▬▬▬▬▬▬"]],

        [["     ___  "],
        ["    /  |  "],
        ["    |  ☺  "],
        ["    |  O  "],
        ["    | //  "],
        ["▬▬▬▬▬▬▬▬▬▬"]],


        [["     ___  "],
        ["    /  |  "],
        ["    |  ☺  "],
        ["    | .O  "],
        ["    | //  "],
        ["▬▬▬▬▬▬▬▬▬▬"]],

        [["     ___  "],
        ["    /  |  "],
        ["    |  ☺  "],
        ["    | .O. "],
        ["    | //  "],
        ["▬▬▬▬▬▬▬▬▬▬"]]]


def affichage_matrice(matrice):
    for elt in matrice:
        for i in elt :
            print(i,end=" ")
        print(" ")



def longueur_mot(mot):
    compteur=0
    for elt in mot:
        compteur+=1
    return compteur



def mot_aleatoire(tab):
    nombre=randint(0,len(tabmot)-1)
    return tab[nombre]

def vide():
    for i in range(10):
        print(" ")
        
        
def tabindice_mot_lettre(mot,lettre):
    tabindice=[]
    for i in range(len(mot)):
        if mot[i] == lettre:
            tabindice.append(i)
    return tabindice


def jeu():
    global mot_a_remplir,dessin

    nombre_essai=0
    
    mot_a_trouver=mot_aleatoire(tabmot)

    tab_mot_a_trouver=[]
    for elt in mot_a_trouver:
        tab_mot_a_trouver.append(elt)
     
    for i in range(len(mot_a_trouver)):
        # fill mot_a_remplir de "_"
        mot_a_remplir += "_"
    
    tab_mot_a_remplir=[]
    
    for elt in mot_a_remplir:
        tab_mot_a_remplir.append(elt)
        
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("             Le Pendu® par Tom ^^")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
#     
#     print(mot_a_remplir)
    
    
    while tab_mot_a_remplir != tab_mot_a_trouver:
        
        if nombre_essai>=8:
            print("Dommage, vous avez perdu. Le mot était: ")
            print("                               -",mot_a_trouver)
            return
        
        
        demande_lettre=input("Veuillez saisir une lettre : ")
        

        tab_indice = tabindice_mot_lettre(mot_a_trouver,demande_lettre)
        vide()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("             Le Pendu® par Tom ^^")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(" ")
            
        if  demande_lettre not in mot_a_trouver:
            nombre_essai+=1
            for elt in tab_mot_a_remplir:
                print(elt,end=" ")
            print(" ")
            affichage_matrice(dessin[nombre_essai])
            print(" ")
                
        else:
            for i in range(len(tab_indice)):
                tab_mot_a_remplir[tab_indice[i]]=demande_lettre
                    
            for elt in tab_mot_a_remplir:
                print(elt,end=" ")
                
            print(" ")
            print(" ")
            affichage_matrice(dessin[nombre_essai])
    

jeu()

# 
# score=open("Score.csv



