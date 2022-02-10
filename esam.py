from datetime import datetime

class ExamException(Exception):

  pass

class CSVTimeSeriesFile():

  def __init__(self,name):

    self.name = name

  def get_data(self):

    #controllo se il file può essere aperto o se esiste
    try:

      myfile = open(self.name)
    
    except:

      raise ExamException('il file non è adeguato o non esiste')
    
    #init -------
    value_data = []

    value_passe = []

    value = []

    #variabili per controllare che la lista inizialmente passata sia ordinata in modo crescente------------
    y = 0

    m = 0
    #--------
    i = 0

    k = 0

    j = 0

    anno = 0

    #creazione lista date e lista passeggeri

    #per ogni riga del file lo divido in due parti
    for line in myfile:

      elements = line.split(',')

      if elements[0] != 'date':

        #se non riesco a convertire il numero di passeggeri in un intero aggiungo alla lista zero
        try:

          elements[1] = int(elements[1])
        
        except:

          elements[1] = 0

        #se il numero dei passeggeri è zero,negativo o non esiste aggiungo alla lista zero, altrimenti aggiungo il numero
        if (int(elements[1]) <= 0) :

          value_passe.append(0)

        else:

          value_passe.append(int(elements[1]))

        value_data.append(elements[0])

    #controllo che le date dei valori siano ordinati in modo crescente
    
    #m1 mi serve per il for annidato
    m1 = m
    
    #è il numero di anni presente nel file
    lungy = int(len(value_data)/12)
     
    for y in range(lungy):
      
      #faccio un ciclo con il range e controllo che il mese del valore sia minore del mese del prossimo valore
      for m in range(11):

        data1 = datetime.strptime(value_data[m1],'%Y-%m')

        data1y = data1.year #anno di data1

        data1m = data1.month #mese si data1

        data2 = datetime.strptime(value_data[m1+1],'%Y-%m')

        data2y = data2.year #anno di data2

        data2m = data2.month #mese si data2

        #se l' anno della data1 è maggiore dell' anno della data2 alzo un' eccezzione 
        if data1y <= data2y:

          #se il mese della data1 è maggiore dell mese della data2 alzo un' eccezzione 
          if data1m < data2m:

            pass

          else:
    
            raise ExamException('le date non sono ordinati in modo crescente')

        else:

          raise ExamException('le date non sono ordinati in modo crescente')
    
      m1 += 12

    #lunghezza lista  
    lun = len(value_data)   

    #creazione lista di liste

    limite = lun+(lun/12)

    anni = int(lun)

    for i in range(anni):

      value.append([])
 
      #per ogni lista all' interno della lista aggiungo la data e il numero di passeggeri
      for j in range(1):

        value[i].append(value_data[anno])

        value[i].append(value_passe[anno])

        anno += 1

    #ritorno la lista di liste
    return value

# corpo del programma -------

time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()

#print(time_series)

#funzione che calcola le differenze ------

def compute_avg_monthly_difference(time_series, first_year, last_year):

  #converto la prima data e l'ultima in interi

  data_inizio = datetime.strptime(time_series[0][0],'%Y-%m')

  data_inizio = data_inizio.year

  data_fine =  datetime.strptime(time_series[143][0],'%Y-%m')

  data_fine = data_fine.year

  #se l' anno inserito è minore di 1949 o maggiore di 1960    chiedo di reinserire una data che stia all' interno dell' intervallo
  
  if int(first_year) < data_inizio or int(first_year) > data_fine:

    raise ExamException("inserire un' anno tra {} e {}".format(data_inizio,data_fine))

  if int(last_year) < data_inizio or int(last_year) > data_fine:

    raise ExamException("inserire un' anno tra {} e {}".format(data_inizio,data_fine))

  # init ------
  #liste

  lista = []

  lista_supp = []

  lista_diff = []

  #indici per cicli

  i = 0

  k = 1

  j = 0

  s = 0

  #variabili
  valore = 0

  differenza = 0

  anno = 0

  anno_base = 0

  # trasformo last_year e first_year in interi se mi vengono passati come stringa o float

  first_year = int(first_year)

  last_year = int(last_year)

  #se non è possibile convertire last_year o first_year in un intero alzo un eccezzione

  if (type(first_year) != int) or (type(last_year) != int):

    raise ExamException("impossibile fare la previsione, inserire un' anno ")

  #calcolo anno base

  anno_base = first_year - 1949

  anno_base = anno_base * 12

  #calcolo gli anni su cui devo fare la differenza
  anni = last_year - first_year
  
  #salvo il valore di anni perchè mi servire nel ciclo che calcola le differenze
  n = anni

  #ciclo che costruisce la lista dove registro le differenze tra i vari anni

  for i in range(anni):

    k = 0

    for k in range(12):

      # se uno degli elementi è zero allora aggiungo alla lista uno zero al posto della differenza se il range di anni è =2

      if (time_series[(anno_base)+12][1] == 0) or (time_series[(anno_base)][1] == 0) : 

        differenza = 0       

        anno_base += 1

        anni += 1
      
      else:
        
        differenza = (time_series[(anno_base)+(12)][1]- time_series[(anno_base)][1])

        anno_base += 1

        anni += 1

      lista_supp.append(differenza)

  #calcolo le differenze e le aggiungo alla lista_diff 

  #per ogni mese dell' anno calcolo la differenza con il valore dello stesso mese dell' anno seguente
  while s < 12:

    m = s

    valore = 0

    for i in range(n):

      valore = valore + lista_supp[m]

      m += 12
    
    #divido la differenza per il numero di osservazioni
    lista_diff.append(valore/n)

    s += 1
       
  return  lista_diff  

# corpo del programma -------

first_year = '1949'

last_year = '1951'

ris = compute_avg_monthly_difference(time_series,first_year,last_year)

print('differenza tra {} e {} :'.format(first_year,last_year))

print(ris)

