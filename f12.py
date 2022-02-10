
from datetime import datetime 

class CSV:

  def __init__(self,file):

    self.file = file

  def get_data_vendite(self):

    data_vendite = []
    
    myfile = open(self.file)

    for line in myfile:

      element = line.split(',')

      if element[0] != 'Date':

        date = datetime.strptime( element[0], '%d-%m-%Y')

        data_vendite.append(date)
      
    for data in data_vendite:

      print(data.strftime('%d-%m-%Y'))

    #return value

  def get_data(self):

    n = 0

    myfile = open(self.file)

    values = []

    for line in myfile:

      n = n +1

      elements = line.split(',')

    #vendite = 
      if (elements[0] != 'Date'):

        #my_date = datetime.strptime(elements[0],'%d-%m-%y')

        my_date = elements[1]    #.strip("-")

        values.append(float(my_date))

    return sum(values)/n

file = CSV('shampoo_sales.csv')
risultato=file.get_data()
print(risultato)

print('\n   ')

file1 = CSV('shampoo_sales.csv')
risultato1 = file.get_data_vendite()
print(risultato1)


 


  
  

