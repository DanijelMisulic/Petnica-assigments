import os
import numpy as np

if __name__ == "__main__":
    a_dir = raw_input()
    za_split = os.path.basename(a_dir)

    for subdir, dirs, files in os.walk(a_dir):
        for file in files:
            putanja = os.path.join(subdir, file)
            with open(putanja, 'r') as f:
                fajl = f.read()
                red = fajl.split('\n')
                red = red[:-1]
                brojac = 0

                for r in red:
                    koordinate = r.split(' ')
                    pocetak = koordinate[0:2]
                    prva_tacka = koordinate[2:4]
                    druga_tacka = koordinate[4:6]
                    treca_tacka = koordinate[6:8]

                    if float(pocetak[0])-float(prva_tacka[0]) == 0:
                        a = 0
                        b = 1
                        c = -float(pocetak[1])
                    else:
                        b = 1
                        a = -((float(prva_tacka[1])-float(pocetak[1]))/(float(prva_tacka[0])-float(pocetak[0])))
                        c = -(a*float(pocetak[0]) + float(pocetak[1]))

                    if float(pocetak[0])-float(druga_tacka[0]) == 0:
                        a1 = 0
                        b1 = 1
                        c1 = -float(pocetak[1])
                    else:
                        b1 = 1
                        a1 = -((float(druga_tacka[1])-float(pocetak[1]))/(float(druga_tacka[0])-float(pocetak[0])))
                        c1 = -(a1*float(pocetak[0]) + float(pocetak[1]))

                    x0 = float(treca_tacka[0])
                    y0 = float(treca_tacka[1])

                    dy = np.abs(a*x0 + b*y0 + c)/np.sqrt(a*a+b*b)
                    dx = np.abs(a1*x0 + b1*y0 + c1)/np.sqrt(a1*a1+b1*b1)

                    presek_x = (b*(b*x0-a*y0)-a*c)/(a*a+b*b)
                    presek_y = (a*(-b*x0+a*y0)-b*c)/(a*a+b*b)

                    presek_x1 = (b1*(b1*x0-a1*y0)-a1*c1)/(a1*a1+b1*b1)
                    presek_y1= (a1*(-b1*x0+a1*y0)-b1*c1)/(a1*a1+b1*b1)

                    kriticna_oblastX = np.sqrt((presek_x-float(prva_tacka[0]))*(presek_x-float(prva_tacka[0])) + (presek_y-float(prva_tacka[1]))*(presek_y-float(prva_tacka[1])))
                    rastojanje_prve_i_drugeX = np.sqrt((float(pocetak[0])-float(prva_tacka[0]))*(float(pocetak[0])-float(prva_tacka[0])) + (float(pocetak[1])-float(prva_tacka[1]))*(float(pocetak[1])-float(prva_tacka[1])))

                    if kriticna_oblastX>=rastojanje_prve_i_drugeX:
                        dx = dx*(-1)

                    kriticna_oblastY = np.sqrt((presek_x1 - float(druga_tacka[0])) * (presek_x1 - float(druga_tacka[0])) + (presek_y1 - float(druga_tacka[1])) * (presek_y1 - float(druga_tacka[1])))
                    rastojanje_prve_i_drugeY = np.sqrt((float(pocetak[0]) - float(druga_tacka[0])) * (float(pocetak[0]) - float(druga_tacka[0])) + (float(pocetak[1]) - float(druga_tacka[1])) * (float(pocetak[1]) - float(druga_tacka[1])))



                    if kriticna_oblastY >= rastojanje_prve_i_drugeY:
                        dy = dy*(-1)

                    nova_putanja = putanja.split(za_split)
                    nova_putanja[1] = nova_putanja[1][1:]
                    print nova_putanja[1], brojac, round(dx,5), round(dy,5)
                    brojac = brojac + 1

#C:/Users/Danijel/Desktop/set