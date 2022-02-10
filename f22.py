class Calcolatrice():

  def __init__(self,a,b):

    self.a = a
    self.b = b
  
  def somma(self):

    return  (self.a + self.b)
  
  def sottrazzione(self):

    if(self.a<self.b):
      return self.b-self.a

    else:
      return self.a-self.b

  def moltiplicazione(self):

    return self.a * self.b

  def divisione(self):

    if(self.b!=0):

      return self.a/self.b
  
  def potenza(self):
    
    acc = 1

    c = self.b

    if (c == 0):

      return 1

    else:

      while(c != 0):

        acc = acc * self.a

        c = c -1

    return acc

  def modulo(self):

    if (self.a < 0):

      return (self.a * -1)
    
    else:
      return self.a
    
    if (self.a < 0):

      return (self.b * -1)

    else: 
      return self.b

  def radice(self):

    if (self.b == 0):

      return "impossibile"

    if (self.a > 0):

      radice = pow(self.a,1/(self.b))

      return radice
    
    else:

      return "impossibile"


class Test(Calcolatrice):

  def __init__(self,a,b):

    super().__init__(a,b)

  def testing(self):

    

    if  (super().somma()) != 4:

      raise Exception('la somma non è giusta')

    else:

      print('la somma è giusta')

    if (super().sottrazzione()) != 0:

      raise Exception('la sottrazzione è sbagliata')
a = 2

b = 2

calcolo = Calcolatrice(a,b)

test = Test(a,b)

print(test.testing())


print("somma :",calcolo.somma())
print("sottrazzione :",calcolo.sottrazzione())
print("moltiplicazione :",calcolo.moltiplicazione())
print("divisione :",calcolo.divisione())
print("potenza :",calcolo.potenza())
print("modulo :",calcolo.modulo())
print("radice :",calcolo.radice())



