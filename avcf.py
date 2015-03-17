import re

orig = open ('limpio.txt')
dest = open ('contactosmel.vcf','w')

beg = 'BEGIN:VCARD\nVERSION:3.0'
en = 'END:VCARD'

for line in orig:
	nombre = re.findall('[A-Z|a-z]+',line)
	numero = re.findall('[0-9]+',line)
	nomcompleto ='' 
	for i in nombre:
		if nomcompleto == '':
			nomcompleto = str(i)
		else:
			nomcompleto = nomcompleto + ', ' + str(i)
	if nomcompleto == '':
		continue
	else:
		dest.write(beg+'\n')
		dest.write('FN:' + nomcompleto+'\n')
		dest.write('N:' + nomcompleto + ';;;'+'\n')
		for x in numero:
			dest.write('TEL;TYPE=WORK:'+str(x)+'\n')
		dest.write(en+'\n')
	
	
