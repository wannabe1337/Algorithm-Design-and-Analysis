import string
from collections import Counter

attendance=open((input("Enter Attendance file name . . .")),'r')
text_string = attendance.read()
print('\nStudent\'s Attendance : ',text_string)

pattern=['apa','ppp','ppa','aaa','pap','aap','paa','app']

frequency={}
for p in pattern:
	frequency[p]=text_string.count(p)

frequency_list = frequency.keys()

print('\nPrinting all matched pattern . . .')
for words in frequency_list:
    print (words,':',frequency[words])

max_key = max(frequency, key=frequency.get)	# Pattern with highest match

k=Counter(frequency)
high=k.most_common(3)

print("\nPrinting Top 3 Pattern Found . . .")
for i in high:
	print(i[0],':',i[1])

print("\nPrinting Student Status . . .")
good=0
bad=0
if frequency[max_key]==10 and max_key=='ppp':
	print('Best Record')
elif frequency[max_key]==10 and max_key=='aaa':
	print('Worst Record')
elif frequency[max_key]==10 and max_key==('aap' or 'apa'):
	print('Regularly Irregular')
else:
	for j in high:
		if (j[0] or j[1] or j[2])==('aap' or 'apa' or 'paa'):
			bad+=1
		if (j[0] or j[1] or j[2])==('ppa' or 'pap' or 'app'):
			good+=1
	if good>bad:
		print('Regular')
	else:
		print('Irregular')









#import re

#match_pattern=re.findall(r'\b()\b', text_string)

#frequency[] = for x in text_string.count('apa','ppp','ppa','aaa','pap','aap','paa','app')

#for word in match_pattern:
#    count = frequency.get(word,0)
#    frequency[word] = count + 1




#arr=[]
#for i in range(30):
#	arr.append(input(f"Day {i+1} :"))
#print(arr)
#present=0
#absent=0
#for i in range(30):
	