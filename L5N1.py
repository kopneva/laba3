import numpy as np

a = 0.3
b = -21.17

y = (np.power(a + 1.5, 1/3) + np.power(a - b, 8) - b / np.arcsin(np.abs(np.power(a, 2))))

print(y)
