#!/usr/bin/env python3

import csv


def criaTabela(quant, palavraslinha):
    for i in range(quant):
        linha = next(csvpoke)
        if (linha[2] == "None"):
            listafalta.write(linha[1] + ", ")
            if (palavraslinha % 6 == 0):
                listafalta.write("\n")
            palavraslinha = palavraslinha + 1
    return palavraslinha


if __name__ == '__main__':
    # começa a main do programa

    listapoke = open("listapoke.csv", "r")
    listafalta = open("listafalta.csv", "w")

    # abre o arquivo com csv
    csvpoke = csv.reader(listapoke)

    # ignora o cabeçalho
    cabecalho = next(csvpoke)

    palavraslinha = 1

    palavraslinha = criaTabela(151, palavraslinha)
    palavraslinha = criaTabela(251-151, palavraslinha)
    palavraslinha = criaTabela(386-251, palavraslinha)
    palavraslinha = criaTabela(494-386, palavraslinha)
    palavraslinha = criaTabela(649-494, palavraslinha)
    palavraslinha = criaTabela(721-649, palavraslinha)
    palavraslinha = criaTabela(809-721, palavraslinha)
    palavraslinha = criaTabela(905-809, palavraslinha)
    palavraslinha = criaTabela(1010-905, palavraslinha)

    listafalta.close()
    listapoke.close()
