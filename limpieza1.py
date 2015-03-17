
orig = open('dump2.txt','r')
dest = open('limpio.txt','w')
for line in orig:
	if line.startswith("['Predeterminado"):
		continue
	else:
		dest.write(line)

orig.close()
dest.close()
