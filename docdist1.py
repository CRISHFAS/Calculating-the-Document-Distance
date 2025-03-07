#!/usr/bin/python3
# docdist1.py - versión inicial de distancia de documentos
#
# Versión original por Ronald L. Rivest el 14 de febrero de 2007
# Revisión por Erik D. Demaine el 31 de enero de 2011
#
# Uso:
#    docdist1.py filename1 filename2
#     
# Este programa calcula la "distancia" entre dos archivos de texto
# como el ángulo entre sus vectores de frecuencia de palabras (en radianes).
#
# Para cada archivo de entrada, se calcula un vector de frecuencia de palabras de la siguiente manera:
#    (1) se lee el archivo especificado
#    (2) se convierte en una lista de "palabras" alfanuméricas
#        Aquí, una "palabra" es una secuencia de caracteres alfanuméricos consecutivos.
#        Los caracteres no alfanuméricos se tratan como espacios en blanco.
#        La mayúscula y minúscula no son significativas.
#    (3) se determina la frecuencia de aparición de cada palabra
#    (4) las listas de palabras/frecuencia se ordenan alfabéticamente
#
# La "distancia" entre dos vectores es el ángulo entre ellos.
# Si x = (x1, x2, ..., xn) es el primer vector (xi = frecuencia de la palabra i)
# y y = (y1, y2, ..., yn) es el segundo vector,
# entonces el ángulo entre ellos se define como:
#    d(x,y) = arccos(producto_interno(x,y) / (norma(x)*norma(y)))
# donde:
#    producto_interno(x,y) = x1*y1 + x2*y2 + ... xn*yn
#    norma(x) = sqrt(producto_interno(x,x))

import math
import sys

##################################
# Operación 1: leer un archivo de texto ##
##################################
def leer_archivo(filename):
    """ 
    Leer el archivo de texto con el nombre dado;
    devolver una lista de las líneas de texto en el archivo.
    """
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except IOError:
        print("Error al abrir o leer el archivo de entrada:", filename)
        sys.exit()

#################################################
# Operación 2: dividir las líneas de texto en palabras ##
#################################################
def obtener_palabras_de_lista_de_lineas(L):
    """
    Analizar la lista dada L de líneas de texto en palabras.
    Devolver una lista de todas las palabras encontradas.
    """
    lista_palabras = []
    for linea in L:
        palabras_en_linea = obtener_palabras_de_cadena(linea)
        lista_palabras = lista_palabras + palabras_en_linea
    return lista_palabras

def obtener_palabras_de_cadena(linea):
    """
    Devolver una lista de las palabras en la cadena de entrada dada,
    convirtiendo cada palabra a minúsculas.

    Entrada:  linea (una cadena)
    Salida: una lista de cadenas 
              (cada cadena es una secuencia de caracteres alfanuméricos)
    """
    lista_palabras = []          # acumula palabras en la línea
    lista_caracteres = []     # acumula caracteres en la palabra
    for c in linea:
        if c.isalnum():
            lista_caracteres.append(c)
        elif len(lista_caracteres) > 0:
            palabra = "".join(lista_caracteres)
            palabra = palabra.lower()
            lista_palabras.append(palabra)
            lista_caracteres = []
    if len(lista_caracteres) > 0:
        palabra = "".join(lista_caracteres)
        palabra = palabra.lower()
        lista_palabras.append(palabra)
    return lista_palabras

##############################################
# Operación 3: contar la frecuencia de cada palabra ##
##############################################
def contar_frecuencia(lista_palabras):
    """
    Devolver una lista con pares de forma: (palabra, frecuencia)
    """
    L = []
    for nueva_palabra in lista_palabras:
        for entrada in L:
            if nueva_palabra == entrada[0]:
                entrada[1] = entrada[1] + 1
                break
        else:
            L.append([nueva_palabra, 1])
    return L

###############################################################
# Operación 4: ordenar palabras en orden alfabético          ###
###############################################################
def orden_insercion(A):
    """
    Ordenar la lista A en orden, en su lugar.

    De Cormen/Leiserson/Rivest/Stein,
    Introduction to Algorithms (segunda edición), página 17,
    modificado para ajustar el hecho de que las listas de Python usan 
    indexación desde 0.
    """
    for j in range(len(A)):
        key = A[j]
        # insertar A[j] en la secuencia ordenada A[0..j-1]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A
    
#############################################
## calcular frecuencias de palabras para el archivo de entrada ##
#############################################
def frecuencias_palabras_para_archivo(filename):
    """
    Devolver una lista ordenada alfabéticamente de pares (palabra, frecuencia) 
    para el archivo dado.
    """

    lista_lineas = leer_archivo(filename)
    lista_palabras = obtener_palabras_de_lista_de_lineas(lista_lineas)
    mapa_frecuencias = contar_frecuencia(lista_palabras)
    orden_insercion(mapa_frecuencias)

    print("Archivo", filename, ":")
    print(len(lista_lineas), "líneas,")
    print(len(lista_palabras), "palabras,")
    print(len(mapa_frecuencias), "palabras distintas")

    return mapa_frecuencias

def producto_interno(L1, L2):
    """
    Producto interno entre dos vectores, donde los vectores
    están representados como pares (palabra, frecuencia) ordenados alfabéticamente.

    Ejemplo: producto_interno([["y",3],["de",2],["el",5]],
                           [["y",4],["en",1],["de",1],["esto",2]]) = 14.0 
    """
    suma = 0.0
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        # L1[i:] y L2[j:] aún por procesar
        if L1[i][0] == L2[j][0]:
            # ambos vectores tienen esta palabra
            suma += L1[i][1] * L2[j][1]
            i += 1
            j += 1
        elif L1[i][0] < L2[j][0]:
            # la palabra L1[i][0] está en L1 pero no en L2
            i += 1
        else:
            # la palabra L2[j][0] está en L2 pero no en L1
            j += 1
    return suma

def angulo_vectorial(L1, L2):
    """
    La entrada es una lista de pares (palabra, frecuencia), ordenados alfabéticamente.

    Devolver el ángulo entre estos dos vectores.
    """
    numerador = producto_interno(L1, L2)
    denominador = math.sqrt(producto_interno(L1, L1) * producto_interno(L2, L2))
    return math.acos(numerador / denominador)

def main():
    if len(sys.argv) != 3:
        print("Uso: docdist1.py filename1 filename2")
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        lista_palabras_ordenadas_1 = frecuencias_palabras_para_archivo(filename_1)
        lista_palabras_ordenadas_2 = frecuencias_palabras_para_archivo(filename_2)
        distancia = angulo_vectorial(lista_palabras_ordenadas_1, lista_palabras_ordenadas_2)
        print("La distancia entre los documentos es: %0.6f (radianes)" % distancia)

if __name__ == "__main__":
    main()



    
    



