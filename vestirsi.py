import random

class Automa:
    def __init__(self):
        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None
    
    def indossa_biancheria(self):

        print('L\'automa prova a indossare la biancheria...')

        if self.pantaloni == None and self.calzatura == None :
            self.biancheria = True
            print('... operiazione riuscita')
            return 1
        
        else:
            print('... operazione non riuscita')
            return 0
    
    def indossa_calzini(self):

        print('L\'automa prova a indossare i calzini...')

        if self.calzatura == None :
            self.calzini = True
            print('... operiazione riuscita')
            return 1
        
        else:
            print('... operazione non riuscita')
            return 0
    
    def indossa_maglia(self):

        print('L\'automa prova a indossare la maglia...')

        
        self.biancheria = True
        print('... operiazione riuscita')
        return 1
    
    def indossa_pantaloni(self):

        print('L\'automa prova a indossare i pantaloni...')

        if self.calzatura == None :
            self.pantaloni = True
            print('... operiazione riuscita')
            return 1
        
        else:
            print('... operazione non riuscita')
            return 0
        
        
    def indossa_calzatura(self):

        print('L\'automa prova a indossare le scarpe...')

        
        self.biancheria = True
        print('... operiazione riuscita')
        return 1
    
gigi = Automa()


def esegui(Automa,capo):

    if capo == 'biancheria':
        return Automa.indossa_biancheria()

    if capo == 'calzini':
        return Automa.indossa_calzini()

    if capo == 'maglia':
        return Automa.indossa_maglia()
    
    if capo == 'pantaloni':
        return Automa.indossa_pantaloni()

    if capo == 'calzatura':
        return Automa.indossa_calzatura()
    
capi_vestiario = ['biancheria','calzini','maglia','pantaloni','calzatura'] 

vestito = True

while vestito == True and len(capi_vestiario) > 0:
    indice = random.randint(0,len(capi_vestiario)-1)
    print('estratto',capi_vestiario[indice])
    check = esegui(gigi,capi_vestiario[indice]) 
    print (check)
    
    if check == 1:
        print('indossato',capi_vestiario[indice])
        capi_vestiario.remove(capi_vestiario[indice])
    else:
        print('Non è stato possibile indossare ',capi_vestiario[indice])
        vestito = False


        


        
       

