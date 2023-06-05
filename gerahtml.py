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


def criaTabela(quant):
    htmldex.write("<table style=\"width:100%\">\n")
    htmldex.write(CABECALHOTABELA)
    for i in range(quant):
        linha = next(csvpoke)
        htmldex.write(" <tr>\n")
        htmldex.write("     <td>" + linha[0] + "</td>\n")
        htmldex.write("     <td>" + linha[1] + "</td>\n")
        if (linha[2] == "None"):
            htmldex.write("     <td>" + linha[2] + "</td>\n")
        else:
            htmldex.write("     <td>" + "<a href=\"" + linha[2]
                          + "\">carta</a>" + "</td>\n")
        htmldex.write(" </tr>\n")


if __name__ == '__main__':
    # começa a main do programa

    listapoke = open("listapoke.csv", "r")
    htmldex = open("hrmldex.html", "w")

    # abre o arquivo com csv
    csvpoke = csv.reader(listapoke)

    # ignora o cabeçalho
    cabecalho = next(csvpoke)

    htmldex.write(CABECALHOHTML)

    criaTabela(151)
    criaTabela(251-151)
    criaTabela(386-251)
    criaTabela(494-386)
    criaTabela(459-494)
    criaTabela(649-459)
    criaTabela(721-649)
    criaTabela(809-721)
    criaTabela(905-809)
    criaTabela(1010-905)

    htmldex.write("</table>")
    htmldex.write("</body>\n\
</html>\n")

    htmldex.close()
    listapoke.close()
