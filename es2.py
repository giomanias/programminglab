#Implementare una funzione (simile a quella creata le lezioni precedenti) che ritorni una lista i cui elementi saranno le date delle vendite del file shampoo sales.csv. Attenzione: Avevate usato la funzione float per convertire i prezzi da stringhe a valori numerici. Questa volta dovrete usare un’altra funzione:


from datetime import datetime


my_file = open('shampoo_sales.csv', 'r')

data_vendite = []
value = []

#creo la funzione
def funz(file):

  for line in file:
    
    #faccio lo split in ogni virgola
    elements = file.split(',')
    
    #la prima la metto nella lista vendite
    if elements[0] != 'Date':
      
      value = elements[0]
      
      data_vendite.append(float(value))

  return data_vendite
      
  


risultato = funz('shampoo_sales.csv')

print(risultato)











