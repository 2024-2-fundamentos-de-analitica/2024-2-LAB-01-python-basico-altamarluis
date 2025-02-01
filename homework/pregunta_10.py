"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    letter_column_data = []

    for line in lines:
        columns = line.strip().split("\t")
        letter = columns[0]
        col_4_len = len(columns[3].split(","))
        col_5_len = len(columns[4].split(","))
        letter_column_data.append((letter, col_4_len, col_5_len))

    return letter_column_data
