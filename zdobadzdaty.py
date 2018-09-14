""" Dodaje daty z pliku dni.txt do listy"""
import re


# daty = daty do dodania
daty = []
# Open file
with open("dni.txt", "r", encoding='utf-8') as dni:

    # read every line
    for linia in dni:
        data = re.findall(r'(\d\d?)\s(\S+)', linia)

        # if nothing found go to next line
        if len(data) == 0:
            continue

        daty.append(data[0])


print(daty)  # OLL KORREKT chek
