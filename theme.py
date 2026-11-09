import customtkinter as ctk


def crea_switch_tema(parent, tema_label):

    # Recupero il tema attualmente utilizzato
    tema_corrente = ctk.get_appearance_mode().lower()
    tema_var = ctk.StringVar(value=tema_corrente)

    tema_label.configure(
        text="Modalità chiara" if tema_corrente == "light"
        else "Modalità scura"
    )

    # Creo il contenitore dello switch
    tema_switch = ctk.CTkFrame(
        parent,
        width=82,
        height=34,
        corner_radius=18,
        fg_color=("#D1D5DB", "#334155")
    )

    tema_switch.pack(side="right", padx=10)
    tema_switch.pack_propagate(False)

    # Creo il cursore circolare
    tema_cursore = ctk.CTkLabel(
        tema_switch,
        text="",
        width=28,
        height=28,
        corner_radius=14,
        fg_color="#FFFFFF",
        bg_color=("#D1D5DB", "#334155"),
        text_color="#111827",
        font=ctk.CTkFont(family="Segoe UI Emoji", size=14),
        anchor="center",
    )


    # Posizione iniziale
    if tema_corrente == "dark":
        tema_cursore.configure(text="🌙")
        tema_cursore.place(x=30, y=3)
    else:
        tema_cursore.configure(text="☀️")
        tema_cursore.place(x=5, y=3)

    # Gestisco il cambiamento del tema
    def cambia_tema(event=None):

        if tema_var.get() == "dark":
            nuovo_tema = "light"
            tema_cursore.configure(text="☀️")
            tema_cursore.place(x=5, y=3)

        else:
            nuovo_tema = "dark"
            tema_cursore.configure(text="🌙")
            tema_cursore.place(x=30, y=3)

        tema_var.set(nuovo_tema)
        ctk.set_appearance_mode(nuovo_tema)

        if nuovo_tema == "light":
            tema_label.configure(text="Modalità chiara")
        else:
            tema_label.configure(text="Modalità scura")

    # Associo il click a tutti gli elementi dello switch
    tema_switch.bind("<Button-1>", cambia_tema)
    tema_cursore.bind("<Button-1>", cambia_tema)

    return tema_switch
