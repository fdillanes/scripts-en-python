#extrae los telefonos de unos archivos de barry
import os
import re

base = './AddressBookAll/'
directorio = os.listdir(base)
dest = open('dump2.txt','w')
for i in directorio: 
	lugar = base + str(i)
	fichero = open(lugar)
	for linea in fichero:
		nom = str(re.findall('[A-Za-z]+',linea))
		num = str(re.findall('[0-9]+',linea))
		todo =  nom + num + "\n"
		dest.write(todo)
dest.close()
