import csv
import pandas as pd

# with open() abre el archivo

with open('Book1.csv') as csv_file:
    # delimiter marca por que estan separados los datos (ex:comas)
    # quotechar marca entre que caracteres ignorar (ex:comillas dobles)
    # csv.reader lee las columnas por número, para leer por conmbre usar csv.DictReader
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    # line_count: variable de control de lineas
    line_count = 0
    for row in csv_reader:
        # line 0 marca la primera columna de nombre
        if line_count == 0:
            # union con coma de los datos
            print(f'    {", ".join(row)}')
            line_count += 1
        else:
            # print de las columnas seleccionadas
            # print(f'\t{row[0]} {row[1]} {row[2]} {row[3]} ')
            print(f'\t{", ".join(row)} ')
            line_count += 1
    # numero de lineas procesadas
    print(f'Processed {line_count} lines')
