import unittest

def somma(lista):
    somma = 0
    for item in lista:
        somma += item
    return somma

#La classe che creo si chiama CSVFile come richiesto dalla consegna
class CSVFile:

    def __init__(self,name):
        #attributo name
        self.name = name
        if type(self.name) != str:
            raise Exception('Il valore name non è una stringa')
    
    #metodo get_data che trova i dati dal file CSV come numeri di una lista
    def get_data(self,start,end):

        if start > end:
            raise Exception('start è maggiore di end')
        


        total_values = []
        my_file = open(self.name, "r")

        numero_righe = 0
        for line in my_file:
            numero_righe = numero_righe + 1
        
        if end > numero_righe:
            raise Exception ('End è più grande del numero di righe')

        for line in my_file[start:end]:
            elements = line.split(',')

            if elements[0] != 'Date':
                date = elements[0]
                value = elements[1]

                try:
                    total_values.append(float(value))
                except ValueError:
                    print('La linea "{}" non contiene valori leggibili'.format(line))
                    total_values.append(0)
        
        summ = somma(total_values)
        print('La somma dei valori è:', summ)


#Inizializzo sul nome del file CSV.
try:
    mio_file = CSVFile(name = 'shampoo_sales.csv' )
            
    
except FileNotFoundError:
    print('Hai provato ad aprire un file inesistente')

print(mio_file.name)
mio_file.get_data(12,15)

class TestGet_Data(unittest.TestCase):
    def 


