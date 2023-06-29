import math

def f(x):
  return math.exp(-1/x) - 1/x
#dados iniciais
#raízes
a = 1
b = 2

#Media
M =( a + b )/ 2

#erro
erro = 0.00009

#contagem das iterações
k = 0

while abs(f(M)) > erro:
  M = (a*f(b) - b*f(a)) / (f(b) - f(a))
  if f(a)*f(M)<0:
    b = M
  else:
    a = M
  k = k+1

print("A raiz esolhida foi: " , M)
print("A quantidade de repetições: " , k)