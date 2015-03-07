# abre un mbox y extrae datos y los guarda como un archivo json

import re 



f = raw_input ("Enter a file name: ")
if len(f) < 1: f = "SAI.mbox"

try:
    open_file = open(f)
except:
    print 'File cannot be opened: ', f
    exit()

hand = open("dumpeo.txt", 'w')

cont = 0
for line in open_file:
	line = line.rstrip()
	a = str(re.findall('Actividad:.(.+)', line))
      	if len(a) > 3:
		cont += 1
		salida = str(cont) + "\n" + "Actividad: " + a + "\n" 
		hand.write(salida)
	
	b = str(re.findall('Com.*:.(.+)', line))
	if len(b) > 3 :
		salida = "Comision: " + b + "\n"
		hand.write(salida)

	c = str(re.findall('INAP:.(.+)', line))
	if len(c) > 3 : 
		salida = "Codigo INAP: " + c + "\n"
		hand.write(salida)

	d = str(re.findall('Agente:.(.+)', line))
	if len (d) > 3 :
		salida = "Agente: " + d + "\n" + "\n"
		hand.write(salida)

		

hand.close()

		
		

		
