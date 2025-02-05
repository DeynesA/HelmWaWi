class Helm:
    """
    Diese Klasse ist eine Datenstruktur, sie beinhaltet den Bauplan und die Daten
    um eine entsprechende Klasse zu generieren.
    """
    def __init__(self, name, groesse, warenbestand, preis, art, verschluss, material):
        self.name = name
        self.groesse = groesse
        self.warenbestand = warenbestand
        self.preis = preis
        self.art = art
        self.verschluss = verschluss
        self.material = material

    def __repr__(self):
        return (f"Helm(Name: {self.name}, Gr\u00f6\u00dfe: {self.groesse}, Warenbestand: {self.warenbestand}, "
                f"Preis: {self.preis}\u20ac, Art: {self.art}, Verschluss: {self.verschluss}, Material: {self.material})")

"""
Verschiedene Tupel um in Logic.py strings generisch der Inhalte zu generieren
"""
HelmKategorien = ("Sport", "Enduro", "Cruiser", "Jethelm", "Klapphelm")
HelmSize = ("S","M","L","XL")
HelmVerschluss = ("Ratsche", "Doppel-D")
HelmMaterial = ("Fiberglas", "Carbon", "Polycarbonat")
