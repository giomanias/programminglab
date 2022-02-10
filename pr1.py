class MovingAverage :

  def __init__(self,n=2):

    self.n = n

  def compute(self,lista):

    value = []

    if not isinstance(lista,list):

      raise Exception('si deve inserire una lista')

    i = 0

    lun = len(lista)

    if (self.n <= 1):

      raise Exception('impossibile fare la media')

    if (lun < 2):

      raise Exception('la lista ha troppi pochi elementi')

    while (i <= lun-(self.n-1)):

      k = i

      while (k < i + self.n-1):

        k = k + 1

        lista[i] = lista[i] + lista[k]
      
      lista[i] = lista[i]/self.n

      c = lista[i]

      value.append(c)

      i = i + self.n

    return value

valori=[2,4,8,16,20,22]

ris = MovingAverage()

print(ris.compute(valori))


     

