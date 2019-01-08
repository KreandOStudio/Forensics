#! /usr/bin/env python
# -*- coding: utf-8 -*-

import  string

adn_asesino = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
selecciones = ["genero", "raza", "pelo", "ojos", "cara"]
color_pelo = ["negro", "marron", "rubi@"]
color_ojos = ["azules", "verdes", "marrones"]
tipo_rostro = ["cuadrad@", "redond@", "oval"]
tipo_genero = ["mujer", "hombre"]
tipo_raza = ["negr@", "asiatic@", "blanc@"]

pelo = {
    color_pelo[0]: "CCAGCAATCGC",   # negro
    color_pelo[1]: "GCCAGTGCCG",    # marron
    color_pelo[2]: "TTAGCTATCGC",   # rubi@
}
ojos = {
    color_ojos[0]: "TTGTGGTGGC",    # azules
    color_ojos[1]: "GGGAGGTGGC",    # verdes
    color_ojos[2]: "AAGTAGTGAC",    # marrones
}
rostro = {
    tipo_rostro[0]: "GCCACGG",      # cuadrad@
    tipo_rostro[1]: "ACCACAA",      # redond@
    tipo_rostro[2]: "AGGCCTCA",     # oval
}
genero = {
    tipo_genero[0]: "TGAAGGACCTTC", # mujer
    tipo_genero[1]: "TGCAGGAACTTC", # hombre
}
raza = {
    tipo_raza[0]: "CGACTACAG",      # negr@
    tipo_raza[1]: "CGCGGGCCG",      # asiatic@
    tipo_raza[2]: "AAAACCTCA",      # blanc@
}

nombres = ["Eva", "Larisa", "Matej", "Miha"]
personajes = {}

eva = {
    selecciones[0]: tipo_genero[0],     # genero:  mujer
    selecciones[1]: tipo_raza[2],       # raza: blanc@
    selecciones[2]: color_pelo[2],      # pelo: rubi@
    selecciones[3]: color_ojos[0],      # ojos: azules
    selecciones[4]: tipo_rostro[2],     # rostro: oval
}
Eva = {
    # Género femenino
    # Raza: blanco
    # Color de cabello: Rubio
    # Color de ojos: azul
    # Forma de la cara: Oval
    selecciones[0]: genero[tipo_genero[0]], # genero: mujer
    selecciones[1]: raza[tipo_raza[2]],     # raza: blanc@
    selecciones[2]: pelo[color_pelo[2]],    # pelo: rubi@
    selecciones[3]: ojos[color_ojos[0]],    # ojos: azules
    selecciones[4]: rostro[tipo_rostro[2]], # rostro: oval
}

Larisa = {
    # Género femenino
    # Raza: blanco
    # Color de cabello: marron
    # Color de ojos: Marrón
    # Forma de la cara: Oval
    selecciones[0]: genero[tipo_genero[0]], # genero: mujer
    selecciones[1]: raza[tipo_raza[2]],     # raza: blanc@
    selecciones[2]: pelo[color_pelo[1]],    # pelo: marrón
    selecciones[3]: ojos[color_ojos[2]],    # ojos: marrónes
    selecciones[4]: rostro[tipo_rostro[2]], # rostro: oval
}

Matej = {
    # Género masculino
    # Raza: blanco
    # Color de pelo: negro
    # Color de ojos: azul
    # Forma de la cara: Oval
    selecciones[0]: genero[tipo_genero[1]], # genero: hombre
    selecciones[1]: raza[tipo_raza[2]],     # raza: blanc@
    selecciones[2]: pelo[color_pelo[0]],    # pelo: negro
    selecciones[3]: ojos[color_ojos[0]],    # ojos: azules
    selecciones[4]: rostro[tipo_rostro[2]], # rostro: oval
}

Miha = {
    # Género masculino
    # Raza: blanco
    # Color de cabello: marron
    # Color de ojos: verde
    # Forma de la cara: cuadrado
    selecciones[0]: genero[tipo_genero[1]], # genero: hombre
    selecciones[1]: raza[tipo_raza[2]],     # raza: blanc@
    selecciones[2]: pelo[color_pelo[1]],    # pelo: marrón
    selecciones[3]: ojos[color_ojos[1]],    # ojos: verdes
    selecciones[4]: rostro[tipo_rostro[0]], # rostro: cuadrado
}


def devuelve_chungo(nom):
    if nom == "Miha":
        return Miha
    elif nom == "Larisa":
        return Larisa
    elif nom == "Matej":
        return Matej
    elif nom == "Eva":
        return Eva
    else:
        print "Te equivocaste"
        return False


def devuelve_selecciones(select, indice):
    if select == "genero":
        if indice==0:
            return genero
        elif indice==1:
            return tipo_genero
    elif select == "raza":
        if indice==0:
            return raza
        elif indice==1:
            return tipo_raza
    elif select == "pelo":
        if indice==0:
            return pelo
        elif indice==1:
            return color_pelo
    elif select == "ojos":
        if indice==0:
            return ojos
        elif indice==1:
            return color_ojos
    elif select == "cara":
        if indice==0:
            return rostro
        elif indice==1:
            return tipo_rostro
    else:
        print "Fallaste!"
        return False


def obtengo_datos_del_asesino(adn):
    asesino = {}
    print "Obtengo Datos del ADN del Asesino.\n"
    print ".-Obtengo de qué género es: {}".format(busca_genero(adn))
    print ".-Obtengo el tipo de raza: es {}".format(busca_raza(adn))
    print ".-Obtengo el tipo de rostro: es {}".format(busca_tipo_rostro(adn))
    print ".-Obtengo el color de los ojos: son {}".format(busca_color_ojos(adn))
    print ".-Obtengo el color del pelo y es de color: {}".format(busca_color_pelo(adn))
    for i in range(0, len(selecciones)):
        asesino.setdefault(
            selecciones[i],
            mega_obtencion_datos(
                adn,
                devuelve_selecciones(selecciones[i], 0),
                devuelve_selecciones(selecciones[i], 1)))
    print "Adivinado: {}".format(asesino)
    return asesino


def mega_obtencion_datos(adn, tipo, tipo_datos):
    retorno_datos = None
    no_encontrado = True
    x = 0
    while no_encontrado:
        if x < len(tipo_datos):
            busca = string.find(adn, tipo[tipo_datos[x]])
            if not busca == -1:
                retorno_datos = tipo_datos[x]
                no_encontrado = False
            else:
                x += 1
        else:
            return False
    return retorno_datos


def busca_color_pelo(adn):
    retorno_pelo = None
    no_encontrado = True
    x = 0
    while no_encontrado:
        if x < len(color_pelo):
            busca = string.find(adn, pelo[color_pelo[x]])
            if not busca == -1:
                retorno_pelo = color_pelo[x]
                no_encontrado = False
            else:
                x += 1
        else:
            return False
    return retorno_pelo


def busca_color_ojos(adn):
    retorno_ojos = None
    no_encontrado = True
    x = 0
    while no_encontrado:
        if x < len(color_ojos):
            busca = string.find(adn, ojos[color_ojos[x]])
            if not busca == -1:
                retorno_ojos = color_ojos[x]
                no_encontrado = False
            else:
                x += 1
        else:
            return False
    return retorno_ojos


def busca_tipo_rostro(adn):
    retorno_rostro = None
    no_encontrado = True
    x = 0
    while no_encontrado:
        if x < len(tipo_rostro):
            busca = string.find(adn, rostro[tipo_rostro[x]])
            if not busca == -1:
                retorno_rostro = tipo_rostro[x]
                no_encontrado = False
            else:
                x += 1
        else:
            return False
    return retorno_rostro


def busca_genero(adn):
    retorno_genero = None
    no_encontrado = True
    x = 0
    while no_encontrado:
        if x < len(tipo_genero):
            busca = string.find(adn, genero[tipo_genero[x]])
            if not busca == -1:
                retorno_genero = tipo_genero[x]
                no_encontrado = False
            else:
                x += 1
        else:
            return False
    return retorno_genero


def busca_raza(adn):
    retorno_raza = None
    no_encontrado = True
    x = 0
    while no_encontrado:
        if x < len(tipo_raza):
            busca = string.find(adn, raza[tipo_raza[x]])
            if not busca == -1:
                retorno_raza = tipo_raza[x]
                no_encontrado = False
            else:
                x += 1
        else:
            return False
    return retorno_raza


def main():
    loco = {}
    print "Código Principal Main."

    adivi = obtengo_datos_del_asesino(adn_asesino)

    for i in range(0, len(nombres)):
        print "{}.-{}: {}".format(i, nombres[i], devuelve_chungo(nombres[i]))
        personajes.setdefault(nombres[i], devuelve_chungo(nombres[i]))

    atontao = personajes.keys()[3]
    print atontao
    print "Eva modificado: {}".format(eva)
    print "RAZA:"
    for i in range(0, len(raza.keys())):
        print "{}.-{}".format(i, tipo_raza[i])
    for i in range(0, len(raza.keys())):
        print "{}.-Raza: {}".format(i, raza.keys()[i])
        print "{}.-Rostro: {}".format(i, rostro.keys()[i])
    print "Personajes: {}".format(personajes)

    no_lo_es = True
    #while no_lo_es:


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
