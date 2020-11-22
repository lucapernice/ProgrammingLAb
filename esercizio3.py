def somma(lista):
    somma = 0
    for item in lista:
        somma += item
    return somma

#La classe che creo si chiama CSVFile come richiesto dalla consegna
class CSVFile:

    #
    def __init__(self,name):
        #attributo name
        self.name = name
    #metodo get_data che trona i dati dal file CSV come numeri di una lista
    def get_data(self):

        total_values = []
        my_file = open(self.name, "r")
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                date = elements[0]
                value = elements[1]

                total_values.append(float(value))
        summ = somma(total_values)
        print('La somma dei valori è: {} '.format(summ));

    pass

#Inizializzo sul nome del file CSV.
mio_file = CSVFile(name = 'shampoo_sales.csv')

print(mio_file.name)
print(mio_file.get_data())