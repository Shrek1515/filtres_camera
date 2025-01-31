import math
import threading
import cv2 as cv
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np
from numba import jit

@jit(nopython=True)
def vers_ascii(img):

    ascii_chars = [
        ' ', '.', ',', ':', ';', "'", '"', '`', '^', '-',
        '_', '=', '+', '|', '\\', '/', '?', '!', '~', '<',
        '>', '(', ')', '[', ']', '{', '}', '*', '&', '%',
        '$', '#', '@', '0', '1', '2', '3', '4', '5', '6',
        '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
        'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z', '°', '§', 'µ', '¶', '·',
        '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á',
        'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë',
        'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ',
        'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß',
        'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é',
        'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó',
        'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý',
        'þ', 'ÿ'
    ]

    #ascii2 =  "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"


    #ascii_chars.reverse()

    text = ""

    img_size = img.shape
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            text += ascii_chars[int(img[i,j])]
        text += "\n"

    return text

class Flux:

    def __init__(self):
        self.cap = cv.VideoCapture(0)
        self.racine = tk.Tk()
        self.racine.geometry("1920x1080")
        self.panel = None
        self.thread = None
        self.ret = None
        self.frame = None
        self.plan = None

        self.path = "/home/shrek/Documents/Perso/PythonProjetsPerso/projetrecovisage/.venv/lib/python3.11/site-packages/cv2/data/"
        self.face_cascade = cv.CascadeClassifier(self.path + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv.CascadeClassifier(self.path + 'haarcascade_eye.xml')

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.lancer_flux, args=())
        self.thread.start()


    def lancer_flux(self):
        while True:
            self.ret, self.frame = self.cap.read()

            if not self.ret:
                print("Erreur lors de la lecture du flux vidéo.")
                break

            face_rects = self.face_cascade.detectMultiScale(self.frame, scaleFactor=1.2, minNeighbors=3)
            #for (x, y, w, h) in face_rects:
            #    cv.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            #img = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)
            img = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)

            #img = img.astype(np.uint8)
            #img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


            img = Image.fromarray(img)

            coef = 5
            nouvelle_taille = (math.floor(img.width / coef), math.floor(img.height / coef))
            img = img.resize(nouvelle_taille)

            grayscale_array = np.array(img)
            img = (grayscale_array / 255.0 * 127).astype(np.uint8)
            #img = Image.fromarray(normalized_array, mode='L')

            text = vers_ascii(img)
            #img = ImageTk.PhotoImage(img)

            if self.panel is None:
                self.panel = tk.Label(self.racine, text=text, font=("Courier", 12), justify='left')
                self.panel.pack()

            else:
                self.panel.configure(text=text)
                #self.panel.image = img

            #cv.imshow('frame', self.frame)

            if cv.waitKey(1) == ord('q'):
                break

        self.racine.quit()
        self.cap.release()
        cv.destroyAllWindows()