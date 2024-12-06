import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ["A", "B", "C", "D"]
valores = [10, 15, 7, 10]

# Crear gráfico de barras
plt.bar(categorias, valores, color="skyblue")
plt.title("Gráfico de Barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.show()