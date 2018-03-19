import sys
l=0
ll=[]
for x in range(1, len(sys.argv)):
	if len(sys.argv[x])>=3:
		ll.append(sys.argv[x])
		l+=1
print(l)
for x in ll[::-1]:
	print(x, end=" ")
