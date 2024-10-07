import tkinter as tk
import tkinter.filedialog

def getFileName():
    #path = input("Please enter file name:")

    root = tk.Tk()
    root.withdraw()
    path = tk.filedialog.askopenfilename()
    if len(path) == 0: #no file chosen
        exit()
    root.destroy()

    return path
