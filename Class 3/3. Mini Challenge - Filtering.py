import pandas as pd
students_file = pd.read_excel("Datos.xlsx")
data = students_file.to_dict("records")

math_passing_grades = students_file[students_file['Matematica'] >= 4]
math_data = math_passing_grades.to_dict("records")
print("Gradepoint average for those with Maths passing grades:")

def students_gradepoint_average(data, index):
  gradepoint_average = (data[index]["Quimica"] + data[index]["Matematica"] + data[index]["Fisica"]) / 3
  return gradepoint_average

for i in range(len(data2)):
  student = math_data[i]["Nombre"] + " " + math_data[i]["Apellido"]
  gradepoint_average = students_gradepoint_average(data2, i)
  print(student, "- {0:.2f}".format(gradepoint_average))
