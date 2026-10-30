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
    Funzione che prende in input un valore e si assicura che sia un numero
    """
    try:
        numero = float(valore.replace(',', '.'))
        return math.isfinite(numero)
    except ValueError:
        return False


def mesi_possibili():
    mesi = [
        12,
        13, # CCNL metalmeccanico
        14 #CCNL del commercio e terziario
    ]
    return mesi

def calcolo_IRPEF(IMPONIBILE):
    # Calcolo IRPEF in base agli scaglioni di reddito
    if IMPONIBILE <= 28000:
        IRPEF = IMPONIBILE * 0.23  # Aliquota IRPEF del 23% per redditi fino a 28.000€
    elif 28000 < IMPONIBILE <= 50000:
        IRPEF = (28000 * 0.23) + ((IMPONIBILE - 28000) * 0.33)  # Aliquota IRPEF del 33% per redditi tra 28.001€ e 50.000€
    else:
        IRPEF = (28000 * 0.23) + (27000 * 0.33) + ((IMPONIBILE - 50000) * 0.43)  # Aliquota IRPEF del 43% per redditi oltre 50.000€
    return IRPEF

def calcolo_detrazione(IMPONIBILE):
    # Calcolo detrazione IRPEF in base al RAL
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
    # Calcolo cuneo fiscale
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
    IRPEF_lorda = calcolo_IRPEF(IMPONIBILE)
    detrazione = calcolo_detrazione(IMPONIBILE)
    IRPEF_netta = max(0, IRPEF_lorda - detrazione)
    regione_comune = IMPONIBILE * 0.026
    return IRPEF_netta + regione_comune

def calcola_netto(RAL, mesi):
    INPS = RAL * 0.0919
    IMPONIBILE = RAL - INPS
    tasse = trattenute_IRPEF(IMPONIBILE)
    bonus_cuneo = calcolo_cuneo_fiscale(IMPONIBILE)
    NETTO_ANNUO = RAL - INPS - tasse + bonus_cuneo
    stipendio = NETTO_ANNUO / mesi
    return {
        "netto_annuo": round(NETTO_ANNUO, 2),
        "stipendio": round(stipendio, 2)
    }