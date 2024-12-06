import matplotlib.pyplot as plt

# Datos de ejemplo
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

# Crear gráfico de dispersión
plt.scatter(x, y, color="purple")
plt.title("Gráfico de Dispersión")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()