"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    key_count = {}

    for line in lines:
        key_value_pairs = line.strip().split("\t")[-1].split(",")

        for pair in key_value_pairs:
            key = pair.split(":")[0]

            if key in key_count:
                key_count[key] += 1
            else:
                key_count[key] = 1

    return key_count