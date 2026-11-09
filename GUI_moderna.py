import calcoli
import module
import theme
import componenti_grafici
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

def calcolo():
    """
    Funzione che esegue il calcolo vero e proprio del netto annuo e mensile.
    Per eseguire il calcolo richiama altre funzioni definite in un file esterno
    """
    try:
        RAL_testo = ral_entry.get().strip() # Escludo eventuali spazi introdotti dall'utente

        if not RAL_testo:
            raise ValueError("Inserisci un valore di RAL")
        
        if not calcoli.valida_numero(RAL_testo):
            raise ValueError("Inserisci un valore numerico")
        
        RAL = float(RAL_testo.replace(',','.')) # Python usa i decimali con il '.' uso il replace qualora l'utente usasse la notazione con la virgola
        
        if RAL <= 0:
            raise ValueError("La RAL deve essere un valore positivo")
    
    except ValueError as e:
        CTkMessagebox(title="Errore", message=str(e), icon="cancel")
        return
    
    mesi = int(mensilità_entry.get())
    
    risultati = calcoli.calcola_netto(RAL, mesi)
    
    netto_annuo_output.configure(text=f"{calcoli.formatta_euro(risultati['netto_annuo'])} €")
    
    netto_mensile_output.configure(text=f"{calcoli.formatta_euro(risultati['stipendio'])} €")

def reset():
    """
    Costruzine di una funzione che resetti i campi riportandoli allo stato iniziale.
    Verra richiamata tramite l'uso del tasto ESC
    """
    
    ral_entry.delete(0, "end") # Cancello il campo RAL

    mensilità_entry.set("12") # Ripristino le mensilità

    # Azzero i risultati
    netto_annuo_output.configure(text="--- €")
    netto_mensile_output.configure(text="--- €")

    ral_entry.focus_set() # Riporto il cursore sul campo RAL

# Configurazione tema iniziale
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Definizione finestra
main_window = ctk.CTk()
main_window.title("RAL_netto")
main_window.geometry("1120x630")
main_window.minsize(1040, 585) # Impedisco che la finestra possa essere ridimensionata troppo piccola
main_window.configure(fg_color=("#F3F4F6", "#111827"))

main_window.grid_rowconfigure(1, weight=1)
main_window.grid_columnconfigure(0, weight=1)

# HEADER
header_frame =componenti_grafici.crea_header(main_window, corner_radius = 0)

# Etichetta del tema
tema_label = ctk.CTkLabel(header_frame, text="", font=ctk.CTkFont(size=13))
tema_label.pack(side="right", padx=(10, 5))

tema_switch = theme.crea_switch_tema(header_frame, tema_label)

tema_switch.pack(side="right", padx=10)
title_label = ctk.CTkLabel(header_frame, text="Calcolo stipendio netto mensile", font=ctk.CTkFont(family="Arial", size=28, weight="bold"))
title_label.pack(anchor="w")

subtitle_label = ctk.CTkLabel(header_frame, text="Inserisci la RAL e il numero di mensilità per calcolare lo stipendio netto mensile.", font=ctk.CTkFont(family="Arial", size=16))
subtitle_label.pack(anchor="w")

# AREA PRINCIPALE
content_frame = ctk.CTkFrame(main_window, fg_color="transparent")
content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=10)

content_frame.grid_columnconfigure((0, 1), weight=1, uniform="colonne") # Uniform mi assicura che i due frame siano uguali di larghezza
content_frame.grid_rowconfigure(0, weight=1)

# AREA INSERIMENTO DATI
input_frame = ctk.CTkFrame(content_frame, corner_radius=15, fg_color=("#FFFFFF", "#1F2937"))
input_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=5)
input_title = ctk.CTkLabel(input_frame, text="Inserimento dati", font=ctk.CTkFont(family="Arial", size=22, weight="bold"))
input_title.pack(pady=(20, 10)) # Si usa la tupla per indicare da sopra e da sotto, senza tupla indica solo da sopra
input_content_frame = componenti_grafici.crea_contenitore(input_frame, expand=True) # Creo questo frame per tenere i dati centrati anche se la finestra viene massimizzata

# AREA RISULTATI
results_frame = ctk.CTkFrame(content_frame, corner_radius=15, fg_color=("#FFFFFF", "#1F2937"))
results_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=5)
results_title = ctk.CTkLabel(results_frame, text="Risultati", font=ctk.CTkFont(family="Arial", size=22, weight="bold"))
results_title.pack(pady=20)
result_content_frame = componenti_grafici.crea_contenitore(results_frame, expand=True, fill='x') # Creo questo frame per tenere i dati centrati anche se la finestra viene massimizzata

# FOOTER
footer_frame = componenti_grafici.crea_footer(main_window, row=2, corner_radius=0)
footer_label = ctk.CTkLabel(footer_frame, text="Nota: Le addizionali regionali e comunali variano in base alla residenza. Il programma applica una trattenuta media stimata del 2,6% sull'imponibile (pari a circa il 2,3% del lordo).", font=ctk.CTkFont(family="Arial", size=12))
footer_label.pack()

# ETICHETTE E CAMPI
ral_label = ctk.CTkLabel(input_content_frame, text='RAL (€)', font=ctk.CTkFont('Arial', size=16))
ral_label.pack(pady = (25, 5))
ral_entry = ctk.CTkEntry(input_content_frame, placeholder_text="Es. 35000", width=250, height=40, font=ctk.CTkFont('Arial', size=16), justify="center")
ral_entry.pack(pady = 5)

mensilità = ctk.CTkLabel(input_content_frame, text='Mensilità', font=ctk.CTkFont('Arial', size=16))
mensilità.pack(pady = (25, 5))

mensilità_entry = ctk.CTkComboBox(input_content_frame, values=calcoli.mesi_possibili(), width=250, height=40, font=ctk.CTkFont('Arial', 16), state='readonly', justify="center")
mensilità_entry.set(calcoli.mesi_possibili()[0])
mensilità_entry.pack(pady = 5)

netto_annuo_frame = ctk.CTkFrame(result_content_frame, corner_radius=12, fg_color=("#E5E7EB", "#273449"))
netto_annuo_frame.pack(fill="x", padx=20, pady=(20, 10))

netto_annuo_label = ctk.CTkLabel(netto_annuo_frame, text="NETTO ANNUO", font=ctk.CTkFont(size=13, weight="bold"), text_color=("#6B7280", "#9CA3AF"))
netto_annuo_label.pack(pady=(20, 5))

netto_annuo_output = ctk.CTkLabel(netto_annuo_frame, text="--- €", font=ctk.CTkFont(size=30, weight="bold"), text_color=("#111827", "#FFFFFF"))
netto_annuo_output.pack(pady=(5, 20))

netto_mensile_frame = ctk.CTkFrame(result_content_frame, corner_radius=12, fg_color=("#DBEAFE", "#1E3A5F"))
netto_mensile_frame.pack(fill="x", padx=20, pady=10)

netto_mensile_label = ctk.CTkLabel(netto_mensile_frame, text="NETTO MENSILE", font=ctk.CTkFont(size=13, weight="bold"), text_color=("#1D4ED8", "#BFDBFE"))
netto_mensile_label.pack(pady=(20, 5))

netto_mensile_output = ctk.CTkLabel(netto_mensile_frame, text="--- €", font=ctk.CTkFont(size=30, weight="bold"), text_color=("#1E3A8A", "#FFFFFF"))
netto_mensile_output.pack(pady=(5, 20))

calcolo_button = ctk.CTkButton(input_content_frame, text='Calcola', command=calcolo, width=250, height=45, font=ctk.CTkFont('Arial', size=16, weight="bold"), corner_radius=10, text_color=("#FFFFFF", "#FFFFFF"))
calcolo_button.pack(pady=35)

"""
exit_button = ctk.CTkButton(footer_frame, text="Esci", command=module.uscita_gui, width=120, height=40, fg_color="#DC2626", hover_color="#991B1B", corner_radius=10)
exit_button.pack(side="right", padx=10)
"""

# Creazione funzionalità tasti
main_window.bind("<Return>", lambda event: calcolo()) # Permette di usare il tasto invio per eseguire la funzione calcolo()
main_window.bind("<Escape>", lambda event: reset()) # Permette di usare il tasto ESC per resettare i campi

main_window.after(100, lambda: ral_entry.focus_set()) # Attesa di 100 millisecondi e poi posiziona il cursore su RAL entry
main_window.mainloop()