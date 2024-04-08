import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros de la animación
frames = 100  # Número de frames
duration = 10  # Duración en segundos
fps = frames / duration  # Fotogramas por segundo

# Definir el tamaño del área
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# Función para actualizar la animación en cada frame
def update(frame):
    Z = np.sin(X - frame * 0.1) + np.cos(Y - frame * 0.1)
    ax.clear()
    ax.plot_surface(X, Y, Z, cmap='coolwarm')
    ax.set_title(f'Ondas Sísmicas en el Tiempo')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Amplitud')
    return ax

# Configurar la figura y el eje tridimensional
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
anim = FuncAnimation(fig, update, frames=frames, interval=1000/fps)

# Mostrar la animación
plt.show()
