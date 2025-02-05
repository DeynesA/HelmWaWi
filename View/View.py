from Controller import Logic
from Model import Helm


def getInput():
    """
    Diese Methode nimmt den input entgegen und weist diese Werte (Eingaben) entsprechend den Variabeln in der
    Logic.py zu
    """
    kategorieAuswahl = input(f"Wähle bitte eine Helmkategorie. Zur Auswahl stehen:\n{Logic.HelmKategorien}")
    Logic.kategorie = Helm.HelmKategorien[int(kategorieAuswahl)]
    groesseAuswahl = input(f"Wähle bitte eine Helmgröße. Zur Auswahl stehen:\n{Logic.HelmSize}")
    Logic.groesse = Helm.HelmSize[int(groesseAuswahl)]
    materialAuswahl = input(f"Wähle bitte ein Helmmaterial. Zur Auswahl stehen:\n{Logic.HelmMaterial}")
    Logic.material = Helm.HelmMaterial[int(materialAuswahl)]
    verschlussAuswahl = input(f"Wähle bitte einen Helmverschluss. Zur Auswahl stehen:\n{Logic.HelmLock}")
    Logic.verschluss = Helm.HelmVerschluss[int(verschlussAuswahl)]
    Logic.preis = int(input(f"Wähle bitte einen Maximalpreis.\n"))


def printHelmet():
    """
    Diese Methode gibt die gefundenen Helme aus der Logic.py Datei aus der Variabel ConfirmedHelmets aus
    """

    Logic.extractedHelmets = ", ".join(Logic.ConfirmedHelmet)
    print(f"Diese Helme: {Logic.extractedHelmets} stehen zur Auswahl")


