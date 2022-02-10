#definire una classe calcolatrice che faccia le operazioni aritmetiche del tipo somma, divisione, moltiplicazione, sottrazzione. e si faccia il test per controllare ilrisultato


class Calcolatrice():

  def __init__(self,a,b):

    self.a = a
    self.b = b

  def somma(self):

    return sum(a,b)
  
  def moltiplicazione(self):

    return (a*b)
  
  def sottrazione(self):

    return (a-b)
  
  def divisione(self):
    
    if (b != 0):

      return (a/b)
    
    else:

      return ('impossibile perchè b è 0')

mio_file=Calcolatrice(1,2)

somma=mio_file.somma()

  print('test somma passato')

else:

  print('dio cane')

     





