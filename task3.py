even_list = []
for i in range(100,500,2):
	even_list.append(i)
#print(even_list)
print(reduce(lambda x,y: x+y,even_list))
