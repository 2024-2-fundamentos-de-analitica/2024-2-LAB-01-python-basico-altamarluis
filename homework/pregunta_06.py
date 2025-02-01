"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    key_min_max = {}

    for line in lines:
        key_value_pairs = line.strip().split("\t")[-1].split(",")

        for pair in key_value_pairs:
            key, value = pair.split(":")
            value = int(value)

            if key in key_min_max:
                key_min_max[key][0] = max(key_min_max[key][0], value)
                key_min_max[key][1] = min(key_min_max[key][1], value)
            else:
                key_min_max[key] = [value, value]

    return sorted((key, values[1], values[0]) for key, values in key_min_max.items())
