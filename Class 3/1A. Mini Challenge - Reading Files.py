#  Read Tabla1.xlsx file which contains some soccer championship scores.
#  This file has two columns, Team and Score. Calculate for each team the goal difference and print them


! wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_3_datos/Tabla1.xlsx"

import pandas as pd
file = pd.read_excel("Tabla1.xlsx")
data = archivo.to_dict("records")


for i in range(len(data)):
    difference = data[i]["Goles a favor"]-data[i]["Goles en contra"]
    sign = "in favor"
    if difference < 0:
        difference = difference * (-1)
        sign = "against"
    print(data[i]["Equipo"],"has a difference of", difference, "goals", sign)


