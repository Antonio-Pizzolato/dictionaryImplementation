# dictionaryImplementation

Come funziona  __setitem__ nella classe Dictionary:
il metodo __setitem__ viene chiamato quando si cerca di impostare un valore in un'istanza della classe tramite la sintassi my_dict[key] = value. Il primo argomento del metodo è self, che rappresenta l'istanza della classe sulla quale il metodo è stato chiamato. Il secondo argomento è key, che rappresenta la chiave associata al valore che si sta cercando di impostare. Il terzo argomento è value, che rappresenta il valore che si sta cercando di impostare.

Il metodo __setitem__ comincia cercando la chiave key nella lista di chiavi self.keys dell'istanza della classe. Se la chiave esiste già nel dizionario, viene trovato l'indice corrispondente tramite il metodo index() della lista. Questo indice viene utilizzato per aggiornare il valore associato alla chiave nella lista di valori self.values.

Se la chiave non esiste ancora nel dizionario, viene aggiunta alla fine della lista di chiavi self.keys, insieme al valore value alla fine della lista di valori self.values.

In questo modo, il metodo __setitem__ implementa il comportamento di un dizionario Python, cioè permette di aggiungere o aggiornare un valore associato a una chiave, ma in modo personalizzato e senza utilizzare la funzione predefinita di Python.
