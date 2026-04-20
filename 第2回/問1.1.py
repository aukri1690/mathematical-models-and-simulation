import numpy as np

x = np.linspace(0, 1, 128)
y = np.sin(x)

h = 1 / 127

for i in range(1, 127):
    print((y[i + 1] - y[i - 1]) / (h * 2))