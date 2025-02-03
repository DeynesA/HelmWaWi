from Controller import Logic
from Model import HelmBestand

def Start():
    """Diese Methode stößt den Installationsablauf an."""
    while True:
        displayMenu()
        if not weiterMachen():
            break

def displayMenu():
    """Diese Methode zeigt das Menü im Terminal an und fordert den Benutzer zur Eingabe auf."""
    print("Willkommen zur Helm-Auswahl!")
    list_criteria()
    print("Bitte gib die Suchkriterien für deinen Helm ein.")
    benutzerEingabe()

def benutzerEingabe():
    """Fordert zur Eingabe der Suchkriterien auf und ermöglicht die Auswahl eines Helms anhand der Nummer."""
    try:
        arten, preise, materialien, groessen, verschluesse = get_criteria()

        print("Arten:")
        for index, art in enumerate(arten):
            print(f"{index + 1}. {art}")
        art_index = input("Art (Nummer eingeben oder leer lassen für keine Einschränkung): ")
        art = list(arten)[int(art_index) - 1] if art_index else None

        preis = input(f"Maximaler Preis (Max: {max(preise)}, oder leer lassen für keine Einschränkung): ")
        preis = int(preis) if preis else None

        print("Materialien:")
        for material in materialien:
            print(material)
        material = input("Material (Nummer eingeben oder leer lassen für keine Einschränkung): ") or None

        print("Größen:")
        for groesse in groessen:
            print(groesse)
        groesse = input("Größe (Nummer eingeben oder leer lassen für keine Einschränkung): ") or None

        print("Verschlüsse:")
        for verschluss in verschluesse:
            print(verschluss)
        verschluss = input("Verschluss (Nummer eingeben oder leer lassen für keine Einschränkung): ") or None

        gefundene_helme = Logic.suche_helme(preis, material, groesse, art, verschluss)
        if gefundene_helme:
            print("\nGefundene Helme:")
            for index, helm in enumerate(gefundene_helme):
                print(f"{index}. {helm}")

            auswahl = int(input("\nBitte wähle einen Helm anhand der Nummer aus: "))
            if 0 <= auswahl < len(gefundene_helme):
                ausgewaehlter_helm = gefundene_helme[auswahl]
                print(f"\nDu hast den Helm ausgewählt: {ausgewaehlter_helm}")
            else:
                print("\nUngültige Auswahl. Bitte versuche es erneut.")
                benutzerEingabe()
        else:
            print("\nKeine Helme gefunden, die den Kriterien entsprechen.")
    except ValueError:
        print("\nUngültige Eingabe! Bitte geben Sie eine gültige Zahl ein.")
        benutzerEingabe()

def weiterMachen():
    """Fragt den Benutzer, ob er eine weitere Suche durchführen möchte."""
    antwort = input("Möchtest du eine weitere Suche durchführen? (J/N): ").strip().lower()
    return antwort == 'j'

def generateHelmSite():
    """Generiert eine Liste von Helmseiten und gibt sie aus."""
    index = 0
    helm_sites = ""
    for helm_name, helm in HelmBestand.helme.items():
        helm_sites += f"{index}. {helm_name}: {helm}\n"
        index += 1
    return helm_sites

def list_criteria():
    """Listet die verfügbaren Kriterien für die Helmsuche auf."""
    arten, preise, materialien, groessen, verschluesse = get_criteria()

def get_criteria():
    """Ermittelt die verfügbaren Kriterien für die Helmsuche."""
    arten = set()
    preise = set()
    materialien = set()
    groessen = set()
    verschluesse = set()

    for helm in HelmBestand.helme.values():
        arten.add(helm.art)
        preise.add(helm.preis)
        materialien.add(helm.material)
        groessen.add(helm.groesse)
        verschluesse.add(helm.verschluss)

    return arten, preise, materialien, groessen, verschluesse

if __name__ == "__main__":
    list_criteria()
    Start()
    print(generateHelmSite())
    """ Der Codeblock wird nur ausgeführt, wenn das Skript direkt ausgeführt wird. Dies verhindert, 
    dass der Code ausgeführt wird, wenn das Skript als Modul importiert wird, was unerwünschte Nebenwirkungen vermeiden kann."""