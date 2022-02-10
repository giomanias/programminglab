
#-----------------------------------------------------------
class IncrementModel:

  def __init__(self,data):

    self.data = data

  def predict(self):
  
    precedente = None
    
  #se data non è una lista lo segnalo 
    if isinstance(self.data,list):
    
      print('data è una lista')
  
    else:
      
      return 'data non è una lista'
  #controllo se data ha abbastanza elementi per fare la previsione
    n = len(self.data)
    
    if (n < 2):

      print('non posso fare la previsione perchè data ha troppi pochi dati \n')
      
    
  #altrimenti faccio un ciclo per calcolare la differenza tra i vari elementi

    else:

      for item in self.data:
        
        if precedente is not None:

          diff = item - precedente
          base = item

        else:
          precedente = item

    return base+(diff/(n-1))
   
#------------------------------------------------------------
#INIZIALIZZAZIONE

l = [50,52,60]

previsione = IncrementModel(l)

print(previsione.predict())








