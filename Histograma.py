import matplotlib.pyplot as plt

# Datos de ejemplo
datos = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9]

# Crear histograma
plt.hist(datos, bins=5, color="orange", edgecolor="black")
plt.title("Histograma")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.show()
