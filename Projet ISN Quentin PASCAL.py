from tkinter import *
import time
from random import randrange

mots_a_trouver = ['Chien', 'Bouteille', 'Pharaon', 'Singe', 'Stylo']

#Variables de Pent
b1 = "up"
b2 = "up"
xold, yold = None, None
ptsNoirs = []

## Paramètres de la fenêtre
largeur = 400
hauteur = 600
numero_mot = 0

## Variable mot secret
mot_secret = mots_a_trouver[randrange(len(mots_a_trouver))]

def envoi(event):
    global mot, numero_mot, mot_secret
    if event.keysym == 'Return': ##Pour un événement de type KeyPress ou KeyRelease impliquant une touche spéciale
        mot = text.get()
        ## Victoire
        if mot == mot_secret:
            print('Gagné')
            mot_secret = mots_a_trouver[randrange(len(mots_a_trouver))]
            label.config(text=mot_secret)
            drawing_area.delete(ALL)
        mots.append(mot)
        chat.insert(END, username+' : ' + mots[numero_mot])
        numero_mot = numero_mot+1
        texte.delete(0,END)
        chat.insert(END,'\n\n') 

def Pent(): # module de dessin(
        global drawing_area
        def b1On(event):
            global b1
            b1 = "On"           #Reconnaissance du clic gauche de la souris

        def b2On(event):
            global b2
            b2 = "On"
                                

        def b1Off(event):
            global b1, xold, yold
            b1 = "Off"               #reintialise la ligne quand on arrête d'appuyer
            xold = None           
            yold = None

        def b2Off(event):
            global b2, xold, yold
            b2 = "up"               
            xold = None
            yold = None

        def motion(event):
            global xold, yold, cote
            if b1 == "On":
                if xold is not None and yold is not None:
                    event.widget.create_line(xold,yold,event.x,event.y,fill="black",smooth=TRUE, capstyle=ROUND, splinesteps=36, width=5, tags='noir')
                                    #Création du brush
                    ptsNoirs.append((event.x,event.y))
                    #print(ptsNoirs)

                xold = event.x
                yold = event.y
                
            if b2 == "On":
                if xold is not None and yold is not None:
                    event.widget.create_line(xold,yold,event.x,event.y,fill="white",smooth=TRUE,width=10, capstyle=ROUND, splinesteps=36)
                                    #création de la gomme
                xold = event.x
                yold = event.y

        root = Tk()
        drawing_area = Canvas(root, bg = 'white', width=800, height=600)
        drawing_area.pack()
        drawing_area.bind("<Motion>", motion)
        drawing_area.bind("<ButtonPress-1>", b1On)
        drawing_area.bind("<ButtonRelease-1>", b1Off)
        drawing_area.bind("<ButtonPress-3>", b2On)
        drawing_area.bind("<ButtonRelease-3>", b2Off)
        #root.mainloop()

    
##Création de la liste pour stocker les textes
mots=[]


## Paramètres de la fenêtre
largeur = 400
hauteur = 600
numero_mot = 0
mot = ''

## Création de la fenêtre
fenetre = Tk()
username = 'Moi'## Nom variable

main = Canvas(fenetre, width = largeur, height = hauteur)
main.grid()
        
## Création du fond blanc
base = main.create_rectangle(0,0,largeur+3,hauteur, fill = 'white') 
## Création de la ligne entre la zone de saisie de texte et l'espace d'affichage
zone_de_texte = main.create_rectangle(0,hauteur-(hauteur-500),largeur,hauteur-(hauteur-505), fill = 'black')

########### Scrollbar

## Fonction d'écriture

text = StringVar()
## while espace_ligne <= 400: 
chat = Text(width = 40, height = 30) ##Affichage dans le chat
chat.place(x='5',y='10')

scrollbar = Scrollbar(fenetre)
scrollbar.grid(row=0, column=1, sticky='ns')

chat.config(yscrollcommand = scrollbar.set)

scrollbar.config( command = chat.yview )

texte = Entry(fenetre, textvariable=text)    ##Affichage zone de saisie
texte.place(x='5',y='510')

      


###########
fenetre.bind("<Return>", envoi)###### Appel de la fonction affichage
###########

##
Pent()
##
## En-tête du jeu
En_tete = Tk()

label = Label(En_tete, text=mot_secret, bg="white")
label.pack()
