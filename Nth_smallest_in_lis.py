def bubble_sort(l):
	for i in range(len(l)-1):
		for j in range(i+1,len(l)):
			if l[i] > l[j]:
				temp = l[i]
				l[i] = l[j]
				l[j] = temp
	return l

def nth(li,k):
	return li[k-1]

size = int(input())
lis = []
for i in range(size):
	x = int(input())
	lis.append(x)
bubble_sort(lis)
key = int(input())
print(nth(lis,key))