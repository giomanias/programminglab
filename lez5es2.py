#Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in  modo che converta automaticamente a numero tutte le colonne tranne la prima (della data). Poi, aggiungete questi due campi al file “shampoo_sales.csv”: e gestite gli errori che verranno generati in modo che le linee vengano saltate senza bloccare il programma ma che venga stampato a schermo l’errore

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
shampoo=CSVFile("sales.csv")
#dichiaro my_data e la associo al metodo get_data della classe CSVFile
my_data=shampoo.get_data()

#stampo a schermo i valori
print(my_data)
    
