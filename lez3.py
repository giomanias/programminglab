
#scrivere una funzioni che sommi i valori dell file.shampoo , li trasformi in float e faccia la somma dei valori

def somma_valori_file(my_file):
  values=[]
  for line in my_file:

    elements = line.split(",")
    if (elements[0] != "Date"):

      value = elements[1]
      values.append(float(value))

  my_file.close()
  return (sum(values))

shampoo=open("sales.csv","r")
print(somma_valori_file(shampoo))


  
