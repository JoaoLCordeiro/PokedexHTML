#!/usr/bin/env python3

import csv

CABECALHOHTML = "<!DOCTYPE html>\n\
<html>\n\
<style>\n\
table, th, td {\n\
  border:1px solid black;\n\
}\n\
</style>\n\
<body>\n\
\n\
<h2>Pokedex</h2>\n"

CABECALHOTABELA = " <tr>\n\
    <th>Numero</th>\n\
    <th>Pokemon</th>\n\
    <th>Carta</th>\n\
    </tr>\n"

if __name__ == '__main__':
    # começa a main do programa

    listapoke = open("listapoke.csv", "r")
    htmldex = open("hrmldex.html", "w")

    # abre o arquivo com csv
    csvpoke = csv.reader(listapoke)

    # ignora o cabeçalho
    cabecalho = next(csvpoke)

    htmldex.write(CABECALHOHTML)

    htmldex.write("<table style=\"width:100%\">\n")
    htmldex.write(CABECALHOTABELA)
    for i in range(151):
        linha = next(csvpoke)
        htmldex.write(" <tr>\n")
        htmldex.write("     <td>" + linha[0] + "</td>\n")
        htmldex.write("     <td>" + linha[1] + "</td>\n")
        htmldex.write("     <td>" + "None" + "</td>\n")
        htmldex.write(" </tr>\n")

    htmldex.write("</table>")
    htmldex.write("</body>\n\
</html>\n")

    htmldex.close()
    listapoke.close()