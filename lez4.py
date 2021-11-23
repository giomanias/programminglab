#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista  di liste, ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ] Provatelo sul file “shampoo_sales.csv”.

class CSVFile():
#creo classe 
  def __init__(self , name):

    self.name = name
#creo la funzione 
  def get_data(self):
    
    my_file=open(self.name,"r")

    values=[]

    for line in my_file:

      elements = line.split(',')

      values.append(elements)

    my_file.close()
    return (values)


    
shampoo=CSVFile("sales.csv")
my_data=shampoo.get_data()

print(my_data)
    
