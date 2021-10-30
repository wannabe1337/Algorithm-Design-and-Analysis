# Starting Point = (0,0)
# Destination Point = (Row-1, Cols-1)

r,c = [int(x) for x in input('Enter number of rows and columns : ').split()]
print('rows = ',r," and cols = ",c)

Sol = []		# Sol will keep track of open path during journey
for i in range(r):
	temp = []
	for j in range(c):
		temp.append(0)
	Sol.append(temp)
print("Sol = ",*Sol, sep = "\n")

#################### Creating Maze ####################
Maze = []
for i in range(r):
	temp = []
	for j in range(c):
		temp.append(int(input('Enter value at ({0},{1}) : '.format(i,j))))
	Maze.append(temp)
print("Maze = ",*Maze,sep = "\n")
print()


# right = y+1
# down = x+1
# left = y-1
# up = x-1
#################### Algorithm to find path in Maze ####################

All_Path=[]			# Remembers path at the end of each journey
path=[]				# Remembers steps taken during journey (Right, Left, Up, or Down)
R_pointer,C_pointer = 0,0		#Initializing Current Pointer at starting point

def find_path(Maze,Sol,x,y):
	global r,c
	if(x == r-1 and y == c-1):
		Sol[x][y] = 1
		path.append('{0}{1}'.format(x,y))	# appending current position to the list path
		print("Sol = ",*Sol, sep="\n")
		print("path = ",path,"\n")
		All_Path.append(path[:])
		
		del path[-1]			# Deleting Last position added, so it can be used later 
		return
	if(x>=r or y>=c or x<0 or y<0 or Maze[x][y]==0 or Sol[x][y]==1):
		return

	Sol[x][y] = 1
	path.append('{0}{1}'.format(x,y))
	find_path(Maze,Sol,x,y+1)
	find_path(Maze,Sol,x+1,y)
	find_path(Maze,Sol,x,y-1)
	find_path(Maze,Sol,x-1,y)
	Sol[x][y] = 0				# Making current position 0 in Sol matrix so it can be used later
	del path[-1]				# Deleting Last position added, so it can be used later

find_path(Maze,Sol,R_pointer,C_pointer)		# Calling find_path()
print("All_Path = ", *All_Path, sep="\n")	# Printing All Available Path
print()

#################### Finding Shortest Path to reach to the destination ####################

min=len(All_Path[0])
short=0
for i in range(len(All_Path)):
	next=len(All_Path[i])
	if(next < min):
		min=next
		short=i
	
print('Total Number Of Path Available = ',len(All_Path),"\n")	#Total Number Of Path Found
print("Shortest Path = ",All_Path[short])			# Shortest Path








