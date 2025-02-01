"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    month_count = {}
    for i in lines:
        c = i.split(",")[0].split("-")[1]
        if c in month_count:
            month_count[c] += 1
        else:
            month_count[c] = 1

    return sorted(month_count.items())
print(pregunta_04())