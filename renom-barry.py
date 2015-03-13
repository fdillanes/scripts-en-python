# renombrar archivos en un directorio con numeros secuenciales
import os

n = 0
base = './'
directorio = os.listdir(base)
for i in directorio:
	n += 1
	dest = base + str(n)
	os.rename(base+i,dest)
	print type(i), base + i
	print type(dest), dest
