c = a.copy()
for i, x in enumerate(a):
	if x in b:
	c.pop(i)
print(c)
