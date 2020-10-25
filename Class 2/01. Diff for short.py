#  Write a function to take a list of n numbers and return the discrete derivative with the differences between each number and its preceding when there is one.
#  The new list should thusly be one number shorter.


def derivative(list):
  new_list = []
  
  for i in range(1,len(list)):
    r = int(list[i]) - int(list[i-1])
    new_list.append(r)
  return new_list


list = input("Please, enter numbers separated by a comma")
list = list.split(',')
print(derivative(list))
