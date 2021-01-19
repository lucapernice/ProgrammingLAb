def controllodilista(lista):
    if type(lista) is not list:
        raise ExamException('La funzione compute necessita di una lista come variabile')
    if len(lista) < 2:
        raise ExamException('La lista inserita deve avere almeno due elementi')
    
    for item in lista:
        if type(item) is not int or float:
            raise ExamException('Errore, inserire nella lista solo valori di tipo int o float!') 

    if lista == []:
            raise ExamException('Errore, lista valori vuota')
    


class ExamException(Exception):

        pass

class Diff:

    def __init__(self,ratio = 1):
        self.ratio = ratio
    
    def compute(self,lista):
        controllodilista(lista)
        result=[]
        i = 1
        while i < len(lista):
            differenza = lista[i]-lista[i-1]
            result.append(differenza/self.ratio)
            i +=1

        return result