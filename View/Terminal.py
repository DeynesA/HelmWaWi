from Controller import Logic
from Model import HelmBestand

def Start():
    """Diese Methode stößt den Installationsablauf an."""
    while True:
        displayMenu()  # Zeigt das Menü an.
        if not weiterMachen():  # Fragt, ob du weitermachen möchtest.
            break  # Beendet die Schleife, wenn du nicht weitermachen möchtest.

def displayMenu():
    """Diese Methode zeigt das Menü im Terminal an und fordert dich zur Eingabe auf."""
    print("Willkommen zur Helm-Auswahl!")
    list_criteria()  # Zeigt die Suchkriterien an.
    print("Bitte gib die Suchkriterien für deinen Helm ein.")
    benutzerEingabe()  # Fordert dich zur Eingabe auf.

def benutzerEingabe():
    """Fordert zur Eingabe der Suchkriterien auf und ermöglicht die Auswahl eines Helms anhand der Nummer."""
    try:
        arten, preise, materialien, groessen, verschluesse = get_criteria()  # Holt die Suchkriterien.

        print("Arten:")
        for index, art in enumerate(arten):  # Zeigt die Arten an.
            print(f"{index + 1}. {art}")
        art_index = input("Art (Nummer eingeben oder leer lassen für keine Einschränkung): ")
        art = list(arten)[int(art_index) - 1] if art_index else None  # Wählt die Art aus.

        preis = input(f"Maximaler Preis (Max: {max(preise)}, oder leer lassen für keine Einschränkung): ")
        preis = int(preis) if preis else None  # Wählt den Preis aus.

        print("Materialien:")
        for index, material in enumerate(materialien):  # Zeigt die Materialien an.
            print(f"{index + 1}. {material}")
        material_index = input("Material (Nummer eingeben oder leer lassen für keine Einschränkung): ")
        material = list(materialien)[int(material_index) - 1] if material_index else None  # Wählt das Material aus.

        print("Größen:")
        for index, groesse in enumerate(groessen):  # Zeigt die Größen an.
            print(f"{index + 1}. {groesse}")
        groesse_index = input("Größe (Nummer eingeben oder leer lassen für keine Einschränkung): ")
        groesse = list(groessen)[int(groesse_index) - 1] if groesse_index else None  # Wählt die Größe aus.

        print("Verschlüsse:")
        for index, verschluss in enumerate(verschluesse):  # Zeigt die Verschlüsse an.
            print(f"{index + 1}. {verschluss}")
        verschluss_index = input("Verschluss (Nummer eingeben oder leer lassen für keine Einschränkung): ")
        verschluss = list(verschluesse)[int(verschluss_index) - 1] if verschluss_index else None  # Wählt den Verschluss aus.

        gefundene_helme = Logic.suche_helme(preis, material, groesse, art, verschluss)  # Sucht Helme nach den Kriterien.
        if gefundene_helme:
            print("\nGefundene Helme:")
            for index, helm in enumerate(gefundene_helme):  # Zeigt die gefundenen Helme an.
                print(f"{index}. {helm}")

            auswahl = int(input("\nBitte wähle einen Helm anhand der Nummer aus: "))
            if 0 <= auswahl < len(gefundene_helme):  # Prüft, ob die Auswahl gültig ist.
                ausgewaehlter_helm = gefundene_helme[auswahl]
                print(f"\nDu hast den Helm ausgewählt: {ausgewaehlter_helm}")
            else:
                print("\nUngültige Auswahl. Bitte versuche es erneut.")
                benutzerEingabe()  # Fordert zur erneuten Eingabe auf.
        else:
            print("\nKeine Helme gefunden, die den Kriterien entsprechen.")
    except ValueError:
        print("\nUngültige Eingabe! Bitte gib eine gültige Zahl ein.")
        benutzerEingabe()  # Fordert zur erneuten Eingabe auf.

def weiterMachen():
    """Fragt, ob du eine weitere Suche durchführen möchtest."""
    antwort = input("Möchtest du eine weitere Suche durchführen? (J/N): ").strip().lower()
    return antwort == 'j'  # Gibt True zurück, wenn du 'j' eingibst.

def generateHelmSite():
    """Generiert eine Liste von Helmen und gibt sie aus."""
    index = 0
    helm_sites = ""
    for helm_name, helm in HelmBestand.helme.items():  # Geht alle Helme durch.
        helm_sites += f"{index}. {helm_name}: {helm}\n"  # Fügt den Helm zur Liste hinzu.
        index += 1
    return helm_sites  # Gibt die Liste zurück.

def list_criteria():
    """Listet die verfügbaren Kriterien für die Helmsuche auf."""
    arten, preise, materialien, groessen, verschluesse = get_criteria()  # Holt die Suchkriterien.

def get_criteria():
    """Ermittelt die verfügbaren Kriterien für die Helmsuche."""
    arten = set()
    preise = set()
    materialien = set()
    groessen = set()
    verschluesse = set()

    for helm in HelmBestand.helme.values():  # Geht alle Helme durch.
        arten.add(helm.art)  # Fügt die Art hinzu.
        preise.add(helm.preis)  # Fügt den Preis hinzu.
        materialien.add(helm.material)  # Fügt das Material hinzu.
        groessen.add(helm.groesse)  # Fügt die Größe hinzu.
        verschluesse.add(helm.verschluss)  # Fügt den Verschluss hinzu.

    return arten, preise, materialien, groessen, verschluesse  # Gibt die Suchkriterien zurück.

if __name__ == "__main__":
    list_criteria()  # Listet die Suchkriterien auf.
    Start()  # Startet das Programm.
    print(generateHelmSite())  # Zeigt die Liste der Helme an.
    # Dieser Code wird nur ausgeführt, wenn du das Skript direkt ausführst.