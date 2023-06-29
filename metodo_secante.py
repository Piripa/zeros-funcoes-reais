import math

#Função original
def f(x):
  return math.exp(-1/x) -1/x

#Condições iniciais:
x_0 = 1
x_1 = 2

#Erro
erro = 0.00009

#Contagem
k = 0

while abs(f(x_1)) > erro:
  if(f(x_1) < 0):
    break
  x_2 = ((x_0*f(x_1)) - (x_1*f(x_0))) / (f(x_1) - f(x_0))
  x_0 = x_1
  x_1 = x_2

  k = k+1

print("A solução encontrada foi" , x_2)
print("O número de interações foi ", k )