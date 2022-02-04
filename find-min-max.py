print("Welcome this is my homework")
value = []
def recive_value(number):
  for number_of_value in range(number):
    value.append(int(input("value is :")))

number_input = int(input("Type Number of value: "))
recive_value(number_input)
print(value)

def findmin_num():
  min = 99999
  result_min = 0
  min2 = 99999
  for x in value:
    if x < min:
      min = x
      result_min = x
  for x in value:
    if min < x < min2 :
      min2 = x
      result_min2 = x
  print("min value is:", result_min) 
  print("min valueNo2 is :", result_min2)
def findmax_num():
  max = 0
  second_max = 0
  result_max = 99999
  for x in value:
    if x > max: 
      max = x
      result_max = x
      #print(x)
  for x in value:
    if max > x > second_max:
     second_max = x
     #print(x)
  print("max value is :", result_max)
  print("max value No.2 is :" , second_max)

findmin_num() 
findmax_num()