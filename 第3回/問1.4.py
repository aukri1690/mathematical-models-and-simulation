import numpy as np
import matplotlib.pyplot as plt

x_values = [0.0]
y_values = [1.0]
y_flog_values = [1.0]
y_exact_values = [1.0]

N: int = 100
h: float = 2 / N

x: float = 0.0
y: float = 1.0

print("前進オイラー法")
print("-----------------")
for i in range(N):
  dy_dx = -y - np.pi * np.exp(-x) * np.sin(np.pi * x)
  y = y + (h * dy_dx)
  x = x + h
  x_values.append(x)
  y_values.append(y)
  print(y)
print("-----------------")

x: float = 0.0
y: float = 1.0

dy_dx = -y - np.pi * np.exp(-x) * np.sin(np.pi * x)
y_old = y
y = y + h * dy_dx
x = h
y_flog_values.append(y)

print("リープ・フロッグ法")
print("-----------------")
print(y)
for i in range(2, N + 1):
  dy_dx = -y - np.pi * np.exp(-x) * np.sin(np.pi * x)
  y_old, y = y, y_old + (2 * h * dy_dx)
  x = x + h
  y_flog_values.append(y)
  print(y)
print("-----------------")

x: float = 0.0
y: float = 1.0

print("厳密解")
print("-----------------")
for i in range(N):
  y_exact = np.exp(-x) * np.cos(np.pi * x)
  x = x + h
  y_exact_values.append(y_exact)
  print(y_exact)
print("-----------------")

plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label="Forward Euler method", color="green", marker="o", alpha=0.5)
plt.plot(x_values, y_flog_values, label="Leapfrog method", color="red", marker="x", alpha=0.5)
plt.plot(x_values, y_exact_values, label="numerical solution", color="blue", linestyle="--", alpha=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()