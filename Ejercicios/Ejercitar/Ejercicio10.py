# ejericio10

Agenda_Telefono = {
    "Nombre:": "Pepe",
    "Direccion:": "Libertad 321",
    "Ciudad": "Chubaca",
    "Numero Telefonico": "123456789",
}

Agenda_Telefono["Redes Sociales"] = ["PepeTWI", "PepeIG", "PepeFACE"]

print("Agenda completa:")
for clave, valor in Agenda_Telefono.items():
    print(clave + ":", valor)

print()

print("Perfil de Instagram:", Agenda_Telefono["Redes Sociales"][1])
