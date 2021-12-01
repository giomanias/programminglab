#Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in  modo che converta automaticamente a numero tutte le colonne tranne la prima (della data). Poi, aggiungete questi due campi al file “shampoo_sales.csv”: e gestite gli errori che verranno generati in modo che le linee vengano saltate senza bloccare il programma ma che venga stampato a schermo l’errore

class CSVFile():
  values = []
#creo classe 
  def __init__(self , name):

    self.name = name

#estendo l oggetto

class NumericalCSVFile(CSVFile):
  
  def converti(self):

    for line in self:
      
      elements=line.split(',')

      if (elements[0] != "Date"):

        value = elements[1]
        values.append(float(value))


