# Modificate l’oggetto CSVFile della lezione precedente in modo che stampi a schermo un messaggio di errore se si cerca di aprire un file non esistente.

class CSVFile():
#creo classe 
  def __init__(self , name):

    self.name = name

#creo la funzione 
  def get_data(self):
    try:
      
      open('mio file')
    except:
      print('il file non esiste allora uso un file come default')
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
    
