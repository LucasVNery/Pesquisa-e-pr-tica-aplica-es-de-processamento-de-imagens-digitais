import numpy as np
import matplotlib.pyplot as plt
from skimage import feature, io, color
import sys
import os

if len(sys.argv) < 2:
    print("Uso: python canny_edge_detector.py <caminho_da_imagem>")
    print("Exemplo: python canny_edge_detector.py imagens/foto.jpg")
    sys.exit(1)

image_path = sys.argv[1]

if not os.path.exists(image_path):
    print(f"Erro: Arquivo '{image_path}' não encontrado!")
    sys.exit(1)

try:
    image = io.imread(image_path)

    if len(image.shape) == 3:
        image = color.rgb2gray(image)

    print(f"Imagem carregada: {image_path}")
    print(f"Dimensões: {image.shape}")

except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
    sys.exit(1)

edges1 = feature.canny(image)
edges2 = feature.canny(image, sigma=3)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Imagem Original', fontsize=20)

ax[1].imshow(edges1, cmap='gray')
ax[1].set_title(r'Canny filter, $\sigma=1$', fontsize=20)

ax[2].imshow(edges2, cmap='gray')
ax[2].set_title(r'Canny filter, $\sigma=3$', fontsize=20)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
