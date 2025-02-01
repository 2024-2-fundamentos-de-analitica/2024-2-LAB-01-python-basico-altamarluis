"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    letter_value_sum_dict = {}

    for line in lines:
        columns = line.strip().split("\t")
        letter = columns[0]
        col_5_values = columns[4].split(",")
        col_5_sum = sum(int(value.split(":")[1]) for value in col_5_values)

        if letter in letter_value_sum_dict:
            letter_value_sum_dict[letter] += col_5_sum
        else:
            letter_value_sum_dict[letter] = col_5_sum

    return letter_value_sum_dict