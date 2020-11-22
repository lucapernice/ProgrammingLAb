import math

my_list = ['casa', 12 , 'giardino','naso']

def stampa_lista(lista):
    for item in lista:
        print (str(item))

stampa_lista(my_list)

def statistiche(lista):

    somma = sum(lista)
    print(somma)

    media = somma / len(lista)
    print(media)

    minimo = min(lista)
    massimo = max(lista)
    print('Il min è: ',minimo,' ed il max è: ',massimo)


my_number_list = [1,2,3,5,7,12,11]

statistiche(my_number_list)

def somma_vettoriale(lista1 , lista2):
    if len(lista1) != len(lista2):
        print('I due vettori non hanno la stessa dimensione')
        return []
    
    print('\ Controllo prima lista...')
    for item in lista1:
        if type(item) != int:
            print('In questa lista non tutti gli elementi sono interi')
            return []
            
            
    print('\ Controllo seconda lista...')
    for item in lista2:
        if type(item) != int:
            print('In questa lista non tutti gli elementi sono interi')
            return []
    
    somma = []
    i = 0
    for i in range(len(lista1)):
        result = lista1[i] + lista2[i]
        somma.append(result)
    print (somma)        

def prodotto_vettoriale(lista1, lista2):
    if len(lista1) != len(lista2):
        print('I due vettori non hanno la stessa dimensione')
        return []
    
    print('\ Controllo prima lista...')
    for item in lista1:
        if type(item) != int:
            print('In questa lista non tutti gli elementi sono interi')
            return []
            
            
    print('\ Controllo seconda lista...')
    for item in lista2:
        if type(item) != int:
            print('In questa lista non tutti gli elementi sono interi')
            return []
    
    prodotto = []
    i = 0
    for i in range(len(lista1)):
        result = lista1[i] * lista2[i]
        prodotto.append(result)
    print (prodotto)                     
    
lista1 = [2,3,4]
lista2 = [1,2,3]
somma_vettoriale(lista1,lista2) 
prodotto_vettoriale(lista1, lista2)   

