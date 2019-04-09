from PIL import Image
import cmath
pi2 = cmath.pi * 2.0

def DFT2D(image):
    global M, N
    (M, N) = image.size # (tamanho em x, y)
    dft2d_red = [[0.0 for k in range(M)] for l in range(N)] 
    dft2d_grn = [[0.0 for k in range(M)] for l in range(N)] 
    dft2d_blu = [[0.0 for k in range(M)] for l in range(N)] 

    return (dft2d_red, dft2d_grn, dft2d_blu)
        
def IDFT2D(dft2d):

    return image

# TEST
# Abre a imagem
imgOpen = Image.open("horizontal_lines.jpg)
