while True:
  try:
    n = int(input())
  except EOFError:
    exit(0)
 
  menor = 0
  for i in range(n):
    t = float(input())
    if menor > t or i == 0:
      menor = t
 
  print(menor)