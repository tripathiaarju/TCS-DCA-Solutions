s = input()
a = "53"
b = "8"
res = ""
if s.isalnum():
	if a in s:
		s = s.replace(a, "")

	if b in s:
		s =s.replace(b, "")
	print(s.lower())
else:
	print("Invalid input given, please remove the characters that are non digits and alphabets")
