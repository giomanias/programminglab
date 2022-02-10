import numpy as np

class LinearModel:

  def __init__(self,angolar_coeff=None,intercept=None,train_data=None):

    self.angolar_coeff = angolar_coeff

    self.intercept = intercept

    self.train_data = train_data

  def fit(self,train_data):

     #init---

    z = self.train_data

    q = 0   #valore intercetta

    den = 0  #denominatore

    cv = 0   #covarianza

    dx = 0   #deviazione xi

    dy = 0   #deviazione y

    sommax = np.sum(z[:,0])

    ux = np.mean(z[:,0])
    
    xn = len(z[:,0])
    
    xi = 0

    #y----------somma,media,n

    sommay = np.sum(z[:,1])

    uy = np.mean(z[:,1])
    
    yn = len(z[:,1])

    yi = 0

    n = xn

    n1 = n
    n2 = n

    #numeratore m

    while (n>=0):

      xi = 0
      yi = 0

      n = n-1

      xi = z[n-1,1] - ux

      yi = z[n-1,0] - uy

      cv = cv + (xi * yi)
    
    #denominatore m

    while(n1>=0):

      xi = 0
      yi = 0

      n1 = n1 - 1

      xi = z[n-1,1] - ux

      dx = dx + xi

      yi = z[n-1,0] - uy

      dy = dy + yi

    dx = dx * dx  #varianza x

    dy = dy * dy  #varianza y

    den = dx * dy

    den = pow(den,1/2)   #denominatore

    pxy = cv/den  # pxy

    while (n2>=0):

      xi = 0
      yi = 0

      n2 = n2 - 1

      xi = z[n-1,1] - ux

      dx = dx + pow(dx,2)

      yi = z[n-1,0] - uy

      dy = dy + pow(dy,2)
    
    dx = dx/(xn-1)

    sx = pow(dx,1/2)   #devi x

    dy = dy/(yn-1)

    sy = pow(dy,1/2)   #devi y

    m = (sx/sy)*pxy

    self.angolar_coeff = m

    q = uy + (m * ux)

    self.intercept = q


  def predict(self,xp):

    if (self.intercept == None):

      raise Exception('il valore dell intercetta è None')

    if (self.angolar_coeff == None):

      raise Exception ('il valore del coefficente angolare è None')

    else:

      nn = len(xp[:,1])  

      while (nn >= 0 ):

        xp[nn-1,1] = self.angolar_coeff * xp[nn-1,1] + self.intercept
  
    return xp



x = np.array([[1,2],[3,4],[5,6]])

ris = LinearModel(0,0,x)

print(ris.predict(x))
    