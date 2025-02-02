from Model import HelmBestand

def suche_helme(preis=None, material=None, groesse=None, art=None, verschluss=None):
    """Sucht Helme basierend auf den angegebenen Kriterien."""
    gefundene_helme = []
    for helm in HelmBestand.helme.values():
        if (preis is None or helm.preis <= preis) and \
           (material is None or helm.material == material) and \
           (groesse is None or helm.groesse == groesse) and \
           (art is None or helm.art == art) and \
           (verschluss is None or helm.verschluss == verschluss):
            gefundene_helme.append(helm)
    return gefundene_helme

def helm_auswahl(helm_liste):
    """Zeigt die Details der ausgewählten Helme an."""
    for helm_name in helm_liste:
        try:
            helm = HelmBestand.helme[helm_name]
            helm_info = (f"{helm.name}, Größe: {helm.groesse}, Warenbestand: {helm.warenbestand}, "
                         f"Preis: {helm.preis}€, Art: {helm.art}, Verschluss: {helm.verschluss}, "
                         f"Material: {helm.material}")
            print(helm_info)
            print(f"{helm.name} wurde jetzt ausgewählt")
        except KeyError:
            print(f"Der Helm'{helm_name}' wurde nicht gefunden.")