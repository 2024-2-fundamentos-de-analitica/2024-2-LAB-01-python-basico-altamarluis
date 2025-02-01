"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    total_sum = sum(int(line.split(",")[0].split("\t")[1]) for line in lines)

    return total_sum
