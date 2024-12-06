import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
datos = np.random.rand(10, 10)

# Crear mapa de calor
plt.imshow(datos, cmap="viridis", interpolation="nearest")
plt.title("Mapa de Calor")
plt.colorbar()
plt.show()
