import webbrowser
import os


f = open("../../../work/identify/result", "r")

full=True

for line in f:
    if line.find("car") != -1 or line.find("van") != -1:
        print ("find a car")
    else:
        print ("empty!!")
        full = False



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if full == False:
    webbrowser.open('file://' + os.path.join(BASE_DIR, 'map_empty.html'))
else:
    webbrowser.open('file://' + os.path.join(BASE_DIR, 'map_full.html'))



