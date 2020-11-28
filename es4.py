class Automobile:
    def __init__(self,casa_auto, modello, numero_posti,kw,targa):
        self.casa_auto = casa_auto
        self.modello = modello
        self.numero_posti = numero_posti
        self.kw = kw
        self.targa = targa

    def __str__(self):
        print("L'auto è della casa: ",self.casa_auto)  
        print('Il modello é: ', self.modello)
        print('Dispone di ',self.numero_posti,' posti') 
        print(self.kw, 'kw')  
        print('Targa: ',self.targa)
    
    def parla(self):
        print('Broom Broom')
    
    def confronta(self,altra_automobile):

        if self.casa_auto == altra_automobile.casa_auto:
            print('Le due vetture sono della stessa casa')
        else:
            print('Le due vetture sono diverse')
            return 0
        
        if self.modello == altra_automobile.modello :
            print('Le due vetture sono dello stesso modello')
        else:
            print('Le due vetture non sono dello stesso modello')
            return 0
        
        if self.numero_posti == altra_automobile.numero_posti:
            print('Le due automobili hanno lo stesso numero di posti')
        else:
            print('Le due vetture non hanno lo stesso numero di posti')
            return 0
        
        if self.kw == altra_automobile.kw:
            print('Uguale kw')
        else:
            print('Non hanno lo stesso kw')
            return 0
    
class Transformer(Automobile):
    def __init__(self,casa_auto, modello, numero_posti,kw,targa,nome, generazione,grado,fazione,reparto):
        super().__init__(casa_auto, modello, numero_posti,kw,targa)
        self.generazione = generazione
        self.grado = grado
        self.fazione = fazione
        self.reparto = reparto
        
panda = Automobile('Fiat','Panda',4,100,1234)    
panda2 = Automobile('Fiat','Panda',5,100,2342)

panda.confronta(panda2)
        
        
    

        
        