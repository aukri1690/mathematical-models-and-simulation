x: float = 0.0
y: float = 0.1
N: int = 40
h: float = 20 / N

for i in range(N):
  dy_dx = y - y**2
  y = y + (h * dy_dx)
  x = x + h
  print(y)