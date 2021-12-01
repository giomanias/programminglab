#Implementare una funzione (simile a quella creata le lezioni precedenti) che ritorni una lista i cui elementi saranno le date delle vendite del file shampoo sales.csv. Attenzione: Avevate usato la funzione float per convertire i prezzi da stringhe a valori numerici. Questa volta dovrete usare un’altra funzione:

#creo la classe
class CSVFile():

  #inizializzo la classe
  def __init__(self,name):

    self.name = name
     
    #se l argomento non è una stringa alzo un eccezzione
    if not isinstance(name,str):

      print('non è una stringa')

    #creo una funzione che ritorni le date delle vendite
    def get_data(name):

      #apro il file con il nome my_file
      my_fyle = open('shampoo_sales.csv')

      for line in my_fyle:

        elments = line.split(',')

        if elemen






