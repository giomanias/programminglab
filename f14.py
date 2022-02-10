
class Automobile:

  def __init__(self,modello,marca ,targa):

    self.modello = modello
    self.targa = targa
    self.marca = marca

  def __str__(self):

    print('modello : {}'.format(self.modello))
    print('marca : {}'.format(self.marca))
    print('targa : {}'.format(self.targa))

  def parla(self):

    return('broom broom')

  def confronta(self,auto):

    return auto

    #if (self.modello == modello):

      #print('il modello è uguale :{}'.format(modello))
    
    #if (self.marca == marca):

      #print('la marca è uguale :{}'.format(marca))

    
auto1 = Automobile('y','lancia','213hj')

auto2 = Automobile('y1','lancia','214hj')

print(auto1.__str__())
print(auto1.parla())
print(auto1.confronta(auto2))


  