from Model import HelmBestand

def suche_helme(preis=None, material=None, groesse=None, art=None, verschluss=None):
    """Sucht Helme basierend auf den angegebenen Kriterien."""
    gefundene_helme = []  # Liste für gefundene Helme
    for helm in HelmBestand.helme.values():  # Geht alle Helme im Bestand durch
        if  (preis is None or helm.preis <= preis) and (material is None or helm.material == material) and (groesse is None or helm.groesse == groesse) and \
            (art is None or helm.art == art) and (verschluss is None or helm.verschluss == verschluss):
            # Prüft, ob der Helm den Kriterien entspricht
            gefundene_helme.append(helm)  # Fügt den Helm zur Liste der gefundenen Helme hinzu
    return  gefundene_helme  # Gibt die Liste der gefundenen Helme zurück

def helm_auswahl(helm_liste):
    """Zeigt die Details der ausgewählten Helme an."""
    for helm in helm_liste:  # Geht die Liste der ausgewählten Helme durch
        helm_info = (f"{helm.name}, Größe: {helm.groesse}, Warenbestand: {helm.warenbestand}, "
                     f"Preis: {helm.preis}€, Art: {helm.art}, Verschluss: {helm.verschluss}, "
                     f"Material: {helm.material}")
        # Erstellt eine Zeichenkette mit den Details des Helms
        print(helm_info)  # Gibt die Helm-Details aus
        print(f"{helm.name} wurde jetzt ausgewählt")  # Bestätigt die Auswahl des Helms