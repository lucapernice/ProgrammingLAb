lista = [5]

def contatore(a):
    segni = []
    for i in range(1,len(a),1):
        if a[i]!=a[i-1]:
            segno = (a[i]-a[i-1])/abs(a[i]-a[i-1])
            segni.append(segno)
    #print(segni)
    
    contatore = 0


    for i in range(0,len(segni)-1,1):
        if segni[i] != segni[i+1]:
            contatore += 1
    
    return contatore

print(contatore(lista))

