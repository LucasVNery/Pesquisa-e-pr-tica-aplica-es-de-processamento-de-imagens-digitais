# Detector de Bordas Canny

Projeto simples de Computação Gráfica que implementa detecção de bordas em imagens usando o algoritmo Canny do scikit-image.

## O que faz?

Este programa permite carregar qualquer imagem e visualizar suas bordas detectadas usando o filtro Canny com diferentes níveis de sensibilidade.

## Sobre o Algoritmo Canny

O filtro Canny é um detector de bordas multi-estágio considerado um dos melhores algoritmos de detecção de bordas. Ele funciona através de:

1. **Suavização Gaussiana**: Reduz o ruído da imagem
2. **Cálculo de Gradientes**: Identifica áreas de mudança rápida de intensidade
3. **Supressão de Não-Máximos**: Afina as bordas para linhas de 1 pixel
4. **Limiarização por Histerese**: Elimina bordas fracas e mantém bordas fortes

### Parâmetro Principal: Sigma (σ)

- **σ baixo (1)**: Detecta mais detalhes, incluindo bordas finas
- **σ alto (3)**: Detecta apenas bordas mais evidentes, ignorando detalhes finos e ruído

## Estrutura do Projeto

```
atv-ead/
├── canny_edge_detector.py    # Programa principal
├── requirements.txt           # Dependências do projeto
└── README.md                  # Este arquivo
```

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas Python: numpy, matplotlib, scikit-image

## Instalação

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Como Usar

### Comando Básico

```bash
python canny_edge_detector.py <caminho_da_imagem>
```

### Exemplos

```bash
# Windows
python canny_edge_detector.py foto.jpg
python canny_edge_detector.py C:\Users\Desktop\imagem.png

# Linux/Mac
python canny_edge_detector.py imagens/foto.jpg
python canny_edge_detector.py ~/Downloads/paisagem.png
```

### Formatos Suportados

O programa aceita os principais formatos de imagem:
- JPG / JPEG
- PNG
- BMP
- TIFF
- GIF

## O que o Programa Faz

1. **Carrega a imagem** fornecida via linha de comando
2. **Converte para escala de cinza** (se a imagem for colorida)
3. **Aplica o detector Canny** com dois valores de sigma diferentes
4. **Exibe 3 visualizações**:
   - Imagem original em escala de cinza
   - Bordas com σ=1 (detecção sensível)
   - Bordas com σ=3 (detecção suavizada)

## Interpretando os Resultados

| Sigma | Características | Melhor para |
|-------|----------------|-------------|
| σ=1 | Detecta bordas finas e detalhes | Imagens nítidas, documentos, desenhos |
| σ=3 | Ignora ruído, bordas mais limpas | Fotos naturais, imagens com textura |

## Referências

- [Scikit-Image Canny Documentation](https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.canny)
- Canny, J., A Computational Approach To Edge Detection, IEEE Trans. Pattern Analysis and Machine Intelligence, 8:679-714, 1986
