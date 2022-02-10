class Model():

  def __init__(self,file,n=24):

    self.file = file

    self.n = n

  def fit(self):

  #init -------
    
    value =[]

    predizioni = []

    precedente = None

    differenza = 0

    k = 0

    sudd = 0

    predizione = 0

    myfile = open(self.file)

    for line in myfile:

      elements = line.split(',')

      if elements[0] != 'Date':

        value.append(float(elements[1]))

    for item in value:

      k += 1

      if (k <= self.n):

        if (precedente == None):

          precedente = item
        
        else:

          differenza = differenza + (item -precedente)

          precedente = item
      
      else:

        sudd += 1

        k += 1

        if(sudd != 4):

          predizione = item + (differenza/k-1)

          precedente = item











    
