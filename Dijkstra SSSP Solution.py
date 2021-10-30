n=int(input("Enter Number Of Nodes : "))

########################################(Input Graph)########################################
# Storing Graph using Adjacency List

G={}
print("Input vertex and their weight in [v:w] format \nEnter \'#\' to indicate ending of list for a vertex.")
for s in range(97,97+n):
	i=1
	nodelist=[]
	while(i!='#'):
		ve=(input("Enter "+str(i)+" Vertex and Weight(E) connected to "+chr(s)+" : ")).split(':')
		if(ve[0]!='#'):
			node=[ve[0],int(ve[1])]
			nodelist.append(node)
			i+=1
		else:
			i='#'
	G[chr(s)]=nodelist

print('Given Graph :',G)
########################################(SSSP)########################################
source=input("Enter Source Node : ")
dest=list(G.keys())

#initializtion
d={}
pi={}
def initialize():
	for v in dest:
		d[v]=1000
		pi[v]='nil'
	d[source]=0

#Relaxation
def relax(u,v,w):
	if(d[v]>d[u]+w):
		d[v]=d[u]+w
		pi[v]=u

#Extract-Min Q
def extract_min(queue,dist):
	u=queue[0]
	min=dist[u]
	for key in queue:
		if(dist[key]<min):
			min=dist[key]
			u=key
	return u

#Dijkstra Algo (SSSP)
initialize()
s=set()
Q=list(G.keys())
while(Q):
	
	u=extract_min(Q,d)
	Q.remove(u)
	s.add(u)
	for n in G[u]:
		v=n[0]
		w=n[1]
		relax(u,v,w)
print(f'Shortest-Path to all vertices from source {source} :',d)
print('Predecessor of each vertex in Shortest-Path :',pi)
