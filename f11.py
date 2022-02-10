#Realizzare un programma con le seguenti funzioni per la manipolazione di liste:
#1) stampa, una funzione che stampa il contenuto di una lista passata come argomento;
#2)statistiche, una funzione che riceve una lista e, se `e una lista di interi,ne determini la somma, la media, il minimo ed il massimo degli elementi;
#somma vettoriale, una funzione che riceve in ingresso due liste, determina se sono due liste di interi, se hanno la stessa dimensione e ne calcola la somma vettoriale, poi ritornata come lista, altrimenti ritorna una lista vuota

#dichiaro le mie liste

lista = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista_vuota = []
lista_interi = [1]

#funzione che stampa la lista

def stampa_liste(my_lista):
  print(my_lista) 

#funzione che fa la somma la media  e trova il massimo e il minimo

def statistiche(my_lista):
  i=0
  print('somma',sum(my_lista))
  for item in my_lista:
    i=i+1
  print('media',(sum(my_lista))/i)
  print('massimo',max(my_lista))
  print('minimo',min(my_lista))

#funzione che fa la somma vettoriale di 2 liste

def somma_vettoriale(my_lista,my_lista2):

  i = 0

  somma = 0

  try:

    if (len(my_lista) == len(my_lista2)):

      if(type(my_lista) == type(lista_interi)):

        if (type(my_lista) == type(my_lista2)):
        
          while (i < len(my_lista)):

            somma = my_lista[i] + my_lista2[i]

            lista_vuota.append(somma)

            i += 1

    return lista_vuota

  except:

    return lista_vuota

#provo a richiamare le funzioni e vedo se le liste sono di interi 

try:
  stampa_liste(lista)
  statistiche(lista)
  risultato=somma_vettoriale(lista,lista2)
  print(risultato)

#altrimenti stampo a schermo che non contiene interi

except TypeError:
  print('la mia lista non contiene interi')

  