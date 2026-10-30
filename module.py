import sys

def uscita():
    """
    Funzione che permette di interrompere uno script Python
    """
    if input ("\nPremi invio per uscire ").strip().lower() == "":
        exit()

def uscita_gui():
    """
    Funzione che permette di uscire da una GUI
    """
    sys.exit()

def colore():
   """
   Funzione per definire un codice colore in esadecimale
   """
   return "#f8f9fa"