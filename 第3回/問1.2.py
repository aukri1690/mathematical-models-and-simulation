x: float = 0.0
y: float = 1.0
N: int = 5
h: float = 1 / N

for i in range(N):
  dy_dx = y + x**2 - 2*x
  y = y + (h * dy_dx)
  x = x + h
  print(y)