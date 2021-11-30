from matplotlib.pyplot import *
from math import cos,sin,pi,radians
from numpy import arange

class Projectile():
  """Classe permettant la création des projectiles."""

  g = 9.80665
  nb_projectile = 0

  def __init__(self,norme,angle,hauteur):
    self.norme = norme
    self.angle = angle
    self.hauteur = hauteur
    Projectile.nb_projectile += 1

  def calcul_position(self):
    loop = True
    liste_des_x_de_P = [0]
    liste_des_y_de_P = [self.hauteur]
    t = 1

    while loop:
      vxt = self.norme*cos(radians(self.angle))
      vyt = self.norme*sin(radians(self.angle))-(Projectile.g*t)

      xt = vxt*t
      yt = (-1/2)*Projectile.g*(t**2)+vyt*t+self.hauteur

      if yt >= 0:
        liste_des_x_de_P.append(xt)
        liste_des_y_de_P.append(yt)
      else: loop = False

      t += 0.01

    return liste_des_x_de_P , liste_des_y_de_P

  def affichage(self):
    liste = self.calcul_position()
    print(liste)
    plot(liste[0],liste[1])
    show()

A = Projectile(100,65,100)
B = Projectile(150,65,8)

A.affichage()
B.affichage()


