#colour file taken from https://github.com/codebrainz/color-names/blob/master/output/colors.csv
import csv

class Colour:
    def __init__(self, r, g, b, name):
        self.r = r
        self.g = g
        self.b = b
        self.name = name

    def __str__(self):
        return self.name + ", " + str(self.r) + ", " + str(self.g) + ", " + str(self.b)



def getRgbName(pxl):
    r, g, b = pxl[0], pxl[1], pxl[2]
    colourName = findClosestColourMatch(r, g, b)

    return colourName

def findClosestColourMatch(r, g, b):
    rgbValues = loadColourValues()
    curNearestColour = None
    curNearestColourDiff = None

    for colour in rgbValues:
        diffValue = 0
        diffValue += abs(r - colour.r)
        diffValue += abs(g - colour.g)
        diffValue += abs(b - colour.b)

        if curNearestColour == None or diffValue < curNearestColourDiff:
            curNearestColour = colour
            curNearestColourDiff = diffValue

    return curNearestColour.name

def loadColourValues():
    fileName = "colors.csv"
    colourList = []

    with open(fileName, newline='') as colourCsv:
        csvReader = csv.reader(colourCsv)

        for row in csvReader:
            newColour = Colour(int(row[3]), int(row[4]), int(row[5]), row[1])
            colourList.append(newColour)

    return colourList
