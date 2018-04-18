import os
import cv2 as cv
import numpy as np

if __name__ == "__main__":
    a_dir = raw_input()
    for subdir, dirs, files in os.walk(a_dir):
        for file in files:
            putanja = os.path.join(subdir, file)
            img = cv.imread(putanja)

            cX = 0
            cY = 0

            provera = False
            for i in range(1, img.shape[0]):
                for j in range(1, img.shape[1]):
                    if img[i, j][0] == 255:
                        cX = j + 1
                        provera = True
                        break
                if provera == True:
                    break

            if i == 1:
                provera2 = False
                for g in range(img.shape[0]-1, 1, -1):
                    for h in range(img.shape[1]-1, 1, -1):
                        if img[g, h][0] == 255:
                            cX = h + 1
                            provera2 = True
                            break
                    if provera2 == True:
                        break

            provera3 = False
            for l in range(1, img.shape[1]):
                for s in range(1, img.shape[0]):
                    if img[s, l][0] == 255:
                        cY = s + 1
                        provera3 = True
                        break
                if provera3 == True:
                    break
            if l == 1:
                provera4 = False
                for p in range(img.shape[1]-1, 1, -1):
                    for e in range(img.shape[0]-1, 1, -1):
                        if img[e, p][0] == 255:
                            cY = e + 1
                            provera4 = True
                            break
                    if provera4 == True:
                        break


            maks_brojac_ugla = 0
            izadji = False
            for popluprecnik in range (1, 80):
                brojac_ugla = 0
                for ugao in range(0, 720):

                    X = cY + (popluprecnik * np.cos(ugao / (180 / np.pi)))
                    Y = cX + (popluprecnik * np.sin(ugao / (180 / np.pi)))
                    if img[int(X),int(Y)][0] == 0:
                        brojac_ugla = brojac_ugla + 1

                        if maks_brojac_ugla<brojac_ugla:
                            maks_brojac_ugla = brojac_ugla
                    else:
                        brojac_ugla = 0

                if izadji == True:
                    break


            lista2 = []
            for mali_p in range(1, img.shape[0]):
                if len(lista2) > 0:

                    break
                for uglic in range(0, 360):
                    X1 = cY + (mali_p * np.cos(uglic / (180 / np.pi)))
                    Y1 = cX + (mali_p * np.sin(uglic / (180 / np.pi)))

                    lista2.append(img[int(X1), int(Y1)][0])
                for li in range(len(lista2) - 1):
                    if (lista2[li] == 0 and lista2[li + 1] == 0):
                        break

                    elif li == len(lista2) - 2:
                        lista2 = []

                        break


            lista1 = []
            for polupre in range(mali_p+10, img.shape[0]):
                if len(lista1) > 0:
                    break
                for uglic in range(0, 360):
                    X1 = cY + (polupre * np.cos(uglic / (180 / np.pi)))
                    Y1 = cX + (polupre * np.sin(uglic / (180 / np.pi)))

                    lista1.append(img[int(X1), int(Y1)][0])

                for li in range(len(lista1)-1):
                    if (lista1[li] == 0 and lista1[li+1] == 0):
                        lista1 = []
                        break
                    elif li == len(lista1)-1:
                        iskoci = True
                        break


            polupre = polupre-1




            dzins = []
            broj_celih = 0
            iter = 0
            pomocni_br = 0
            while iter < 360:
                for brojac in range(mali_p+1, polupre-1):
                    X1 = cY + (brojac * np.cos(iter / (180 / np.pi)))
                    Y1 = cX + (brojac * np.sin(iter / (180 / np.pi)))
                    dzins.append(img[int(X1), int(Y1)][0])

                for element in range(0, len(dzins)-1):
                    if (dzins[element] == 0 and dzins[element + 1] == 0):
                        iter = iter + 3
                        break

                    elif element == len(dzins) - 2:
                        broj_celih = broj_celih + 1
                        iter = iter + 10

                iter = iter + 3
                dzins = []

            print cX, cY, broj_celih, "0",maks_brojac_ugla+1,"1 23"

            break
        break


#C:/Users/Danijel/Desktop/tocak/set/example_3