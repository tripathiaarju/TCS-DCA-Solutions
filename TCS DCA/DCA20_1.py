n = int(input())
qu = n**4
temp = qu
s= ""
for i in range(len(str(n))):
    x= temp%10
    temp = int(temp/10)
    s+=str(x)
rev = s[::-1]
if int(rev) == n:
    print("TRUE")
elif n>0:
    print("Wrong Input")
else:
    print("FALSE")
