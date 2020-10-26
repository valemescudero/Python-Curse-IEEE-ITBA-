#  Determine the gradepoint average for the Chemistry class from its students' grades in the Datos.xlsx file


! wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_3_datos/Datos.xlsx"


import pandas as pd
file = pd.read_excel("Datos.xlsx")
data = file.to_dict("list")

gradepoint_average = sum(data["Quimica"]) / len(data["Quimica"])
print("The gradepoint average for the Chemistry class is {0:.2f}".format(gradepoint_average))
