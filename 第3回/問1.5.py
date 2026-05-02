import numpy as np
import matplotlib.pyplot as plt

x_values = [0.0]
y_values = [1.0]
y_flog_values = [1.0]

x: float = 0.0
y: float = 1.0
v: float = 0.0
N: int = 100
h: float = 10 / N

print("前進オイラー法")
print("-----------------")
for i in range(N):
  dy_dx = v
  dv_dx = -y
  y = y + (h * dy_dx)
  v = v + (h * dv_dx)
  x = x + h
  x_values.append(x)
  y_values.append(y)
  print(y)
print("-----------------")

x: float = 0.0
y: float = 1.0
v: float = 0.0

dy_dx = v
dv_dx = -y
y_old = y
v_old = v
y = y + h * dy_dx
v = v + h * dv_dx
x = h
y_flog_values.append(y)

print("リープ・フロッグ法")
print("-----------------")
for i in range(2, N+1):
  dy_dx = v
  dv_dx = -y
  y_old, y, v_old, v = y, y_old + (2 * h * dy_dx), v, v_old + (2 * h * dv_dx)
  x = x + h
  y_flog_values.append(y)
  print(y)
print("-----------------")

x_exact = np.linspace(0, 10, 200) 
y_exact = np.cos(x_exact)

plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label="Forward Euler method", color="green", marker="o", alpha=0.5)
plt.plot(x_values, y_flog_values, label="Leapfrog method", color="red", marker="x", alpha=0.5)
plt.plot(x_exact, y_exact, label="Exact solution", color="blue", linestyle="--")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
