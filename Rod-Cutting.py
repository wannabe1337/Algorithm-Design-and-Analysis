l=int(input('Total length of rod : '))
p=[0]
for i in range(l):
	p.append(int(input("Price of rod of length "+str(i+1)+" : ")))


r=[[0 for i in range(l+1)] for j in range(l+1)]

"""
#Comments#

Base Case :
	r[i][j]=j*p[i]		for all i==1
	
And
	r[i][j]=r[i-1][j]	if(i>j)

Otherwise:
	r[i][j]=max(p[i]+r[i][j-i],r[i-1][j])

#Running Time#
The running time of algorithm is Theta(n^2), due to its doubly-nested loop structure.

Refer this link : https://www.radford.edu/~nokie/classes/360/dp-rod-cutting.html

#Comments#
"""

#Main Algorithms Program
for j in range(1,l+1):
	r[1][j]=j*p[1]

for i in range(2,l+1):
	for j in range(1,l+1):	
		if(i>j):
			r[i][j]=r[i-1][j]
		else:
			r[i][j]=max(p[i]+r[i][j-i],r[i-1][j])

print('\nR = ',*r,sep='\n')

piece=[]
j=l
for i in range(l,1,-1):
	if(r[i][j]!=r[i-1][j]):
		piece.append(i)
		j-=i
print("\nPieces For Optimal Revenue = ",piece)