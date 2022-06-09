a=input("enter the string")
b=input("enter the string")
x=len(a)
y=len(b)
x1=sorted(a)
x2=sorted(b)
if x==y:
	if x1==x2:
		print("b is anagram of a")
	else:
		print("b is not anagram of a")
else:
	print("plz enter same length string")
