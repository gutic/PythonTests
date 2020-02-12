#generar un programa q va ser importado para informar resultados de puntajes usando matri
def fecha():
    archmov = open('colision.txt','r+')
    linea = archmov.readline()
    fecha = 0
    while linea != "":
        linea = linea.split(",")
        fecha = linea[1].split("/")
        print fecha[0]
        print fecha[1]
        print fecha[2]
        linea = archmov.readline()




def abro_arch(anio):
    archmov = open('colision.txt','r+')
    linea = archmov.readline()
    BuscoAnio = anio
    fecha = []
    fechant = []
    m = crear_matriz(33,14)
    x = 1
    for x in range(13):
        m[0][x] = "mes", x  #Agrego en todas las posiciones 0.x la palabra mes y el num crptie
        x +=1
    m[0][0] = "num usr"
    m[0][13] = "Total"
    m[32][0] = "total"
    archmov = open('colision.txt','r')
    linea = archmov.readline()
    dia = []
    mes = []
    anio = []
    x=1
    while linea != "":
        linea = linea.split(",")
        fecha = linea[1].split("/")
        if  BuscoAnio == int(fecha[2]):
            archusr = open('user.txt','r')
            linea1 = archusr.readline()
            while linea1 != "":
                linea1 = linea1.split(",")
                if linea1[0] == linea[0]:
                    m[int(linea1[0])][0] = str(linea1[1])
                linea1 = archusr.readline()
        linea = archmov.readline()
    archusr.close()
    archmov.close()
    archmov = open('colision.txt','r')
    linea = archmov.readline()
    puntos = 0
    dia = []
    mes = []
    anio = []
    x=1
    while linea != "":
        linea = linea.split(",")
        fecha = linea[1].split("/")
        if BuscoAnio == int(fecha[2]):
            if str(linea[3]) == "pc" or str(linea[3]) == "pl" or str(linea[3]) == "bala":
                m[int(linea[0])][int(fecha[1])] += 1
                m[int(linea[0])][13] += 1
                m[32][13] += 1
                m[32][int(fecha[1])] += 1
        linea = archmov.readline()
    mostrar_matriz(m)

def mostrar_desde():
    usr = raw_input("numero de usr ? \n")
    f = 0
    ini = raw_input("fecha desde dd/mm/aa \n")
    fin = raw_input("fecha hasta dd/mm/aa | Enter hasta final \n")
    if fin == "":
        f = 1
        print "vacio"
    archmov = open('colision.txt','r')
    linea = archmov.readline()
    x = 1
    while linea != "":
        linea = linea.split(",")
        if str(linea[1]) == str(ini) and str(linea[0]) == usr:
            print "entro"
            if f == 0:
                while str(linea[1]) != fin and str(linea[0]) == usr:
                    x += 1
                    linea = archmov.readline()
                    linea = linea.split(",")
            elif f == 1:
                while linea != "" and str(linea[0]) == usr:
                    x +=1
                    linea = archmov.readline()
        linea = archmov.readline()
    archmov.close()
    print x
    m = crear_matriz(x,5)
    m[0][0] = "fecha"
    m[0][1] = "objeto 1 con"
    m[0][2] = "Objeto 2"
    m[0][3] = "Eje x"
    m[0][4] = "Eje Y"
    archmov = open('colision.txt','r')
    linea = archmov.readline()
    x = 1
    while linea != "":
        linea = linea.split(",")
        if str(linea[1]) == str(ini) and str(linea[0]) == usr:
            if f == 0:
                while str(linea[1]) != fin and str(linea[0]) == usr:
                    m[x][0] = str(linea[1])
                    m[x][1] = str(linea[2])
                    m[x][2] = str(linea[3])
                    m[x][3] = str(linea[4])
                    m[x][4] = str(linea[5])
                    x +=1
                    linea = archmov.readline()
                    linea = linea.split(",")
            elif  f == 1:
                while linea != "" and str(linea[0]) == usr:
                    m[x][0] = str(linea[1])
                    m[x][1] = str(linea[2])
                    m[x][2] = str(linea[3])
                    m[x][3] = str(linea[4])
                    m[x][4] = str(linea[5])
                    x +=1
                    linea = archmov.readline()
                    linea = linea.split(",")
        linea = archmov.readline()
    mostrar_matriz(m)


def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas): #DEFINO FILAS
        matriz.append([0] * columnas) #DEFINO LAS COLUMNAS
    return matriz

def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(filas):
        for columna in range(columnas):
            print  "{0:11} ".format(matriz[fila][columna]), #doy formato al imprimir
        print

def main():
    opcion = input("ingrese el anio\n")
    abro_arch(opcion)

main()
