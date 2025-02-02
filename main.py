from View import Terminal as view

# Aufruf der Methode Start 
try:
    view.Start()
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")