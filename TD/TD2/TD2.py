import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry('600x600') 
fenetre.title("Mon dessin")

def couleur():
    couleur = input("Donner une couleur")

def fermer_fenetre() :
    fenetre.destroy()

def draw_target(canvas, 200, 200, 20, 5):
    for i in range(num_rings):
        if i % 2 == 0:
            color = "cyan"
        else:
            color = "white"
        canvas.create_oval(x - size * (i + 1), y - size * (i + 1), 
                           x + size * (i + 1), y + size * (i + 1), 
                           outline="black", fill=color)

def cercle():
    canvas.create_oval(100,100,10,10, width=2, fill="blue", outline="blue")

def carre():
    canvas.create_rectangle(100, 100, 30, 30, fill="red", outline="red")

def croix():
    canvas.create_line((150,160),(60,50), fill="yellow")
    canvas.create_line((50,60),(160,150), fill="yellow")
    
canvas = tk.Canvas(width=300, height=300, bg="black")
bouton_carre = tk.Button(fenetre, text="Carré", command=carre)
bouton_cercle = tk.Button(fenetre, text="Cercle", command=cercle)
bouton_croix = tk.Button(fenetre, text="Croix", command=croix)   
bouton_cible = tk.Button(fenetre, text="Cible", command=draw_target) 
bouton_quitter = tk.Button(fenetre, text="Fermer la fenêtre", command=fermer_fenetre)
bouton_couleurs = tk.Button(fenetre, text="Choisir une couleur", command=couleur)

canvas.grid(row=2, column=1, rowspan=4,  columnspan=1)
bouton_carre.grid(row=3,column=0)
bouton_cible(row=7, column=0)
bouton_cercle.grid(row=2,column=0)
bouton_croix.grid(row=4,column=0)
bouton_quitter.grid(row=5, column=0)
bouton_couleurs.grid(row=1, column=1)

fenetre.mainloop()