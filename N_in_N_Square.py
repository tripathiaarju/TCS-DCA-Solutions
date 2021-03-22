num = int(input())
snum = num**4
s = ""
for i in range(len(str(num))):
    x = snum%10
    snum = int(snum/10)
    s+=str(x)
rev = s[::-1]
if int(rev) == num:
    print("TRUE")
elif num>0:
    print("Wrong Input")
else:
    print("Wrong Input")
"""
n = int(input())
n_sq = n*n
s = ""
for i in range(len(str(n))):
	temp = n_sq%10
	n_sq = int(n_sq/10)
	s+=str(temp)
s_res = s[::-1]
if n==int(s_res):
	print("Correct Number")
elif n>0:
	print("Incorrect Number")
else:
	print("Wrong Input")
"""
#3
def check(p):
    sq = p * p
    while (p > 0):
        if (p % 10 != sq % 10):
            return False
        p = int(p/10)
        sq = int(sq/10)
    return True
num = int(input())
if(num > 0):
    if(check(num)):
        print("Correct Number")
    else:
        print("Incorrect Number")
else:
    print("Wrong Input")