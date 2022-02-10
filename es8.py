
from matplotlib import pyplot

class Model():

  def __init__(self,file,diff=0):

    self.file = file

    self.diff = diff

  def fit(self):

    val = None
    inc = 0
    ultimo = 0
    n = 0
    sudd = 1

    for item in self.file:

      if (n == 3):

        self.diff = inc/n

        inc = 0

        n = 0

        val = item

        sudd += 1

      else:

        if (val != None):

          inc = inc + (item - val)

          val = item

          n += 1
      
        else:

          val = item
      
    return (self.diff+(inc/(n)))/sudd

  def predict(self):

    return (self.fit()+self.file[-1])


lista = [8,19,31,41,50,52,60]

previsione = Model(lista)

print(previsione.predict())

pyplot.plot(lista + [previsione], color='tab:red')
pyplot.plot(lista,color='tab:blue')

pyplot.show()




