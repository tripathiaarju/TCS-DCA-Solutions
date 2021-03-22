num = int(input())
if num>0:
    lis = [str(x) for x in str(num)]
    mul = 1
    for i in lis:
        mul = mul*int(i)
    print(mul)
else:
    print("Number is not valid, please enter a positive number.")