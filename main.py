from Controller import Logic
from View import View

"""
Dieses Script ist der Entrypoint. Es startet alles Methoden nach und nach
um ein Ablauf zu gewährleisten
"""

Logic.generateStrings()
View.getInput()
Logic.getHelmets()
View.printHelmet()



