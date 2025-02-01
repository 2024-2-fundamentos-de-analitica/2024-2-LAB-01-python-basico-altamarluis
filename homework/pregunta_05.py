"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    letter_min_max = {}

    for line in lines:
        letter, number = line.split(",")[0].split("\t")[:2]
        number = int(number)

        if letter in letter_min_max:
            letter_min_max[letter][0] = max(letter_min_max[letter][0], number)
            letter_min_max[letter][1] = min(letter_min_max[letter][1], number)
        else:
            letter_min_max[letter] = [number, number]

    return sorted((letter, values[0], values[1]) for letter, values in letter_min_max.items())