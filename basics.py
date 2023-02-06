import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 10000)
y = np.sin(x)

plt.plot(x,y)
plt.show()