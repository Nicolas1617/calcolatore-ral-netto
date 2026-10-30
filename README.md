# 🧮 Calcolatore RAL to Netto (Tassazione Italiana)

Un'applicazione desktop leggera, veloce e intuitiva per **calcolare lo stipendio netto mensile partendo dalla Retribuzione Annua Lorda (RAL)**. 

Capire come le tasse, le addizionali e le mensilità influenzino la busta paga in Italia è spesso complicato. Questo strumento nasce per dare una risposta immediata e trasparente con pochissimi clic.

---

## ✨ Funzionalità

* **Calcolo in tempo reale:** Trasforma la tua RAL nel netto mensile stimato.
* **Supporto multi-mensilità:** Gestione del calcolo basata su contratti a 12, 13 o 14 mensilità.
* **Interfaccia Grafica (GUI):** Semplice da usare, pulita e senza bisogno di aprire il terminale.
* **Nessuna installazione richiesta:** Un unico file `.exe` pronto all'uso.

---

## 🚀 Come scaricare ed eseguire il programma

Non è necessario installare Python o configurare librerie sul tuo computer per usare l'applicazione:

1. Vai nella sezione **[Releases](https://github.com/Nicolas1617/calcolatore-ral-netto)** sulla destra di questa pagina.
2. Scarica l'ultima versione dell'eseguibile (es. `RAL_netto.exe`).
3. Fai doppio clic sul file scaricato per avviare l'app.

---

## ⚠️ Nota importante per l'Antivirus (Falsi Positivi)

Poiché il file `.exe` è compilato tramite `PyInstaller`, **Windows Defender o altri antivirus potrebbero bloccarlo o segnalarlo come minaccia**. 

Si tratta di un **falso positivo** molto comune nel mondo Python. Gli antivirus tendono a diffidare dei file eseguibili creati da sviluppatori indipendenti che non dispongono di una firma digitale a pagamento.

* **La massima trasparenza:** Questo progetto è al 100% open-source. Puoi esaminare l'intero codice sorgente qui sopra per assicurarti che l'applicazione sia totalmente sicura e priva di codice dannoso.
* **Come avviarlo:** Se Windows mostra la schermata blu *SmartScreen*, clicca su **"Ulteriori informazioni"** e successivamente sul pulsante **"Esegui comunque"**.

---

## 🐛 Segnalazione Bug e Suggerimenti

Il tuo feedback è fondamentale per migliorare l'algoritmo di calcolo o aggiungere nuove funzioni! 

Se riscontri un errore nei conteggi, se il programma va in crash o se hai in mente una miglioria (es. gestione delle detrazioni per figli a carico, calcolo del superminimo, ecc.):
1. Vai nella scheda **[Issues](https://github.com/Nicolas1617/calcolatore-ral-netto)** in alto.
2. Clicca su **New Issue**.
3. Descrivi il problema o la tua proposta in modo dettagliato.

---

## 🛠️ Tecnologie utilizzate

* **Python 3** (Logica di calcolo)
* **PyInstaller** (Per la creazione dell'eseguibile standalone)

---

## 📄 Licenza

Questo progetto è distribuito sotto licenza **MIT**. Consulta il file `LICENSE` per ulteriori dettagli. 
*Nota: I calcoli forniti dall'applicazione hanno valore puramente indicativo e informativo, e non sostituiscono in alcun modo il parere di un consulente del lavoro o di un commercialista.*
