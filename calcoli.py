import math

def richiedi_intero(messaggio):
    """
    Funzione che si assicura che il valore in input sia un intero
    """
    while True:
        try:
            return int(input(messaggio))
        except ValueError:
            print("\nErrore: Devi inserire un numero intero valido. Riprova.\n")

def valida_numero(valore):
    """
    Funzione che prende in input un valore e si assicura che sia un numero e che questo non sia infinito.
    Fa anche una sostituzione tra virgola e punto in quanto Python per indicare un valore decimale usa il punto
    ma nel linguaggio comune si usa la virgola.
    Siccome ci si può aspettare che l'utente inserisca un valore contenente la virgola che genererebbe un errore quest'ultima verrà sostituita con il punto
    """
    try:
        numero = float(valore.replace(',', '.'))
        return math.isfinite(numero)
    except ValueError:
        return False


def mesi_possibili():
    """
    Funzione che ritorna la lista di mensilità da usare nella box della GUI
    """
    mesi = [
        12,
        13, # CCNL metalmeccanico, AIOP
        14  # CCNL del commercio e terziario
    ]
    return mesi

def calcolo_IRPEF(IMPONIBILE):
    """
    Funzione che calcola l'IRPEF in base agli scaglioni dell'imponibie.

    Input: Valore Imponibile
    Output: Quota IRPEF
    """
    if IMPONIBILE <= 28000:
        IRPEF = IMPONIBILE * 0.23  # Aliquota IRPEF del 23% per redditi fino a 28.000€
    elif 28000 < IMPONIBILE <= 50000:
        IRPEF = (28000 * 0.23) + ((IMPONIBILE - 28000) * 0.33)  # Aliquota IRPEF del 33% per redditi tra 28.001€ e 50.000€
    else:
        IRPEF = (28000 * 0.23) + (27000 * 0.33) + ((IMPONIBILE - 50000) * 0.43)  # Aliquota IRPEF del 43% per redditi oltre 50.000€
    return IRPEF

def calcolo_detrazione(IMPONIBILE):
    """
    Funzione che calcola la detrazione IRPEF in base agli scaglioni dell'imponibie.

    Input: Valore Imponibile
    Output: Detrazione IRPEF
    """
    detrazione = 0
    if IMPONIBILE <= 15000:
        detrazione = 1955  # Detrazione per redditi fino a 15.000€
    elif 15000 < IMPONIBILE <= 28000:
        detrazione = 1910 + 1190 *((28000 - IMPONIBILE) / 13000)  # Detrazione decrescente per redditi tra 15.001€ e 28.000€
    elif 28000 < IMPONIBILE <= 50000:
        detrazione = 1910 * ((50000 - IMPONIBILE) / 22000)  # Detrazione decrescente per redditi tra 28.001€ e 50.000€
    else:
        detrazione = 0  # Nessuna detrazione per redditi oltre 50.000€
    return detrazione

def calcolo_cuneo_fiscale(IMPONIBILE):
    """
    Funzione che calcola il cuneo fiscale in base agli scaglioni dell'imponibile
    
    Input: Valore Imponibile
    Output: Valore del cuneo fiscale
    """
    cuneo_fiscale = 0
    if IMPONIBILE <= 20000:
        cuneo_fiscale = IMPONIBILE * 0.053 if IMPONIBILE > 8500 else IMPONIBILE * 0.071
    elif 20000 < IMPONIBILE <= 32000:
        cuneo_fiscale = 1000
    elif 32000 < IMPONIBILE <= 40000:
        cuneo_fiscale = 1000 * (40000 - IMPONIBILE) / 8000  # Cuneo fiscale decrescente per redditi tra 32.001€ e 40.000€
    else:
        cuneo_fiscale = 0  # Nessun cuneo fiscale per redditi oltre 40.000€
    return cuneo_fiscale

def trattenute_IRPEF(IMPONIBILE):
    """
    Funzione che calcola le trattenute IRPEF considerando la detrazione.
    Viene considerata un'imposta media del 2,6% per trattenute regionali e comunali
    
    Input: Valore Imponibile
    Output: Trattenute IRPEF
    """
    IRPEF_lorda = calcolo_IRPEF(IMPONIBILE)
    detrazione = calcolo_detrazione(IMPONIBILE)
    IRPEF_netta = max(0, IRPEF_lorda - detrazione)
    regione_comune = IMPONIBILE * 0.026
    return IRPEF_netta + regione_comune

def calcola_netto(RAL, mesi):
    """
    Funzione che calcola il netto annuo e mensile
    
    Input: RAL e numero di mensilità
    Output: Netto annuo e stipendio mensile
    """
    INPS = RAL * 0.0919 # 9,19% va all'INPS il rimanente è l'imponibile
    IMPONIBILE = RAL - INPS
    tasse = trattenute_IRPEF(IMPONIBILE)
    bonus_cuneo = calcolo_cuneo_fiscale(IMPONIBILE)
    NETTO_ANNUO = RAL - INPS - tasse + bonus_cuneo
    stipendio = NETTO_ANNUO / mesi
    return {
        "netto_annuo": round(NETTO_ANNUO, 2),
        "stipendio": round(stipendio, 2)
    }