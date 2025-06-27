# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 16:01:33 2025

@author: Mauricio Cardoso
"""

import numpy as np

def integral(x):
  return np.exp(-x**2/2)

def simpson(n, sup, inf):
  print("simpson")
  

def trapezoid(h, sup, inf):
  h = (sup - inf)/n
  aux = inf
  multiplier = h/2
  total_sum = 0
  print("\n")
  for i in range(n+1):  
    value = integral(aux)
    if i != 0:
      value = value*2
      
    aux = aux+h
    print(f"f(x{i}): ", value)
    total_sum = total_sum + value
  print("\n")
  print("Resultado: ", total_sum*multiplier)

def solve_method(option, n, sup, inf):
  match option:
    case 1:
        simpson(n, sup, inf)
    case 2:
        trapezoid(n, sup, inf)

while True:
  print("------------------------------------------------")
  print("Escolha um dos métodos abaixo:")      
  print(" 1 - Simpson")
  print(" 2 - Trapézios")
  print("------------------------------------------------")
  method = int(input("Método: "))
  n = int(input("Item de subdivisão: "))
  
  if method not in [1, 2]:
    print("\nErro: Escolha inválida! Digite 1 ou 2.\n")
  elif method == 1 and n % 2 != 0:
    print("\nPara o metodo de Simpson, o número de subdivisões deve ser par.\n")
  else:  
    superior_lim = int(input("Entre com o limite superior: "))
    inferior_lim = int(input("Entre com o limite inferior: "))
    if inferior_lim >= superior_lim:
      print("O limite superior deve ser maior que o limite inferior")
    else:
      solve_method(method, n, superior_lim, inferior_lim)
      break

