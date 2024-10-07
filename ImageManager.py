import tkinter as tk
from PIL import Image
import Identifier

def waitForClickedPixel(fileName, path):
    window = tk.Tk()
    fileName = checkForPng(fileName, path)
    photo = tk.PhotoImage(file=fileName)
    img = tk.Label(window, image=photo)
    img.pack()
    window.bind("<Button-1>", lambda event: imageClicked(event, fileName))
    window.resizable(False, False)

    window.mainloop()

def imageClicked(event, fileName):
    pxl = getPixelRGB(event.x, event.y, fileName)
    colourName = Identifier.getRgbName(pxl)

    #print(colourName)
    tk.messagebox.showinfo("Colour indentified", colourName)

def getPixelRGB(x, y, fileName):
    img = Image.open(fileName).convert("RGB")
    pixels = img.load()

    return pixels[x, y]

#converts to png if necessary as tkinter doesn't like non-pngs
def checkForPng(fileName, path):
    if fileName.endswith(".png"):
        return fileName
    else:
        img = Image.open(fileName)
        newPath = path + "tempImg.png"
        img.save(newPath)

        return newPath
