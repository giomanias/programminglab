#La  media mobile è un’operazione che data una serie di valori calcola la media di una finestra che si “sposta” sulla serie, fino a calcolarla per tutti i valori. Il parametro fondamentale (e unico) di tale operazione è la lunghezza della finestra. Per esempio, con lunghezza della finestra pari a “2”, e data la serie di valori 2, 4, 8, 16, la media mobile calcola al primo giro il risultato “3” (ovvero la media tra il valore 2 e 4, per il secondo il risultato “6” (ovvero la media tra i valori 4 e 8), e per il terzo il valore “12”, per poi tornare i valori 3, 6 e 12.

class MovingAverage():

  def __init__(self,lunghezza):

    self.lunghezza = lunghezza

  def compute(self,lista):

    i=0
    n=0
    item=0
    media=0

    value = []

    while(i <= len(lista)):
      
      while(n <= self.lunghezza):
      
        item =lista[n] + lista[n+1]

        n = n+1

        media = item/self.lunghezza

        value.append(media)
      
      item=0
      i=i+1
    
    return value

class ExamException(Exception):

  pass

#moving_average = MovingAverage(2)

#result = moving_average.compute([2,4,8,16])

#print(result) 
  


  




