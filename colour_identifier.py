import FileManager
import ImageManager
from pathlib import Path
import os
import shutil

def startColourIdentifier():
    path = os.path.dirname(os.path.realpath(__file__)) + "/temp/"
    setup(path)
    fileName = FileManager.getFileName()
    pxl = ImageManager.waitForClickedPixel(fileName, path)
    cleanup(path)

def setup(path):
    Path(path).mkdir(exist_ok=True)

def cleanup(path):
    shutil.rmtree(path)

startColourIdentifier()
