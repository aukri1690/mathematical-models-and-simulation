x: float = 0.0
y: float = 1.0
v: float = 0.0
N: int = 20
h: float = 10 / N

print("前進オイラー法")
print("-----------------")
for i in range(N):
  dy_dx = v
  dv_dx = -y
  y = y + (h * dy_dx)
  v = v + (h * dv_dx)
  x = x + h
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

print("リープ・フロッグ法")
print("-----------------")
for i in range(2, N+1):
  dy_dx = v
  dv_dx = -y
  y_old, y = y, y_old + (2 * h * dy_dx)
  v_old, v = v, v_old + (2 * h * dv_dx)
  x = x + h
  print(y)
print("-----------------")
