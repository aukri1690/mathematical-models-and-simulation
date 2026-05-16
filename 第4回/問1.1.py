import numpy as np
import matplotlib.pyplot as plt

x_values = [0.0]
y_values = [0.3]
y_exact_values = [0.3]

N: int = 100
h: float = 10 / N

a: float = 1.0 / 4.01
b: float = np.pi / 6.0
c: float = 0.6

x: float = 0.0
y: float = 0.3

print("ルンゲ・クッタ法")
print("-----------------")
for i in range(N):
    k1 = h * (a * y + c * np.exp(a * x) * np.cos(x + b))
    k2 = h * (a * (y + k1 / 2.0) + c * np.exp(a * (x + h / 2.0)) * np.cos((x + h / 2.0) + b))
    k3 = h * (a * (y + k2 / 2.0) + c * np.exp(a * (x + h / 2.0)) * np.cos((x + h / 2.0) + b))
    k4 = h * (a * (y + k3) + c * np.exp(a * (x + h)) * np.cos((x + h) + b))
    
    y = y + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    x = x + h
    
    x_values.append(x)
    y_values.append(y)
    print(y)
print("-----------------")

print("厳密解")
print("-----------------")
for i in range(1, N + 1):
    xi = x_values[i]
    y_exact = c * np.exp(a * xi) * np.sin(xi + b)
    y_exact_values.append(y_exact)
    print(y_exact)
print("-----------------")

error_values = np.abs(np.array(y_values) - np.array(y_exact_values))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(x_values, y_values, label="Runge-Kutta method", color="green", marker="o", alpha=0.5)
plt.plot(x_values, y_exact_values, label="Exact solution", color="red", linestyle="--", alpha=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Runge-Kutta method and Exact Solutions")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x_values, error_values, label="Absolute Error", color="red", marker="x")
plt.xlabel("x")
plt.ylabel("Absolute Error")
plt.title("Error")
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.show()