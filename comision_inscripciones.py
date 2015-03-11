# -*- coding: utf-8 -*-
# registra todos los archivos de inscripciones y arma un solo listado
# 

from xlrd import open_workbook,cellname

# primera etapa
# genera el nombre de los archivos a rastrear
def proximo_archivo(n):
	n += 1
	string = "comision_inscripcion_web ("+str(n)+").xls"
	return string

#imprimir = proximo_archivo(3)
#print imprimir
#print type(imprimir)

# segunda etapa
# 1.-abre un archivo xls
nombre = proximo_archivo(0)
book = open_workbook(nombre)
sheet = book.sheet_by_index(0)
#print sheet.name
#print sheet.nrows
#print sheet.ncols

# 2.- navega a través de sus datos transformandolos a unicode
for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        j = cellname(row_index, col_index)
        a = unicode(sheet.cell(row_index,col_index).value).encode("utf-8")
        if j[1] == '7':
            print  a 
