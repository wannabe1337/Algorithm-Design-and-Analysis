n=int(input("No. of nodes : "))
p=[0]
q=[]
for i in range(n):
	p.append(float(input("Success probability of node "+str(i+1)+" : " )))
for i in range(n+1):
	q.append(float(input("Failure probability of set "+str(i+1)+" : " )))

print(p)
print(q)
print()

w=[[0 for i in range(n+1)] for j in range(n+1)]
c=[[0 for i in range(n+1)] for j in range(n+1)]
r=[[0 for i in range(n+1)] for j in range(n+1)]

# Main Algorithm

for i in range(n+1):
	w[i][i]=q[i]
	for j in range(i+1,n+1):
		w[i][j]=w[i][j-1]+p[j]+q[j]


	c[i][i]=0
	if(i<n):
		c[i][i+1]=w[i][i+1]
		r[i][i+1]=i+1
for l in range(2,n+1):
	for i in range(n-l+1):
		j=i+l
		c[i][j]=9999999999	# infinite
		for k in range(i+1,j+1):
			min=c[i][k-1]+c[k][j]+w[i][j]
			if(min<c[i][j]):
				c[i][j]=min
				r[i][j]=k
	
print()
print('W= ',*w,sep="\n")
print()
print('C= ',*c,sep="\n")
print()
print('R= ',*r,sep="\n")
print()

print('Tree root positions : ')
def prnt(i,j):
	if((j-i)==1 or (j-i)==0):
		print('r[',i,',',j,'] = ', r[i][j])
		return
	else:
		prnt(i,r[i][j]-1)
		prnt(r[i][j],n)
		print('r[',i,',',j,'] = ', r[i][j])
	
prnt(0,n)


"""
#Comments#

		#Table# 

w00,c00,r00	w11,c11,r11	w22,c22,r22	

w01,c01,r01	w12,c12,r12

w02,c02,r02

		#Algorithm#
for the base case we compute :
	w[i][i]=q[i]	for all 1<=i<=n
and for all n>=j>=i
	w[i][j]=w[i][j-1]+p[j]+q[j]
and then 
We have to find value of C[i][j] and r[i][j] using formula
	c[i][j]=for all i<k<=j[min(c[i][k-1]+c[k][j])] + w[i][j]

	-> If we want to know the cost for larger difference in i and j
	   we should first know the cost for smaller differences in i and j.
	   Therefore, we will start with the i,j difference 0

	-> Apart from finding the cost, we should also know about who is giving the
	   minimum cost; the key which is giving minimum cost should be selected as root. i.e.(k Value)

		#Running Time
Algorithm computes the rows from bottom to top and from left to right within each row.
The OPTIMAL-BST procedure takes Theta(n^3) time, just like MATRIX-CHAINORDER. 

We can easily see that its running time is O(n^3), since its for loops are nested three deep and each loop index takes on atmost n values.
The loop indices in this Algo do not have exactly the same bounds as those in MATRIX CHAIN ORDER,but they are within atmost 1 in all directions.
Thus,like MATRIX-CHAINORDER, this Algo takes Omega(n^3) time.

#Comments#

#Input
No. of nodes : 4
No. of nodes : 4
Success probability of node 1 : 3
Success probability of node 2 : 3
Success probability of node 3 : 1
Success probability of node 4 : 1
Failure probability of set 1 : 2
Failure probability of set 2 : 3
Failure probability of set 3 : 1
Failure probability of set 4 : 1
Failure probability of set 5 : 1
p[i] = [0, 3.0, 3.0, 1.0, 1.0]
q[i] = [2.0, 3.0, 1.0, 1.0, 1.0]

#Comments#
"""