"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    file_path = "files/input/data.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()

    number_letter_map = {}

    for line in lines:
        letter, number = line.split(",")[0].split("\t")[:2]
        number = int(number)

        if number not in number_letter_map:
            number_letter_map[number] = set()
        
        number_letter_map[number].add(letter)

    return sorted((num, sorted(letters)) for num, letters in number_letter_map.items())