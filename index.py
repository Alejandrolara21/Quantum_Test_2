from PIL import Image
import random

ancho, alto = 150, 150

def G0():
    M = [[0]*ancho for j in range(alto)]
    
    numero_aleatorio = random.randint(1, 3)

    for i in range(numero_aleatorio):
        anchoRandom = random.randint(1, ancho-1)
        altoRandom = random.randint(1, alto-1)
        M[anchoRandom][altoRandom] = 1
    return M

def imprimir(G):
    for i in range(alto):
        print(G[i])

def d(C, nutrientes):
    q = 0
    if C == 0 and nutrientes > 0:  # Si hay suficientes nutrientes, crece
        q = 1
    if C == 1:  # Los hongos se dividen cuando alcanzan cierto tamaño
        if nutrientes < 2:  # Si hay pocos nutrientes, muere de hambre
            q = 0
        elif nutrientes > 3:  # Si hay muchos nutrientes, muere de hacinamiento
            q = 0
        else:
            q = 1
    return q

def aplicarReglas(G):
    temp = [[0]*ancho for j in range(alto)]
    for i in range(alto):
        for j in range(ancho):
            C = G[i][j]
            nutrientes = sum([sum([G[(i+x)%alto][(j+y)%ancho] for y in range(-1, 2)]) for x in range(-1, 2)])
            nutrientes -= C  # Restar el valor de la propia celda
            temp[i][j] = d(C, nutrientes)
    return temp

def guardarCuadro(G, personal_index):
    with Image.new('RGB', (ancho, alto), color='white') as img:
        for i in range(alto):
            for j in range(ancho):
                if G[i][j] == 1:
                    img.putpixel((j, i), (0, 0, 0))
        img.save(f"images/cuadro_{personal_index}.jpg")

G = G0()
cuadros = []
for i in range(100):
    guardarCuadro(G, i)
    cuadros.append(Image.open(f"images/cuadro_{i}.jpg"))
    G = aplicarReglas(G)

# Guardamos los cuadros como un archivo GIF
cuadros[0].save('hongos4.gif', save_all=True, append_images=cuadros[1:], duration=200, loop=0)