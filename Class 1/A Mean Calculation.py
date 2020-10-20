def test():
  for i in range(3):
    grades = [0,0,0]
    get_grades(grades)
    
    average = average_grade(grades)
    print("The average score is: ", round(average, 2))
    if average > 3:
      print("Passing grade\n")
    else:
      print("Failing grade\n")
    
    f_grade = final_grade(grades)
    print("The final grade is: ", round(f_grade, 2))
    if f_grade > 3:
      print("Passing grade\n")
    else:
      print("Failing grade\n")

def average_grade(grades):
  average = 0
  for i in range(len(grades)):
    average += grades[i]
  
  average = average / len(grades)
  return average

def final_grade(grades):
  f_grade = grades[0] / 5 + grades[1] / 2 + (grades[2] / 10) * 3
  return f_grade

def generate_grade():
  import random
  grade = int(random.random() * 10) + 1
  return grade

def get_grades(grades):
  for i in range(len(grades)):
    grades[i] = generate_grade()
  print("------------------oO0Oo------------------\n")
  print("Generated scores are:\n", grades, "\n")

test()
