import numpy as np

x = np.arange(7, 16)
y = np.arange(1, 18, 2)
z = np.column_stack((x[::-1], y))

for i, j in z:
    print(" " * i + "*" * j)
for i in range(3):
    print(" " * 13, " || ")

print(" " * 12, end="\======/")
print("")
