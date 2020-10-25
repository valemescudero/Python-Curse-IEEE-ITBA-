def derivative(list):
  new_list = []
  
  for i in range(1,len(list)):
    r = int(list[i]) - int(list[i-1])
    new_list.append(r)
  return new_list


list = input("Please, enter numbers separated by a comma")
list = list.split(',')
print(derivative(list))
