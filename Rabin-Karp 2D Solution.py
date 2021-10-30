###################Matrix and Pattern#######
m=10
txt=[
     ['A','W','Q','T','R','U','I','J','N','B'],
     ['T','R','U','E','Y','G','T','R','D','E'],
     ['S','E','L','F','J','U','K','L','I','F'],
     ['G','O','O','D','F','G','H','J','K','L'],
     ['S','O','U','L',' ','T','R','U','E','R'],
     ['H','Y','T','R','E','S','E','L','F','W'],
     ['K','J','H','Y','T','G','O','O','D','S'],
     ['R','V','H','J','R','S','O','U','L','F'],
     ['R','E','D','C','N','K','L','I','O','P'],
     ['E','V','A','Q','Z','X','L','P','U','Y']
    ]
n=4
pat=[
     ['T','R','U','E'],
     ['S','E','L','F'],
     ['G','O','O','D'],
     ['S','O','U','L']
    ]

print('Text = ',*txt,sep='\n')
print()
print('Pattern =',*pat,sep='\n')
print()

#[row][col])
##################### checkEquality #############################
def checkEquality(arr,row,col):
	y=0
	for j in range(col,col+n):
		x=0
		for i in range(row,row+n):
			if(pat[x][y]!=arr[i][j]):
				return False
			x+=1
		y+=1
	return True

###################### hash ##############################
def hash(arr):
	return int( ''.join(map(str, arr)))%11 

###################### findHash ##############################
def findHash(arr,row,col):
	patHash=[]
	for i in range(col,col+n):
		val=0
		for j in range(row,row+n):
			val+=ord(arr[j][i])
		patHash.append(val%11)
	return patHash

array=findHash(pat,0,0)
hashPat=hash(array)
print('Hash Value(Pat)=',hashPat)

#################### Main Algo ##############################
for i in range(m-n+1):
	for j in range(m-n+1):
		textval=findHash(txt,i,j)
		hashTxt=hash(textval)
		if(hashPat==hashTxt):
			if(checkEquality(txt,i,j)):
				print('Found at [row][col] = ['+str(i)+']['+str(j)+']')

		