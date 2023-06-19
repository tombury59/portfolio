
from tkinter import *
from tkinter.filedialog import *

fenetre = Tk()
fenetre.title('Morpion')


tab=[[0,0,0],
     [0,0,0],
     [0,0,0]]
texte1 = Label(fenetre, text = "")


#|----------------------------------------------------|#
#croix#
def callback(event):
    global tab
    
    
    #diagonal gauche --> droite
    if event.x<100 and event.y<100 :
        croix(50,50)
        tab[0][0]=2
        victoire()
        
        
    elif event.x<200 and event.y<200 and event.x>100 and event.y>100:
        croix(150,150)
        tab[1][1]=2
        victoire()
        
        
    elif event.x<300 and event.y<300 and event.x>200 and event.y>200:
        croix(250,250)
        tab[2][2]=2
        victoire()
        
        
    #reste diagonal droite --> gauche
        
    elif event.x>200 and event.y<100 and event.x<300:
        croix(250,50)
        tab[0][2]=2
        victoire()
        
    elif event.x<100 and event.y<300 and event.y>200:
        croix(50,250)
        tab[2][0]=2
        victoire()
    
        
    #reste
        
    elif event.y>100 and event.y<200 and event.x>0 and event.x<100:
        croix(50,150)
        tab[1][0]=2
        victoire()
        
    elif event.x>100 and event.y<100 and event.x<200:
        croix(150,50)
        tab[0][1]=2
        victoire()
        
        
    elif event.y>100 and event.y<300 and event.x<300 and event.x>200:
        croix(250,150)
        tab[1][2]=2
        victoire()
        
       
    elif event.y>200 and event.y<300 and event.x>100 and event.x<200:
        croix(150,250)
        tab[2][1]=2
        victoire()
    #print( ("Rond", event.x, event.y),croix(event.x,event.y))
    
    
    
#cercle#
def callback2(event):
    global tab
    
    #diagonal gauche --> droite
    
    
    if event.x<100 and event.y<100 :
        rond(50,50)
        tab[0][0]=1
        victoire()
        
        
    elif event.x<200 and event.y<200 and event.x>100 and event.y>100:
        rond(150,150)
        tab[1][1]=1
        victoire()
        
    elif event.x<300 and event.y<300 and event.x>200 and event.y>200:
        rond(250,250)
        tab[2][2]=1
        victoire()
        
        
    #reste diagonal droite --> gauche
        
    elif event.x>200 and event.y<100 and event.x<300:
        rond(250,50)
        tab[0][2]=1
        victoire()
        
    elif event.x<100 and event.y<300 and event.y>200:
        rond(50,250)
        tab[2][0]=1
        victoire()
    
    #reste
        
    elif event.y>100 and event.y<200 and event.x>0 and event.x<100:
        rond(50,150)
        tab[1][0]=1
        victoire()
       
    elif event.x>100 and event.y<100 and event.x<200:
        rond(150,50)
        tab[0][1]=1
        victoire()
    
    elif event.y>100 and event.y<300 and event.x<300 and event.x>200:
        rond(250,150)
        tab[1][2]=1
        victoire()
    
    elif event.y>200 and event.y<300 and event.x>100 and event.x<200:
        rond(150,250)
        tab[2][1]=1
        victoire()
        
        
#|----------------------------------------------------|#
    
def rond(x,y):
    canvas.create_oval(x-35,y-35,x+35,y+35,outline='red')

def croix(x,y):
    canvas.create_line(x-30,y-30,x+30,y+30,fill = "blue")
    canvas.create_line(x-30,y+30,x+30,y-30,fill = "blue")
    
def victoire():
    global tab

#Joueur 2
    #toute les lignes -- 
    if [1,1,1] in tab:
        texte1.config(text="VICTOIRE DU JOUEUR 2")
        
    #toute les colonnes |
    if tab[0][0] == 1 and tab[1][0] == 1 and tab[2][0] == 1:
        texte1.config(text="VICTOIRE DU JOUEUR 2")
    if tab[0][1] == 1 and tab[1][1] == 1 and tab[2][1] == 1:
        texte1.config(text="VICTOIRE DU JOUEUR 2")
    if tab[0][2] == 1 and tab[1][2] == 1 and tab[2][2] == 1:
        texte1.config(text="VICTOIRE DU JOUEUR 2")
    
    #toute les diago
    if tab[0][0] == 1 and tab[1][1] == 1 and tab[2][2] == 1:
        texte1.config(text="VICTOIRE DU JOUEUR 2")
    if tab[0][2] == 1 and tab[1][1] == 1 and tab[2][0] == 1:
        texte1.config(text="VICTOIRE DU JOUEUR 2")
#----------------------------------------------------------------#        

#Joueur 1
    #toute les lignes -- 
    if [2,2,2] in tab:
        texte1.config(text="VICTOIRE DU JOUEUR 1")
        
    #toute les colonnes |
    if tab[0][0] == 2 and tab[1][0] == 2 and tab[2][0] == 2:
        texte1.config(text="VICTOIRE DU JOUEUR 1")
    if tab[0][1] == 2 and tab[1][1] == 2 and tab[2][1] == 2:
        texte1.config(text="VICTOIRE DU JOUEUR 1")
    if tab[0][2] == 2 and tab[1][2] == 2 and tab[2][2] == 2:
        texte1.config(text="VICTOIRE DU JOUEUR 1")
    
    #toute les diago
    if tab[0][0] == 2 and tab[1][1] == 2 and tab[2][2] == 2:
        texte1.config(text="VICTOIRE DU JOUEUR 1")
    if tab[0][2] == 2 and tab[1][1] == 2 and tab[2][0] == 2:
        texte1.config(text="VICTOIRE DU JOUEUR 1")
    


#a=texte1.config(text="VICTOIRE DU JOUEUR 2")
#b=texte1.config(text="VICTOIRE DU JOUEUR 1")
def reset():
    texte1.config(text="")
    canvas.create_rectangle(0, 0, 300, 300, fill='white')
    
    
    canvas.create_line(0, 100, 300, 100, width=2)

    canvas.create_line(0, 200, 300, 200, width=2)

    canvas.create_line(100, 0, 100, 300, width=2)

    canvas.create_line(200, 0, 200, 300, width=2)
    
    for i in range(3):
        for j in range(3):
            tab[i][j]=0
            
def affiche_victoire():
    texte1.config(text="FIN DE LA PARTIE")

#|----------------------------------------------------|#


canvas = Canvas(fenetre, width=300, height=300, background='white')


canvas.create_line(0, 100, 300, 100, width=2)

canvas.create_line(0, 200, 300, 200, width=2)

canvas.create_line(100, 0, 100, 300, width=2)

canvas.create_line(200, 0, 200, 300, width=2)


canvas.bind("<Button-1>", callback)
canvas.bind("<Button-3>", callback2)

# if canvas.bind("<Button-1>")<100:
#     print("cc")
# if canvas.bind("<Button-1>")<100:
#    print("salu")

#|----------------------------------------------------|#



Button(fenetre, text ='Reset' ,font=('Cartoon',10),fg='black',width=20,command=reset) .pack ( padx=5, pady=5)

texte1.pack()
canvas.pack()
fenetre.mainloop()