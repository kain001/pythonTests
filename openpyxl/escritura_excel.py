from openpyxl import Workbook
from openpyxl.styles import Font
import time

book = Workbook()
sheet1 = book.active

sheet1['A1'] = 5
sheet1['A2'] = 10

sheet1['B1'] = 'rango'
sheet1['B1'].font = Font(color='FF0000', bold=True)
for i in range(2, 15):
    sheet1[f'B{i}'] = i**2

sheet2 = book.create_sheet('Hoja_2')
sheet2['A1'] = 'Hola Mundo'
time = time.strftime('%x')
sheet2['A2'] = time

book.save('prueba_escritura.xlsx')