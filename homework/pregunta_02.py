"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    letter_count = {}

    for line in lines:
        letter = line.split(",")[0][0]
        letter_count[letter] = letter_count.get(letter, 0) + 1

    return sorted(letter_count.items())
