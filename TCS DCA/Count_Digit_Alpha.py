num = int(input())
arr = []
n = 0
a = 0
mix = 0
for i in range(num):
    arr.append(input())
for i in arr:
    if i.isdigit():
        n+=1
    elif i.isalpha():
        a+=1
    elif i.isalnum():
        mix+=1
if mix>0:
    print("Invalid Input")
else:
    print("Digits =",n)
    print("Words =",a)