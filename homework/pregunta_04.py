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

    for line in lines:
        month = line.split(",")[2].split("-")[1]
        month_count[month] = month_count.get(month, 0) + 1

    return sorted(month_count.items())