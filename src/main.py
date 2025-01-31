"""import cv2 as cv
import tkinter as tk
from PIL import Image, ImageTk

path = "/home/shrek/Documents/Perso/PythonProjetsPerso/projetrecovisage/.venv/lib/python3.11/site-packages/cv2/data/"
face_cascade = cv.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(path + 'haarcascade_eye.xml')

cap = cv.VideoCapture(0)
racine = tk.Tk()
racine.geometry("1600x900")
cadre_image = tk.Frame(racine, bd=0, highlightthickness=0, background="#fe8e36")
cadre_image.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
canvas = tk.Canvas(cadre_image)
canvas.place(relx=0.5, rely=0.5, anchor="center")
racine.mainloop()

while True:
    _, frame = cap.read()
    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=3)

    for (x,y,w,h) in face_rects:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    #cv.imshow('frame', frame)
    canvas.create_image(
        0,0,image=ImageTk.PhotoImage(
            Image.fromarray(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
        )
    )

    if cv.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv.destroyAllWindows()"""

import flux_video

test = flux_video.Flux()
test.racine.mainloop()
