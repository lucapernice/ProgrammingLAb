#Scrivete uno script che sommi
#tutti i valori delle vendite degli shampoo del file
#“shampoo_sales.csv”
#Poi, committate il file in cui l’avete scritto

def somma_elementi(lista):
    somma = 0
    for item in lista:
        somma = somma + item
    return somma

my_file = open("shampoo_sales.csv", "r")
total_values = []

for line in my_file:
    elements = line.split(",")
    if elements[0] != "Date":
        date = elements[0]
        value = elements[1]
        total_values.append(float(value))


print("La somma é: {}".format(somma_elementi(total_values)))
    
