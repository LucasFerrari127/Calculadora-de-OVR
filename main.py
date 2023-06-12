Training = float(input('Ingresa tu valor de training only: '))
Hab = float(input('Ingresa el valor de training de la habilidad a activar: '))
Entreno = float(input('Que porcentaje entrenaste? '))
Compromiso = float(input('Cuanto vas a activar de compromiso: '))
Playstyle = float(input('Cuanto vas a activar de playstyle: '))
Loyality = float(input('Cuantos puntos de loyality bonus tenes: '))
Item = float(input('Cuantos puntos de item tenes: '))

def Calcular_Entreno(Training, Entreno):
  Total = Training * (Entreno / 100)
  return Total

def Calcular_Compromiso(Training, Compromiso):
  Total = Training * (Compromiso / 100)
  return Total

def Calcular_Habilidad(Hab, Playstyle):
  Total = (Hab * (Playstyle / 100)) / 8
  return Total

def Calcular_Total(Training, Hab, Entreno, Compromiso, Playstyle, Loyality, Item):
  Total_OVR = Calcular_Entreno(Training, Entreno) + Calcular_Compromiso(Training, Compromiso) + Calcular_Habilidad(Hab, Playstyle) + Training + Item + Loyality
  print('Tu Overall total es: ', Total_OVR)

Calcular_Total(Training, Hab, Entreno, Compromiso, Playstyle, Loyality, Item)