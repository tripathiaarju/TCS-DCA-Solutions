a = input()
a = a[0]
if a.isdigit():
    print("Number")
elif a.islower():
    print("lower alphabet")
elif a.isupper():
    print("UPPER ALPHABET")
else:
    print("Symbol")