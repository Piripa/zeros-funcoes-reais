import math
#Função original
def f(x):
  return math.exp(-1/x) -1/x
def f_linha(x):
  return (math.exp(-1/x) + 1 ) * (1/x**2)

#Função de iteração
def phi(x):
  return x - f(x) / f_linha(x)

#Aporixmação inicial
x_k = 1

#Erro
erro = 0.00009

#Inicia a contagem das iterações
k = 0

while abs(f(x_k)) > erro :
  x_k = phi(x_k)
  k = k+1

print("A solução encntrada foi" , x_k)
print("O número de iterações foi ", k )