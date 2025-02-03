class Helm:
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
