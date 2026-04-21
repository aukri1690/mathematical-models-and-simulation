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

theoretical_derivative = np.cos(x[1:127])

errors = np.abs(np.array(numerical_derivative) - theoretical_derivative)

print(errors)

plt.figure(figsize=(10, 6))
plt.plot(x[1:127], errors, color='magenta')
plt.xlabel("x")
plt.ylabel("absolute error")
plt.legend()
plt.grid(True)
plt.show()