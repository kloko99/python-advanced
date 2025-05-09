import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100 * np.pi, 8_000_000)
y = np.sin(x)

noise = np.random.normal(0.3, size=x.shape)
y_noise = y + noise

plt.plot(x, y_noise)
plt.show()
