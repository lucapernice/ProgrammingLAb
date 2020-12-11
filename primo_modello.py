#provo a fare un primo modello

def calcolo_incremento(x,y):
    incremento = y-x
    return incremento

def calcolo_incremento_medio(lista_dati):
    
    a = 0
    b = 1
    somm = 0
    while b < len(lista_dati):
        
        x = lista_dati[a]
        y = lista_dati[b]
        somm = somm + calcolo_incremento(x,y)
        
        a = a + 1
        b = b + 1

    media = somm/(len(lista_dati) - 1)
    return media


class Model(object):
    def fit(self,data):
        pass
    
    def predict(self):
        pass

class Prova_di_modello(Model):

    def fit(sefl,data):
        self.global_avg_increment = calcolo_incremento_medio(data)
   
    def predict(self, lista_dati):
        
        
        valore_mese_successivo = lista_dati[len(lista_dati)-1] + calcolo_incremento_medio(lista_dati)

        print('Il mese seguente: ',valore_mese_successivo)
        


    

lista_dati_1 = [50,52,60]

prova1 = Prova_di_modello()
prova1.predict(lista_dati_1)






