import threading
import tkinter as tk
import flux_video

class gui:

    def __init__(self):

        self.racine = tk.Tk()
        self.racine.title("caméra")
        self.racine.geometry("1920x1080")
        self.label = None

        self.cadre_camera = tk.Frame(self.racine, bd=0, background="#345eeb")
        self.cadre_camera.place(x=0, y=0, relwidth=1, relheight=0.8)

        self.cadre_boutons = tk.Frame(self.racine, bd=0, background="#cc1833")
        self.cadre_boutons.place(x=0, rely=0.8, relwidth=1, relheight=0.2)

        self.cadre_boutons.rowconfigure(0, weight=1, uniform='row')
        self.cadre_boutons.columnconfigure(0, weight=1, uniform='column')
        self.cadre_boutons.columnconfigure(1, weight=1, uniform='column')
        self.cadre_boutons.columnconfigure(2, weight=1, uniform='column')
        self.cadre_boutons.columnconfigure(3, weight=1, uniform='column')

        self.afficher_check_var = tk.IntVar()
        self.bouton_activer_camera = tk.Checkbutton(self.cadre_boutons, text="caméra", variable=self.afficher_check_var, onvalue=1, offvalue=0)
        self.bouton_activer_camera.grid(row=0, column=0)

        self.thread = None
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=flux_video.Flux.lancer_flux(self.cadre_camera, self.label, self.racine), args=())
        self.thread.start()





