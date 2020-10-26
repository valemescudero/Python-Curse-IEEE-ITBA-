#  Read file Tabla1.xlsx which contains some soccer championship scores and determine the first and last position based on them.


url = "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_3_datos/Tabla1.xlsx"
import wget as w
w.wget(url)


import pandas as pd
file = pd.read_excel("Tabla1.xlsx")
data = archivo.to_dict("records")

highest_score = data[0]["Puntos"]
lowest_score = data[0]["Puntos"]

highest_score_team = data[0]["Equipo"]
lowest_score_team = data[0]["Equipo"]

for i in range(1,len(data)):
    if data[i]["Puntos"] > highest_score:
        highest_score = data[i]["Puntos"]
        hest_score_team = data[i]["Equipo"]
    if data[i]["Puntos"] < lowest_score:
        lowest_score = data[i]["Puntos"]
        lowest_score_team = data[i]["Equipo"]

print("The team in the first place was", highest_score_team, "with", highest_score, "points.")
print("The team in the last place was", lowest_score_team, "with", lowest_score, "points.")
