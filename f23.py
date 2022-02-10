
class CSVFile:

  def __init__(self,file):

    self.file = file

  def get_data(self,start=None,end=None):

    value = []

    myfile = open(self.file)

    for line in myfile:

      elements = line.split(',')

      if elements[0] != 'Date':

        value.append(float(elements[1]))

    self.file = value

    return self.file[start:end]

  def sum_list(self,file):

    return sum(file)


lista = CSVFile("shampoo_sales.csv")

lista2 = CSVFile("shampoo_sales.csv")

primo = (lista.get_data())

ris1 = (lista.sum_list(primo))

print((lista.sum_list(primo)))

secondo = (lista2.get_data())

ris2 = (lista2.sum_list(secondo))

print((lista2.sum_list(secondo)))

if primo >= secondo:

  if ris1 >= ris2:

    print('tutto apposto')

  else:

    print('sbagliato')

else: 

  if ris2 > ris1:

    print('tutto apposto')

  else:

    print('sbagliato')




















