import random
import math

print('f -> Farmers and s -> Soldiers')
input_num=int(input('Enter the number of input : '))
soldiers=math.ceil(input_num/2)
farmers=soldiers-1

list=[]
for i in range(soldiers):
	list.append('s')
for i in range(farmers):
	list.append('f')
random.shuffle(list)			# Shuffling List
print('Input : ',list)

j=0
cost=0
for i in range(soldiers+farmers):	# Sorting Arrangement
	cost+=1
	j=i
	check=0
	if i%2==0 and list[i]=='f':
		while(list[j]!='s'):
			j+=1
			cost+=1
		check=1	
	if i%2!=0 and list[i]=='s':
		while(list[j]!='f'):
			j+=1
			cost+=1
		check=1
	
	if check==1:
		temp=list[i]
		list[i]=list[j]
		list[j]=temp
		cost+=1
		

print('Output : ',list)
print('Total Cost : ',cost)
