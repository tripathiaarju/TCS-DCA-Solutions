def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
inp = input()
s = [str(x) for x in inp]
vow = ['a','e','i','o','u']
v = []
fin = []
c = {}
d = {}
for i in range(len(s)-1):
    x = s.count(s[i])
    d = dict({s[i]:x})
    c.update(d)
for i in s:
    if i in vow:
        v.append(i)
for i in v:
    if i in s:
        s.remove(i)
count_vow = len(v)
count_con = len(s)+1
ways_vow = fact(count_vow)
ways_con = fact(count_con)
way =ways_con*ways_vow
div = 1
lis = []
for i in c.values():
    if i>0:
        a=fact(i)
        div*=a
print(int(way/div))