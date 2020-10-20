#  Calculating a student's grade is a daily task for a professor. It is usually done by hand or Excel. This time we are doint it with Python.

#  Write a function that calculates the average of three grades and returns that value.
#  Create a second similar function that returns a grade giving the first test score a 20% of importance, 50% to the second and 30% to the third.
#  Call each function three times with different grades and verify, through an if instruction,
#  whether the student has passed or failed the subject in each case having 4 as the lowst passing grade.


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
