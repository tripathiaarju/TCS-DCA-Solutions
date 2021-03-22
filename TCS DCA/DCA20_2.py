n = int(input())
lis = []
for i in range(n):
    x = int(input())
    lis.append(x)
k = int(input())
lis.sort(reverse=True)
print(lis[k - 1])
