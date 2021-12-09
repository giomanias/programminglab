# Implementare una classe Automobile che presenta i seguenti attributi: casa automo, modello, numero posti, targa. Inoltre, la presente classe deve comprendere i seguenti metodi:  init , metodo per inizializzare una istanza della classe;  str , metodo che stampa tutte le informazioni associate ad una specifica istanza (aka oggetto) della classe Automobile;  parla, metodo che stampa a schermo ”Broom Broom”;  confronta, metodo che, data in ingresso un’altra istanza di Automobile, determina se i due oggetti hanno le stesse informazioni (eccetto per la targa che `e univoca!).


class Automobile():

  def __init__(self , name , marca, clacson , grado , reparto):

    self.name = name
    self.marca = marca
    self.clacson = clacson
    self.grado = grado
    self.reparto = reparto

  
  def __str__(self):

    return 'automobile "{} {}"'.format(self.name , self.marca)
  
  def saluta(self):
    
    print('sono una "{}" il clacson fa"{}""'.format(self.name,self.clacson))

#definisco una sottoclasse
class transformer(Automobile):
  
  def saluta(self):

    print ('mi chiamo "{}" sono un "{}" e la mia arma è "{}"'.format(self.name,self.grado,self.reparto))

try:
  transformer = Transformer("giovanni","soldato semplice","distanza")
  transformer.saluta()

except Exception as e:
  'l errore è "{}"'.format(e)
  





