# calcula la venta con tarjeta de credito y cuotas

#================================================
# imports
#================================================
import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox as mBox
# from tkinter import Menu
import math

#================================================
# crear ventana, agregar titulo
#================================================
win = tk.Tk()
win.title('Calculo de Venta con Tarjetas y Cuotas - Intec Informatica')

multipbase =  1.05 #ingresa el aumento para venta con tarjeta si le queres poner 10% de arranque
serieM = (1.0336, 1.0454, 1.0615, 1.0745, 1.0875, 1.1144, 1.1296, 1.1448,  1.1602, 1.1757, 1.1914, 1.22, 1.237, 1.2541, 1.2713, 1.2887, 1.3062, 1.3434, 1.3623,  1.3814, 1.4007, 1.4202, 1.4397)

def consultar():
	precio =  float(valProducto.get()) * multipbase
	for x in range(1, 13):
		etiq = 'L' + str(x)
		etiq = ttk.Label(cuotas, text=str(x)) #cantidad de cuotas
		etiq.grid(row = x, column = 0)
		rta = 'R' + str(x)
		total =  round(precio * serieM[x-1], 2)
		rta = ttk.Label(dolares1, text=str(total)) #valores totales en dolares
		rta.grid(row = x, column=1)
		ccuota = round(total / x, 2)
		rta2 = ttk.Label(dolares2, text=str(ccuota)) # valor de cada cuota
		rta2.grid(row = x, column=2)
		pestot = int(valDolar.get()) * total
		rtap1 = ttk.Label(pesos1, text=str(pestot)) # valor total en pesos
		rtap1.grid(row = x, column = 3)
		pescuot = int(valDolar.get()) * ccuota # valor de cada cuota en pesos
		rtap2 = ttk.Label(pesos2, text=str(pescuot))
		rtap2.grid(row = x, column = 4)
		
		

valDolar = tk.StringVar(value = '16') #ingresa el dolar actual
DolarL = ttk.Label(win, text='Valor del Dolar:')
DolarL.grid(row = 0, column = 0)
ingValDolar = ttk.Entry(win, width = 15, textvariable=valDolar)
ingValDolar.grid (row = 0, column = 1, )

valProducto = tk.StringVar() # ingresa el valor del producto en dolares
ProductoL = ttk.Label(win, text='Valor del Producto')
ProductoL.grid(row = 1, column = 0)
ingValProducto = ttk.Entry(win, width = 15, textvariable=valProducto)
ingValProducto.grid(row = 1, column = 1)

consulta = ttk.Button(win, text='consultar', command=consultar) # el boton que pone todo a andar
consulta.grid(row = 2, column = 0, sticky=tk.W)

# conjunto de salidas
cuotas = ttk.LabelFrame(win, text = 'cuotas')
cuotas.grid(row = 3, column = 0)
dolares1 = ttk.LabelFrame(win, text = 'valor total en dolares')
dolares1.grid(row = 3, column = 1)
dolares2 = ttk.LabelFrame(win, text = 'valor cuota en dolares')
dolares2.grid(row = 3, column = 2)
pesos1 = ttk.LabelFrame(win, text= 'valor total en pesos')
pesos1.grid(row = 3, column = 3)
pesos2 = ttk.LabelFrame(win, text='valor cada cuota en pesos')
pesos2.grid(row=3, column=4)

#================================================
# menu
#================================================



#================================================
# arrancando el programa
#================================================
win.mainloop()
