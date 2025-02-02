from Model import HelmBestand
from Controller import Logic

def Start():
    """Diese Methode stößt den Installationsablauf an."""
    displayMenu()

def displayMenu():
    """Diese Methode zeigt das Menü im Terminal an und fordert den Benutzer zur Eingabe auf."""
    print("Willkommen zur Helm-Auswahl!")
    print("Bitte gib die Suchkriterien für deinli Helm ein.")
    benutzerEingabe()

def benutzerEingabe():
    """Fordert zur Eingabe der Suchkriterien auf."""
    try:
        preis = input("Maximaler Preis (z.B. max.275, oder leer lassen für keine Einschränkung): ")
        preis = int(preis) if preis else None
        material = input("Material (z.B. Carbon, leer lassen für keine Einschränkung): ") or None
        groesse = input("Größe (z.B. L, leer lassen für keine Einschränkung): ") or None
        art = input("Art (z.B. Integralhelm, leer lassen für keine Einschränkung): ") or None
        verschluss = input("Verschluss (z.B. Doppel-D, leer lassen für keine Einschränkung): ") or None

        gefundene_helme = Logic.suche_helme(preis, material, groesse, art, verschluss)
        if gefundene_helme:
            print("Gefundene Helme:")
            for helm in gefundene_helme:
                helm_info = (f"{helm.name}, Größe: {helm.groesse}, Warenbestand: {helm.warenbestand}, "
                             f"Preis: {helm.preis}€, Art: {helm.art}, Verschluss: {helm.verschluss}, "
                             f"Material: {helm.material}")
                print(helm_info)
        else:
            print("Keine Helme gefunden, die den Kriterien entsprechen.")
    except ValueError:
        print("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl für den Preis ein.")
        benutzerEingabe()
        
if __name__ == "__main__":
    Start()
    """ Der Codeblock nur ausgeführt wird, wenn das Skript direkt ausgeführt wird. Dies verhindert, 
dass der Code ausgeführt wird, wenn das Skript als Modul importiert wird, was unerwünschte Nebenwirkungen vermeiden kann."""