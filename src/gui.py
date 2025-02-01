import threading
import tkinter as tk
import flux_video

class gui:

    def __init__(self):

        self.racine = tk.Tk()
        self.racine.protocol("WM_DELETE_WINDOW", self.fermer_fenetre)
        self.racine.title("caméra")
        self.racine.geometry("1920x1080")

        self.flux = flux_video.Flux()

        self.cadre_camera = tk.Frame(self.racine, bd=0, background="#345eeb")
        self.cadre_camera.place(x=0, y=0, relwidth=1, relheight=0.9)
        self.label = tk.Label(self.cadre_camera, text="caca", font=("Courier", 12), justify='left')
        self.label.pack()

        self.cadre_boutons = tk.Frame(self.racine, bd=0, background="#cc1833")
        self.cadre_boutons.place(x=0, rely=0.9, relwidth=1, relheight=0.1)

        self.cadre_boutons.rowconfigure(0, weight=1, uniform='row')
        self.cadre_boutons.columnconfigure(0, weight=1, uniform='column')
        self.cadre_boutons.columnconfigure(1, weight=1, uniform='column')
        self.cadre_boutons.columnconfigure(2, weight=1, uniform='column')
        self.cadre_boutons.columnconfigure(3, weight=1, uniform='column')

        self.bouton_activer_camera = tk.Button(self.cadre_boutons, text="caméra", command=self.afficher_camera)
        self.bouton_activer_camera.grid(row=0, column=0)

    def lancer_flux(self):
        self.flux.lancer_flux(self.label)

    def afficher_camera(self):
        thread = threading.Thread(target=self.lancer_flux, daemon=True)
        thread.start()

    def fermer_fenetre(self):
        self.racine.destroy()
        self.flux.arreter_flux()



