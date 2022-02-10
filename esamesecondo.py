#Vogliamo calcolare la differenza degli elementi di una lista. In genere questa operazione si chiama “diff” in vari framework di calcolo numerico, e così la chiameremo anche noi. La nostra operazione “diff” avrà quindi in input una lista di valori numerici ed in output la lista delle loro differenze.
#Aggiungeremo anche un parametro di nome “ratio”, che permetta di riscalare le differenze (ovvero la differenza tra gli elementi va divisa per la “ratio”). Tale parametro deve avere un valore di default pari a 1.

#Exception è bulitin quindi non serve definire una classe padre
class ExamException(Exception):

        pass

class Diff:

  #se metto ratio=1 il valore di default sara 1

  def __init__(self,ratio=1):

    self.ratio=ratio
  
  #inizializzo all interno di compute le variabili che mi servono E NON FUORI
  
  def compute(self,lista):

    #devo alzare l eccezione scrivendo prima ExamException

    if (lista == None):

      raise ExamException('inserire una lista')
    
    lunghezza=len(lista)

    if (len(lista) < 2):

      raise ExamException('lista ha troppi pochi elementi')
    
    i=0
    differenza=0
    value=[]

    while(i<(lunghezza-1)):

      differenza = lista[i+1] - lista[i]

      differenza = differenza/self.ratio

      value.append(differenza)

      i=i+1

    return value

diff = Diff()

result = diff.compute([2,4,8,16])

print(result)



