from PIL import Image
import cmath
import numpy as np
import cv2
from matplotlib import pyplot as plt

pi2 = cmath.pi * 2.0

def DFT2D(image):
    global M, N
    (M, N) = image.size
    dft2d = [[0.0 for k in range(M)] for l in range(N)]
    pixels = image.load()
    for k in range(M):
        print(k)
        for l in range(N):
            sum = 0.0
            for m in range(M):
                for n in range(N):
                    (L) = pixels[m, n]
                    e = cmath.exp(- 1j * pi2 * (float(k * m) / M + float(l * n) / N))
                    sum += L * e
            dft2d[l][k] = sum / M / N
    return (dft2d)

def IDFT2D(dft2d):
    (dft2d) = dft2d
    global M, N
    image = Image.new("L", (M, N))
    pixels = image.load()
    for m in range(M):
        print(m)
        for n in range(N):
            sum = 0.0
            for k in range(M):
                for l in range(N):
                    e = cmath.exp(1j * pi2 * (float(k * m) / M + float(l * n) / N))
                    sum += dft2d[l][k] * e
            L = int(sum.real+ 0.5)
            pixels[m, n] = (L)
    return image





def filtro(dft2d):
    (dft2d) = dft2d
    global M, N
    dft2dTemp =[[0.0 for k in range(M)] for l in range(N)]

    for m in range(M):
        print(m)
        for n in range(N):
            sum = dft2d[n][m]

            if sum.real < 0:
                sum.real = 0
            dft2dTemp[n][m]=  sum
    return dft2dTemp

imageFrequency = DFT2D(Image.open("input.png"))

# imageFiltrada  = filtro(imageFrequency)


image = IDFT2D(imageFrequency)



image.save("output.png", "PNG")
print(image)
dft_shift =(np.fft.fftshift(imageFrequency))
magnitude_spectrum = 10*np.log(np.abs(dft_shift))
magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
cv2.imshow("saida.png", magnitude_spectrum)
cv2.waitKey(0)
cv2.destroyAllWindows()
