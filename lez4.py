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

#creo una lista vuota
    values=[]

#faccio un ciclo che mi splitti il file sulle virgole
    for line in my_file:

      
      elements = line.split(',')

      #if (elements != 'data'):
      values.append(elements)

    my_file.close()
# ritorno i valori del file
    return (values)


#dichiaro shampoo e la associo alla classe  
shampoo=CSVFile("shampoo_sales.csv")
#dichiaro my_data e la associo al metodo get_data della classe CSVFile
my_data=shampoo.get_data()

#stampo a schermo i valori
print(my_data)
    
