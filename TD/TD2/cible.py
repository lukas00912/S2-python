import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("600x600")
fenetre.title("Mon dessin")


def fermer_fenetre():
    fenetre.destroy()


def cercle():
    canvas.create_oval(1000, 1000, 50, 50, width=2, outline="blue")


canvas = tk.Canvas(width=300, height=300, bg="black")
bouton_quitter = tk.Button(fenetre, text="Fermer la fenêtre", command=fermer_fenetre)
bouton_cercle = tk.Button(fenetre, text="Cercle", command=cercle)


canvas.grid(row=2, column=1, rowspan=4, columnspan=1)
bouton_quitter.grid(row=5, column=0)
bouton_cercle.grid(row=2, column=0)


fenetre.mainloop()
