import numpy as np

x: float = 0.0
y: float = 1.0
N: int = 10
h: float = 2 / N

print("前進オイラー法")
print("-----------------")
for i in range(N):
  dy_dx = -y - np.pi * np.exp(-x) * np.sin(np.pi * x)
  y = y + (h * dy_dx)
  x = x + h
  print(y)
print("-----------------")

x: float = 0.0
y: float = 1.0
N: int = 10
h: float = 2 / N

dy_dx = -y - np.pi * np.exp(-x) * np.sin(np.pi * x)
y_old = y
y = y + h * dy_dx
x = h

print("リープ・フロッグ法")
print("-----------------")
print(y)
for i in range(2, N + 1):
  dy_dx = -y - np.pi * np.exp(-x) * np.sin(np.pi * x)
  y_old, y = y, y_old + (2 * h * dy_dx)
  x = x + h
  print(y)
print("-----------------")