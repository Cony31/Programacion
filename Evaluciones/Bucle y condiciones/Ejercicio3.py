#Definir los pagos 
diurna = 12000*10
nocturna = 16000*10
domingo_diurno = (12000+2000)*10
domingo_nocturno = (16000+3000)*10

#Ordenar los turnos de los empleados en un diccionario
turnos = {
    "turno1" : 
    {"Nombre":"Empleado1",
    "Lunes":"Nocturno",
    "Martes":"Nocturno",
    "Miércoles": "Nocturno",
    "Jueves":"Diurno",
    "Viernes":"Diurno"},
    
    "turno2" : 
    {"Nombre":"Empleado2",
    "Martes":"Nocturno",
    "Miércoles":"Nocturno",
    "Jueves":"Nocturno",
    "Domingo":"Diurno"},
    
    "turno3":
    {"Nombre":"Empleado3",
    "Miércoles":"Diurno",
    "Jueves":"Diurno",
    "Viernes":"Diurno",
    "Sabado":"Nocturno",
    "Domingo":"Nocturno"}
}
#Definir los pagos semanales
semana1 = nocturna+nocturna+nocturna+diurna+diurna
semana2 = nocturna+nocturna+nocturna+domingo_diurno
semana3 = diurna+diurna+diurna+nocturna+domingo_nocturno

#Ordenar toda la informacion en un diccionario
tarifa = {
    1:
    {"Nombre": turnos["turno1"]["Nombre"],
     "Sueldo Diario Diurno":diurna,
     "Sueldo Diario Nocturno": nocturna,
     "Sueldo Semanal":semana1},
    
    2:
    {"Nombre":turnos["turno2"]["Nombre"],
     "Sueldo Diario Diurno":diurna,
     "Sueldo Diario Nocturno":nocturna,
     "Sueldo Diario Diurno Domingo":domingo_diurno,
     "Sueldo Semanal":semana2},
    
    3:
    {"Nombre":turnos["turno3"]["Nombre"],
     "Sueldo Diario Diurno":diurna,
     "Sueldo Diario Nocturno":nocturna,
     "Sueldo Diario Nocturno Domingo":domingo_nocturno,
     "Sueldo Semanal":semana3}
}
#Imprimir el diccionario de forma estructurada con "for"
for clave, valor in tarifa.items():
    print(clave, ":", valor)