x: float = 0.0
y: float = 0.0
h: float = 0.2

for i in range(5):
  dy_dx = x + y
  y = y + (h * dy_dx)
  x = x + h
  print(y)