import calcoli
import module
import tkinter as tk
from tkinter import ttk, messagebox

def calcolo():
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
        messagebox.showerror("Errore", str(e))
        return
    
    mesi = int(mensilità_entry.get())
    
    risultati = calcoli.calcola_netto(RAL, mesi)
    
    netto_output.config(state="normal")
    netto_output.delete("1.0", tk.END)
    netto_output.insert ("1.0", f"{risultati['netto_annuo']} €", "center")
    netto_output.config(state="disable")
    
    mese_generico_output.config(state="normal")
    mese_generico_output.delete("1.0", tk.END)
    mese_generico_output.insert ("1.0", f"{risultati['stipendio']} €", "center")
    mese_generico_output.config(state="disabled")

    messagebox.showinfo("Info", "Nota: Le addizionali regionali e comunali variano in base alla residenza. Il programma applica una trattenuta media stimata del 2,6% sull'imponibile (pari a circa il 2,3% del lordo).")

# Definizione finestra
main_window = tk.Tk()
main_window.title("Calcolo stipendio netto mensile")
main_window.geometry("1280x720")
main_window.configure(background = module.colore()) # Setto un colore per lo sfondo

main_window.grid_rowconfigure(0 , weight=1)
main_window.grid_columnconfigure(0, weight=1)

# Frame centrato
main_frame = tk.Frame(main_window)
main_frame.configure(background = module.colore()) # Setto un colore per lo sfondo del frame
main_frame.grid(row=0, column=0)

# Etichette e campi input
ral_label = tk.Label(main_frame, text='RAL', font=('Arial', 16), background = module.colore())
ral_label.grid(row=0, column=1, padx=10, pady=10)
ral_entry = tk.Entry(main_frame, font=('Arial', 16), justify="center")
ral_entry.grid(row=0, column=2, padx=10, pady=10)

mensilità = tk.Label(main_frame, text='Mensilità', font=('Arial', 16), background=module.colore())
mensilità.grid(row=1, column=1, padx=10, pady=10)

mensilità_entry = ttk.Combobox(main_frame, values=calcoli.mesi_possibili(), font=('Arial', 16), state='readonly', justify="center")
mensilità_entry.current(0)
mensilità_entry.grid(row=1, column=2, padx=10, pady=10)

netto_label = tk.Label(main_frame, text='Netto Annuo', font=('Arial', 16), background=module.colore())
netto_label.grid(row=2, column=0, padx=10, pady=10)
netto_output = tk.Text(main_frame, width=20, height=1, state="disabled", font=('Arial', 16))
netto_output.grid(row=2, column=1, padx=10, pady=10)
netto_output.tag_configure("center", justify="center")

mese_generico_label = tk.Label(main_frame, text='Mensilità', font=('Arial', 16), background=module.colore())
mese_generico_label.grid(row=2, column=2, padx=10, pady=10)
mese_generico_output = tk.Text(main_frame, width=20, height=1, state="disabled", font=('Arial', 16))
mese_generico_output.grid(row=2, column=3, padx=10, pady=10)
mese_generico_output.tag_configure("center", justify="center")

# Frame pulsanti e Bottone Calcola
button_frame = tk.Frame(main_frame)
button_frame.configure(background = module.colore()) # Setto un colore per lo sfondo dei pulsanti
button_frame.grid(row=4, column=0, columnspan=4)

calcolo_button = tk.Button(button_frame, text='Calcola', command=calcolo, font=('Arial', 16), background='lightgreen')
main_window.bind("<Return>", lambda event: calcolo()) # Permette di usare il tasto invio per eseguire la funzione calcolo()
calcolo_button.grid(row=0, column=1, padx=10, pady=10)
exit_button = tk.Button(button_frame, text='Esci', command=module.uscita_gui, font=('Arial', 16), background='lightcoral')
exit_button.grid(row=0, column=0, padx=10, pady=10)

main_window.mainloop()