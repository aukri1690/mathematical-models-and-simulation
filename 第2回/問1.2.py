import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 128)
y = np.sin(x)

h = 1 / 127

def central_difference_method():
  array = []
  for i in range(1, 127):
    derivative = (y[i + 1] - y[i - 1]) / (h * 2)
    array.append(derivative)
  return array

numerical_derivative = central_difference_method()

plt.figure(figsize=(10, 6))
plt.plot(x[1:127], numerical_derivative, 'go', label="Numerical Derivative (Central Difference)", markersize=4)
plt.plot(x, np.cos(x), 'orange', label="Theoretical solution (cos(x))", alpha=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()