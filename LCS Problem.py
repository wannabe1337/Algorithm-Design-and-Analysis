m=int(input("Length of 1st seq. : "))
x=['0']
n=int(input("Length of 2nd seq. : "))
y=['0']

for i in range(m):
	x.append(input("Enter "+str(i+1)+" element in seq. X : " ))
for i in range(n):
	y.append(input("Enter "+str(i+1)+" element in seq. Y : " ))
print()
print("X = ",x[1:])
print()
print("Y = ",y[1:])
print()

c=[[0 for i in range(n+1)] for j in range(m+1)]


"""
#Comments#
if X.len=m and Y.len=n

for the base case we compute :
	c[i][j]=0			 if i=0 or j=0

And 	c[i][j]= c[i-1][j-1] + 1	 if i,j>0 and x[i]=y[j]

	c[i][j]=max(c[i][j-i],c[i-1][j]) if i,j>0 and x[i]!=y[j]

then
Cost to fill the table will be 
	Theta(m*n)
The running time of the procedure is Theta(mn), since each table entry takes Theta(1) time to compute.

#input
Length of 1st seq. : 7
Length of 2nd seq. : 6

X :
a
b
c
b
d
a
b

Y:
b
d
c
a
b
a
#Comments#
"""

# Filling the table Row-By-Row

for i in range(1,m+1):
	for j in range(1,n+1):
		if(x[i]==y[j]):
			c[i][j]=c[i-1][j-1] + 1
		else:
			c[i][j]= max(c[i][j-1],c[i-1][j])
print('C = ',*c,sep="\n")
print()
print("Length Of LCS = ",c[m][n])

#Printing the LCS
j=n
i=m
lcs=[0 for i in range(c[i][j])]
k=c[i][j]-1
while(i>0):
	if(c[i][j]!=c[i-1][j]): 
		if(x[i]==y[j]):
			lcs[k]=x[i]
			j-=1
			k-=1
		else:
			j-=1
			i+=1
	i-=1
			
	

print("LCS = ",lcs)
