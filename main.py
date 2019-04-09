from PIL import Image
import cmath
pi2 = cmath.pi * 2.0

def DFT2D(image):
    global M, N
    (M, N) = image.size # (tamanho em x, y)

    return (dft2d_red, dft2d_grn, dft2d_blu)
        
def IDFT2D(dft2d):

    return image

# TEST
# Abre a imagem
imgOpen = Image.open("horizontal_lines.jpg)
