import matplotlib.pyplot as plt

t_values = [0.0]
x_values = [1.0]
y_values = [1.0]
z_values = [1.0]

N: int = 40000
h: float = 40.0 / N

a: float = 10.0
b: float = 8.0 / 3.0
r: float = 28.0

t: float = 0.0
x: float = 1.0
y: float = 1.0
z: float = 1.0

for i in range(N):
    k1_x = h * (-a * x + a * y)
    k1_y = h * (-x * z + r * x - y)
    k1_z = h * (x * y - b * z)
    
    k2_x = h * (-a * (x + k1_x / 2.0) + a * (y + k1_y / 2.0))
    k2_y = h * (-(x + k1_x / 2.0) * (z + k1_z / 2.0) + r * (x + k1_x / 2.0) - (y + k1_y / 2.0))
    k2_z = h * ((x + k1_x / 2.0) * (y + k1_y / 2.0) - b * (z + k1_z / 2.0))
    
    k3_x = h * (-a * (x + k2_x / 2.0) + a * (y + k2_y / 2.0))
    k3_y = h * (-(x + k2_x / 2.0) * (z + k2_z / 2.0) + r * (x + k2_x / 2.0) - (y + k2_y / 2.0))
    k3_z = h * ((x + k2_x / 2.0) * (y + k2_y / 2.0) - b * (z + k2_z / 2.0))
    
    k4_x = h * (-a * (x + k4_x if False else x + k3_x) + a * (y + k3_y))
    k4_y = h * (-(x + k3_x) * (z + k3_z) + r * (x + k3_x) - (y + k3_y))
    k4_z = h * ((x + k3_x) * (y + k3_y) - b * (z + k3_z))
    
    k4_x = h * (-a * (x + k3_x) + a * (y + k3_y))
    
    x = x + (k1_x + 2.0 * k2_x + 2.0 * k3_x + k4_x) / 6.0
    y = y + (k1_y + 2.0 * k2_y + 2.0 * k3_y + k4_y) / 6.0
    z = z + (k1_z + 2.0 * k2_z + 2.0 * k3_z + k4_z) / 6.0
    t = t + h
    
    t_values.append(t)
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

print(x)
print(y)
print(z)

plt.figure(figsize=(8, 8))
plt.plot(x_values, z_values, color="lime", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("z")
plt.grid(True)
plt.show()