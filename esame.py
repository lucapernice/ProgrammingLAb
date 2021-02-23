class ExamException(Exception):

        pass

class CSVTimeSeriesFile:

    def __init__(self,name=None):

        #setto il nome del file
        self.name = name
    
    def get_data(self):

        #Per prima cosa controllo che il nome del file inserito sia una stringa oppure che non sia stato prorio inserito
        if type(self.name) != str or self.name == None:
            raise ExamException ('Errore, il "name" inserito non è una stringa oppure il campo è vuoto')

        #inizializzo una lista vuota per salvare i valori in seguito.La get_data tornerà questa stessa lista.
        values = []

        try:
            my_file = open(self.name,'r')
        
        except:

            raise ExamException('Errore nella lettura del file')
            


        #leggo il file linea per linea
        for line in my_file:

            #faccio lo split di ogni linea sulla virgola
            elements = line.split(',')
            

            if elements[0] != 'epoch':
                try:
                    #converto prima in float e poi approssimo
                    elements[0] = float(elements[0])
                    elements[0] = round(elements[0])
                    if elements[0] < 0:
                        continue
                    
                    elements[1] = float(elements[1])
                    
                    
                    

                    values.append(elements)

                except:
                    continue

        #chiudo il file
        my_file.close()

        #A questo punto controllo se la lista values è vuota. 
        if len(values) == 0:
            raise ExamException('Lista valori vuota')

        #controllo ordine
        for i in range (len(values)-1):
            
            if values[i][0] >= values[i+1][0]:
                raise ExamException('La serie temporale non è ordinata oppure è presente un duplicato')
            
            


        return values



#Corpo del programma

#funzione che mi crea una lista con le temperature per ogni ora più l'ultima temperatura (o le ultime due quando necessario) dell'ora precedente

def suddivisione(lista_dati):

    i = 0
    #ore sarà il return della funzione. Dentro ci vanno le liste delle serie di temperature relative a ogni ora
    ore = []

    while i < len(lista_dati)-1:
        #definisco un insieme che contiene l'ultima temperatura dell'ora precedente e la prima dell'ora corrente
        if i>0:
            insieme = [lista_dati[i-1][1],lista_dati[i][1]]
        #se i = 0 non esiste una temperatura precedente
        if i == 0:
            insieme = [lista_dati[i][1]]
    
        
        start = i
        #A insieme aggiungo i termini successivi della lista di dati se corrispondono alla stessa ora
        while i+1 < len(lista_dati)-1 and lista_dati[i+1][0]//3600 == lista_dati[i][0]//3600 :
            insieme.append(lista_dati[i+1][1])
            i+=1
        #con questo if considero anche l'ultimo elemento della lista_dati lasciato fuori dal while(evito index error)
        if lista_dati[i+1][0]//3600 == lista_dati[i][0]//3600:
            insieme.append(lista_dati[i+1][1])
        
        
        #se ho solo due valori vuol dire che devo aggiungerne un altro dell'ora precedente(ho bisogno di almeno tre valori per contare le inversioni di trend)
        if len(insieme) == 2 and i>1:
            insieme = [lista_dati[start-2][1],lista_dati[start-1][1],lista_dati[start][1]]
        
        
        #aggiungo insieme alla lista ore
        ore.append(insieme)
        
        
        i+=1
        
            
    
    #se l'ultimo elemento della lista è di un'ora diversa da quelli precedenti    
    if lista_dati[i][0]//3600!= lista_dati[i-1][0]//3600:
        ore.append([lista_dati[i-2][1],lista_dati[i-1][1],lista_dati[i][1]]) 
    

    print(ore)
    return ore

#la funzione contatore prenerà come imput il return della funzione suddivisione. Serve a contare il numero di variazioni di trend
def contatore(a):
    
    segni = []
    for i in range(1,len(a),1):
        
        if a[i]!=a[i-1]:
            #segno = 1 se trend è crescente, -1 se decrescente
            segno = (a[i]-a[i-1])/abs(a[i]-a[i-1])
            
            segni.append(segno)
    
    #contatore è il numero di variazioni del trend
    contatore = 0

    #conto le variazioni con un for
    for i in range(0,len(segni)-1,1):
        if segni[i] != segni[i+1]:
            contatore += 1
    
    return contatore

#come richiesto dal compito
def hourly_trend_changes(lista_dati):
    if len(lista_dati)==1:
        return [0]

    insieme = suddivisione(lista_dati)
    #print(insieme)
    result = []
    for elem in insieme:
        result.append(contatore(elem))
    
    
    
    return result







        
time_series_file = CSVTimeSeriesFile(name ='data.csv')
    
time_series= time_series_file.get_data()

hourly_trend_changes(time_series)


