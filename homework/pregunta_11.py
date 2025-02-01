"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    letter_sum_dict = {}

    for line in lines:
        columns = line.strip().split("\t")
        col_4_values = columns[3].split(",")
        col_2_value = int(columns[1])

        for value in col_4_values:
            letter = value.split(":")[0]

            if letter in letter_sum_dict:
                letter_sum_dict[letter] += col_2_value
            else:
                letter_sum_dict[letter] = col_2_value

    return dict(sorted(letter_sum_dict.items()))
