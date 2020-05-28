# Cutset Conditioning & Map Coloring
- AdjacencyMatrix-> crea una matrice di adiacenza per il grafo iniziale con l'uso di probabilità
- Node -> crea l'istanza di un nodo, con caratteristiche relative a colore, nodi adiacenti e dominio dei colori
- Graph -> genera il grafo di partenza basandosi sulla matrice di adiacenza e sfruttando la classe Node
- TreeDecision -> uso di due funzioni: 1) find_cycle che permette di determinare un ciclo all'interno del grafo; 2) cutset_decomposition che trasforma il grafo in un albero eliminando i riferimenti dei nodi del ciclo all'interno della matrice di adiacenza
- Functions -> funzioni utili alla risoluzione del problema: 1) TopSort determina un ordinamento topologico per l'espolarazione dell'albero; 2) Revise che permette di eseguire eventuali crossout tra i domini dei vari nodi adiacenti; 3) DAC che mantiene la consistenza di arco utile per il mantenimento dei vincoli.
- CSP -> classe che determina gli assegnamenti in base ai vincoli imposti tramite due funzioni: 1) assignment_cycle che assegna il colore ai nodi all'interno del ciclo trovato con TreeDecision; 2) assignment che assegna il colore ai nodi restanti del grafo
- CSP_Solver -> funzione che determina la soluzione del problema all'interno della quale si richiamano TopSort, DAC e assignment
- Main -> rappresenta in chiaro il progetto che si è voluto svolgere
