from random import *
from tkinter import *
import time

#canvas.create_text (200,200,text='cc')
#pierre  =canvas.create_line(0, 200, 200, 300,fill='black',width=1)
#feuille =canvas.create_line(0, 0, 300, 300,fill='black',width=1)
#ciseau  =canvas.create_line(0, 100, 400, 300,fill='black',width=1)



#idéé : crée deux carré blanc pour reset lorsqu'on appui sur un bouton

fenetre = Tk()
fenetre.title('DUEL')

def random_bot():
   a=randint(1,3)

   if a==1:
       b='Pierre'

   if a==2:
       b='Feuille'

   if a==3:
       b='Ciseau'

   return b


def pierre():
    
    canvas.create_rectangle(0, 0, 400, 400, fill='grey')
    
    fills=''

    nb_bot=random_bot()

    if nb_bot=='Pierre':
        fills='red'
    if nb_bot=='Feuille':
        fills='green'
    if nb_bot=='Ciseau':
        fills='blue'

    canvas.create_text (300,200,text='Pierre',fill='red',font=("Arial", 18))
    
    
    time.sleep(0.5)
    
    canvas.create_text (100,200,text=nb_bot,fill=fills,font=("Arial", 18))
    
    if nb_bot=='Pierre':
        canvas.create_text (200,100,text='Egalité',fill='black',font=("Courier", 40))
    if nb_bot=='Feuille':
        canvas.create_text (200,100,text='PERDU',fill='black',font=("Courier", 40))
    if nb_bot=='Ciseau':
        canvas.create_text (200,100,text='GAGNE',fill='black',font=("Courier", 40))

    
    #nb_bot.set("")


def feuille():
    
    canvas.create_rectangle(0, 0, 400, 400, fill='grey')
    
    fills=''
    
    nb_bot=random_bot()

    if nb_bot=='Pierre':
        fills='red'
    if nb_bot=='Feuille':
        fills='green'
    if nb_bot=='Ciseau':
        fills='blue'

    canvas.create_text (300,200,text='Feuille',fill='green',font=("Arial", 18))
    
    
    time.sleep(0.5)

    
    canvas.create_text (100,200,text=nb_bot,fill=fills,font=("Arial", 18))

    if nb_bot=='Pierre':
        canvas.create_text (200,100,text='GAGNE',fill='black',font=("Courier", 40))
    if nb_bot=='Feuille':
        canvas.create_text (200,100,text='Egalité',fill='black',font=("Courier", 40))
    if nb_bot=='Ciseau':
        canvas.create_text (200,100,text='PERDU',fill='black',font=("Courier", 40))
     
     
     
     
     
     
def ciseau():
    
    canvas.create_rectangle(0, 0, 400, 400, fill='grey')
    
    
    fills=''
    
    nb_bot=random_bot()

    if nb_bot=='Pierre':
        fills='red'
    if nb_bot=='Feuille':
        fills='green'
    if nb_bot=='Ciseau':
        fills='blue'

    canvas.create_text (300,200,text='Ciseau',fill='blue',font=("Arial", 18))
    
    
    time.sleep(0.5)
    
    canvas.create_text (100,200,text=nb_bot,fill=fills,font=("Arial", 18))

    if nb_bot=='Pierre':
        canvas.create_text (200,100,text='PERDU',fill='black',font=("Courier", 40))
    if nb_bot=='Feuille':
        canvas.create_text (200,100,text='GAGNE',fill='black',font=("Courier", 40))
    if nb_bot=='Ciseau':
        canvas.create_text (200,100,text='Egalité',fill='black',font=("Courier", 40))


    #canvas.create_rectangle(100, 100, 300, 300, fill='white')





Button(fenetre, text ='Pierre' ,font=('Cartoon',20),fg='Red',width=20,command=pierre) .pack ( padx=5, pady=5)
Button(fenetre, text ='Feuille',font=('Cartoon',20),fg='Green',width=20,command=feuille) .pack ( padx=5, pady=5)
Button(fenetre, text ='Ciseau' ,font=('Cartoon',20),fg='Blue',width=20,command=ciseau) .pack ( padx=5, pady=5)

label = Label(fenetre, text='Ordinateur                                                  Vous')

canvas = Canvas(fenetre, width=400, height=400, background='grey')




#LigneSepare = canvas.create_line(200, 0, 200, 400,fill='gray',width=1)

label.pack()
canvas.pack()
fenetre.mainloop()
