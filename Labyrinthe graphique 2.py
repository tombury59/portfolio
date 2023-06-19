from tkinter import *

'''
Initialisation d'une matrice qui sera le référent du canvas et du labyrinthe
taille: 14 elt *14 elt
'''
tab=[["█","•","█","█","█","█","█","█","█","█","█","█","█","█"],
     ["█"," "," "," "," "," ","█"," "," "," "," "," "," ","█"],
     ["█"," ","█"," ","█"," ","█"," ","█","█","█","█"," ","█"],
     ["█","█","█"," ","█"," "," "," ","█"," "," ","█"," ","█"],
     ["█"," "," "," ","█"," ","█","█","█"," ","█","█","█","█"],
     ["█","█","█","█","█"," ","█"," "," "," ","█"," "," ","█"],
     ["█"," "," "," "," "," ","█"," ","█"," "," "," ","█","█"],
     ["█"," ","█","█","█"," ","█"," ","█","█","█"," "," ","█"],
     ["█"," ","█"," ","█"," ","█"," "," "," ","█","█"," ","█"],
     ["█"," ","█"," "," "," ","█"," ","█","█","█"," "," ","█"],
     ["█"," ","█","█","█","█","█"," ","█"," ","█"," ","█","█"],
     ["█"," ","█"," "," "," ","█"," ","█"," ","█"," "," ","█"],
     ["█"," "," "," ","█"," "," "," "," "," ","█","█"," ","█"],
     ["█","█","█","█","█","█","█","█","█","█","█","█","v","█"]]


'''
Initiation d' tkinter/canvas qui va accueillir le labyrinthe
taille : 350px * 350px
'''
root=Tk()
root.geometry('350x350')
canvas=Canvas()

def couleur():
    '''Remplie le canvas de couleur'''
    global tab
    for i in range(len(tab)):
            for j in range(len(tab[0])):
                if tab[i][j]=="█":
                    canvas.create_rectangle(j*20,i*20,j*20+20,i*20+20,outline='black',fill='black')
                if tab[i][j]==" ":
                    canvas.create_rectangle(j*20,i*20,j*20+20,i*20+20,outline='grey',fill='grey')
                if tab[i][j]=="•":
                    canvas.create_rectangle(j*20,i*20,j*20+20,i*20+20,outline='grey',fill='grey')
                    canvas.create_oval(j*20,i*20,j*20+20,i*20+20,outline="red",fill="red")
                if tab[i][j]=="v":
                    canvas.create_rectangle(j*20,i*20,j*20+20,i*20+20,outline='yellow',fill='yellow')

def haut(event):
    global tab
    '''
    L'action de la fleche haut du clavier : il verifie si la case au dessus est vide et déplace le personnage
    Si la case ou atterie le pion est un "v" alors le programme s'arrete et affiche victoire
    '''
    Clic()
    position=trouve_position(tab)
    if tab[position[0]-1][position[1]]==" ":
        
        tab[position[0]][position[1]]=" "
        position[0]-=1
        tab[position[0]][position[1]]="•"
        couleur()
                    
    elif tab[position[0]-1][position[1]]=="v":
        print("victoire")
        root.destroy()
        return
        
    else:
        print("Aie, c'était un mur")
    

def bas(event):
    global tab
    '''
    L'action de la fleche bas du clavier : il verifie si la case en dessous est vide et déplace le personnage
    Si la case ou atterie le pion est un "v" alors le programme s'arrete et affiche victoire
    '''
    Clic()
    position=trouve_position(tab)
    if tab[position[0]+1][position[1]]==" ":

        
        tab[position[0]][position[1]]=" "
        position[0]+=1
        tab[position[0]][position[1]]="•"
        couleur()
        
    elif tab[position[0]+1][position[1]]=="v":
        print("victoire")
        root.destroy()
        return
        
    else:
        print("Aie, c'était un mur")

def gauche(event):
    global tab
    '''
    L'action de la fleche gauche du clavier : il verifie si la case a gauche est vide et déplace le personnage
    Si la case ou atterie le pion est un "v" alors le programme s'arrete et affiche victoire
    '''
    Clic()
    position=trouve_position(tab)
    if tab[position[0]][position[1]-1]==" ":

        
        tab[position[0]][position[1]]=" "
        position[1]-=1
        tab[position[0]][position[1]]="•"
        couleur()
        
    elif tab[position[0]][position[1]-1]=="v":
        print("victoire")
        root.destroy()
        return
        
    else:
        print("Aie, c'était un mur")

def droite(event):
    global tab
    '''
    L'action de la fleche droite du clavier : il verifie si la case a droite est vide et déplace le personnage
    Si la case ou atterie le pion est un "v" alors le programme s'arrete et affiche victoire
    '''
    Clic()
    position=trouve_position(tab)
    if tab[position[0]][position[1]+1]==" ":

        tab[position[0]][position[1]]=" "
        position[1]+=1
        tab[position[0]][position[1]]="•"
        couleur()
        
    elif tab[position[0]][position[1]+1]=="v":
        print("victoire")
        root.destroy()
        return
    else:
        print("Aie, c'était un mur")

def trouve_position(tab):
    '''
    Fonction renvoyant un tableau indiquant les coordonnées du personnage
    '''
    position=[]
    for i in range(len(tab)-1):
        for j in range(len(tab)-1):
            if tab[i][j]=="•":
                position=[i,j]
                break
    return position


def Clic():
    global canvas
    '''
    Fonction permettant d'actualiser la page a chaque avancer du personnage
    '''
    canvas.destroy()
    canvas=Canvas()
    couleur()
    canvas.pack()

'''Association de chaque bouton a une fonction'''
root.bind('<Up>',haut)
root.bind('<Right>',droite)
root.bind('<Left>',gauche)
root.bind('<Down>',bas)

'''Mise en couleur du canvas pour la première fois'''
couleur()

canvas.pack()


root.mainloop()