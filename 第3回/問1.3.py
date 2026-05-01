import math
import matplotlib.pyplot as plt

x_values = [0.0]
y_values = [0.1]
y_exact_values = [0.1]

x: float = 0.0
y: float = 0.1
N: int = 20
h: float = 20 / N

print("前進オイラー法による数値解")
print("-----------------")
for i in range(N):
  dy_dx = y - y**2
  y = y + (h * dy_dx)
  x = x + h
  x_values.append(x)
  y_values.append(y)
  print(y)
print("-----------------")

x: float = 0.0
y: float = 0.1

print("求積解")
print("-----------------")
for i in range(N):
  y_exact = 1.0 / (1.0 + ((1.0 / y) - 1.0) * math.exp(-x))
  x = x + h
  y_exact_values.append(y_exact)
  print(y_exact)
print("-----------------")

plt.figure(figsize=(10, 5))
plt.plot(x_values, y_exact_values, label="numerical solution", color="blue", linestyle="--")
plt.plot(x_values, y_values, label="Forward Euler method", color="green", marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()