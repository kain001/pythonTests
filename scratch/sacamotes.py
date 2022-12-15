jhon = ["Paraguas", "El Sandalia", "Chancleta", "Barbas"]
name = input("Escribe el nombre de quien quieres los motes")


def saca_motes(search_name: str):
    if search_name == "jhon":
        for x in range(0, 4):
            print(jhon[x])


saca_motes(name)
