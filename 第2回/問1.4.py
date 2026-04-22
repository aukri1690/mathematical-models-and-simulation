a: float = 0
b: float = 0
c: float = 0

for i in range(2):
  a_new = (1 - 0.8 * b - 2 * c) / 4
  b_new = (0.5 - 0.4*a - 0.6*c) / 1
  c_new = (4 - 0.5*a - 3.5*b) / 5

  a = a_new
  b = b_new
  c = c_new

print(a)
print(b)
print(c)