my_list=[[1,2,3],3,4]
def nested_sum(any_list):
  total  = 0
  for i in any_list:
    if isinstance(i,int):
      total+=i
    else:
      total+=nested_sum(i)
  return total

print(nested_sum(my_list))
