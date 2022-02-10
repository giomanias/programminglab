
class Model():

  def __init__(self,file,n=24):

    self.file = file

    self.n = n

  def predict (self):

# init------
    precedente = None

    differenza = 0

    k = 0

    predizione = 0

    somma = 0

# liste vuote

    value = []

    predizioni = []

    myfile = open(self.file,"r")

#converto a float e aggioungo i dati a value

    for line in myfile:

      elements = line.split(',')

      if (elements[0] != 'Date'):

        value.append(float(elements[1]))

#eccezzioni ----- su n e lunghezza della lista

    if self.n > len(value):

      raise Exception('non è possibile fare la prediction')

    if len(value) < 2:

      raise Exception ('troppi pochi elementi per fare la previsione')

# predizione ------

    for item in value:

# calcolo la somma deiprimi 24=n

      if (k < self.n-1):

        if (precedente == None):

          precedente = item

        else :

          differenza = differenza + (item - precedente)

          k += 1

          precedente = item

# calcolo la predizione poi la sommo alla somma dei dati precedenti

      else:
        
        predizione = item + differenza/k

        differenza = differenza + (predizione - item)

        predizioni.append(int(predizione))

        k += 1

        precedente = item

    self.file = value[self.n:k+1]

    return predizioni

  def errore_medio(self):

# init --------

    predizioni = self.predict()

    lista_errore = []

    i = 0

    errore = 0

# ciclo che calcola la differenza tra le predizioni e i valori reali

    for item in predizioni:

      errore = item - self.file[i]

#se la differenza è negativo lo rendo positivo

      if errore < 0:

        errore = errore * (-1)

      i += 1

      lista_errore.append(int(errore))

# ritorno la somma delle differenze fratto il numero dei dati

    return (sum(lista_errore))/i


ris = Model("shampoo_sales.csv")

print("l' errore medio è :")

print(ris.errore_medio())


    















