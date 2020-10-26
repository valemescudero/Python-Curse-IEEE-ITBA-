#  Write a function to receive two parameters, a DataFrame type variable (students table) and the student's index number.
#  It should return the average gradepoint for the student's grades from all their subjects.


! wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_3_datos/Datos.xlsx"


import pandas as pd
file = pd.read_excel("Datos.xlsx")
data = file.to_dict("records")

def student_gradepoint_average(data, index):
    average = (data[index]["Quimica"] + data[index]["Matematica"] + data[index]["Fisica"]) / 3
    return average

for i in range(len(data)):
    student = data[i]["Nombre"] + " " + data[i]["Apellido"]
    average = student_gradepoint_average(data, i)
    print("The gradepoint average for", alumno, "is {0:.2f}".format(promedio))
