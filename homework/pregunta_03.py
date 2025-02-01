"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    letter_sums = {}

    for line in lines:
        letter, number = line.split(",")[0].split("\t")[:2]
        letter_sums[letter] = letter_sums.get(letter, 0) + int(number)

    return sorted(letter_sums.items())

