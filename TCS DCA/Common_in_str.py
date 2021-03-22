"""
str1 = input()
str2 = input()
lis =[]
for i in str2:
    if i in str1:
        lis.append(i)
slis = sorted(lis)
print(("[{0}]".format(",".join(map(str, slis)))))
print("[{0}]".format(",".join(map (str,lis))))
"""
str1 = input()
str2 = input()
lis =[]
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            lis.append(str1[i])
print("Normal Order[{0}]".format(",".join(map(str,lis))))
print("Reverse Order[{0}]".format(",".join(map(str,sorted(lis)))))