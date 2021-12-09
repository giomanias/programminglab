#esercizio lezione 4
#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista 
#di liste, ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]

#esercizio lezione 5 parte 1
#Modificate l’oggetto CSVFile della lezione precedente in modo che stampi a  schermo un messaggio di errore se si cerca di aprire un file non esistente.

#esercizio  lezione 5 parte 2
#Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in  modo che converta automaticamente a numero tutte le colonne tranne la prima (della data). Poi, aggiungete questi due campi al file “shampoo_sales.csv”:
# /01-01-2015 , 01-02-2015,ciao/

#-------------------------------------------------------------
#creo una classe csv
class CSV():
  
  #inizializzo la classe
  def __init__(self,name):

    self.name = name

  def get_data(self):
    
    #provo ad aprire il file
    try:
      open('mio file')

    except Exception as e:

    #se non riesc o ad aprire il file ne uso come default

      print('impossibile aprire il file , uso un file come default:')
      my_file = open ('shampoo_sales.csv','r')


    #creo una lista vuota per metterci dentro i file
    lista = []


    for line in my_file:

      elements = line.split(',')

      if (elements[0] != 'Date'):

        lista.append(elements)

    return lista    

#creo una sottoclasse di CSV
class NumericalCSV(CSV):

  def get_data(self):

    #accedo alla funzione padre con super
    mia_stringa = super().get_data()
    #preparo una lista dove salvare i dati
    numerical_row = []
    for elements in my_file:

      numerical_row.append(float(elements[0]))
  
    return numerical_row
  

#OUTPUT
file = CSV('shampoo_sales.csv')
risultato=file.get_data()
print(risultato)
file1 = NumericalCSV('shampoo_sales.csv')
risultato1 = file1.get_data()
print(risultato1)
