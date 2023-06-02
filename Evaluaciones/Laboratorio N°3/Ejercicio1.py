# Ejercicio1

Senco = {
    "Id_Bio": 8,
    "NombreB": "BioBio",
    "Superficie_Bio": 23890,
    "Habitantes_Bio": 1556805,
    "Id_Lagos": 10,
    "NombreL": "Los Lagos",
    "Superficie_Lagos": 48583,
    "Habitantes_Lagos": 828708,
}

for clave, valor in Senco.items():
    print(clave + ":", valor)

print()

Superficie_Biobio = 23890
Superficie_Lagos = 48583

Habitantes_Biobio = 1556805
Habitantes_Lagos = 828708

Densidad_Biobio = Habitantes_Biobio / Superficie_Biobio
Densidad_Lagos = Habitantes_Lagos / Superficie_Lagos

Senco["Densidad Biobio"] = round(Densidad_Biobio, 1)
Senco["Densidad Los lagos"] = round(Densidad_Lagos, 1)

Senco["Capital Biobio"] = ["Concepcion"]
Senco["Capital Los lagos"] = ["Puerto Montt"]

Senco["Comunas Biobio"] = ["Lota, Lebu, Los Ángeles"]
Senco["Comunas Los lagos"] = ["Castro, Puerto Varas, Purranque"]

Senco["Provincia Biobio"] = ["Biobío, Arauco, Concepción"]
Senco["Provincia Los lagos"] = ["Osorno, Llanquihue, Chiloé, Palena"]

for clave, valor in Senco.items():
    print(clave + ":", valor)
