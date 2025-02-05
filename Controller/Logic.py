from Model import Helm # Import des Helmscripts vom Modelmodul
from Model import HelmBestand # Import des HelmBestandscript vom Modelmodul

groesse = ""
preis = ""
kategorie = ""
verschluss = ""
material = ""

HelmKategorien : str = ""
HelmSize = ""
HelmLock = ""
HelmMaterial = ""

ConfirmedHelmet = []

def generateHelmCategories():
    """
    Diese Methode generiert aus der Variabel Helmkategorien aus dem Helmscript
    einen String mit einer zahlen + Kategorie Auswahl. 
    """
    global HelmKategorien
    index = 0
    for helmKategorie in Helm.HelmKategorien:
        HelmKategorien += str(index) + f". {helmKategorie}\n"
        index += 1

def generateHelmSize():
    """
    Diese Methode generiert aus der Variabel HelmSize aus dem Helmscript
    einen String mit einer zahlen + Kategorie Auswahl. 
    """
    global HelmSize
    index = 0
    for helmSize in Helm.HelmSize:
        HelmSize += str(index) + f". {helmSize}\n"
        index += 1

def generateHelmLock():
    """
    Diese Methode generiert aus der Variabel HelmVerschluss aus dem Helmscript
    einen String mit einer zahlen + Kategorie Auswahl. 
    """
    global HelmLock
    index = 0
    for helmLock in Helm.HelmVerschluss:
        HelmLock += str(index) + f". {helmLock}\n"
        index += 1

def generateHelmMaterial():
    """
    Diese Methode generiert aus der Variabel HelmMaterial aus dem Helmscript
    einen String mit einer zahlen + Kategorie Auswahl. 
    """
    global HelmMaterial
    index = 0
    for helmMaterial in Helm.HelmMaterial:
        HelmMaterial += str(index) + f". {helmMaterial}\n"
        index += 1

def getHelmets():
    """
    Diese Methode checkt, ob ein Helm aus dem helme script aus dem Helmbestand modul 
    der Auswahl entspricht und fügt diese entsprechend der ConfirmedHelmet Liste zu
    """
    for key in HelmBestand.helme:
        helm = HelmBestand.helme[key]
        if helm.art == kategorie and helm.groesse == groesse and helm.material == material and helm.verschluss == verschluss and helm.preis <= preis and helm.warenbestand > 0:
            ConfirmedHelmet.append(key)

def generateStrings():
    """
    Diese Methode ist eine Sammelmethode um alle Methoden auf zu rufen, die Strings generieren.
    Eine Art Initialisierung
    """

    generateHelmCategories()
    generateHelmLock()
    generateHelmMaterial()
    generateHelmSize()

