str1 = input()
a = str1[0]
b = str1[-1]
forward = str1[1::]+a
backward = b+str1[:len(str1)-1]
if forward == backward:
    print("1")
else:
    print("0")