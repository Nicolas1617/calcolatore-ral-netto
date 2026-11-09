import customtkinter as ctk

def crea_contenitore(parent, **kwargs):
    """
    Permette di creare un frame e posizionarlo con pack
    Input:
        - nome del frame/finestra in cui posizionarlo
        - attributi che gli si vogliono dare
    Output:
        - frame configurato secondo le specifiche inserite
    """
    frame = ctk.CTkFrame(parent, fg_color="transparent")

    frame.pack(**kwargs)

    return frame

def crea_header(parent, **kwargs):
    """
    Permette di creare un header
    """
    header_frame = ctk.CTkFrame(parent, fg_color="transparent", **kwargs)
    header_frame.grid(row=0, column=0, sticky="ew", padx=30, pady=(20, 10)) # Sticky indica dove deve aderire il widget

    return header_frame

def crea_footer(parent, row, **kwargs):
    footer_frame = ctk.CTkFrame(parent, fg_color="transparent", **kwargs)
    footer_frame.grid(row=row, column=0, sticky="ew", padx=30, pady=(5, 15))

    return footer_frame