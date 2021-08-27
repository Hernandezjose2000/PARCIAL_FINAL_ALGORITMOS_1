import csv


def menu() ->int:

    opciones = ["Procesar archivos","Agregar o eliminar un gasto al archivo gasto.csv",
                "Cantidad de dinero recaudado","Top 3 productos mas comprados",
                "Reporte de porcentaje por de cada gasto sobre el total", "Incidencia en porcentaje de cada articulo"] 
    
    for opcion in range(len(opciones)):
        print(f"{opcion+1}){opciones[opcion]}")
    
    decision_usuario = int(input("\nPor favor marque la opcion deseada "))

    return decision_usuario


def cargar_informacion(nombre_archivo:str) ->list:



    '''Se usa try/except para que si no se consigue el archivo capte el error
        e informe el error al usuario y no nos frene el programa por completo y poder seguir operando'''

    lineas_archivo = list()
    try:
        with open(nombre_archivo, "r")as archivo:
            leer_archivo = csv.reader(archivo, delimiter=',') 
            for id_linea in leer_archivo:                     
                lineas_archivo.append(id_linea)
    except FileNotFoundError:
        print("Marque 1 nuevamente debido a que no se econtro dicho archivo")
    
    return lineas_archivo


def mostrar_top_tres_productos(ventas:list) ->None:

    lista_cantidad_compradas = list()
    top_tres = list()

    for id_producto,nombre,precio_por_kilo,cantidad_en_stock,cantidad_kilo_vendida,compras_clientes in ventas:
        lista_cantidad_compradas.append(int(compras_clientes))

    lista_cantidad_compradas.sort()
    lista_cantidad_compradas.reverse()
    lista_top_tres = lista_cantidad_compradas[0:3]

    print("El top 3 de los productos mas comprados esta formado por:")
    for producto_cantidad_vendida in lista_top_tres:
        for id_producto,nombre,precio_por_kilo,cantidad_en_stock,cantidad_kilo_vendida,compras_clientes in ventas:
            if (int(producto_cantidad_vendida) == int(compras_clientes)) :
                print(f"Producto:{nombre} -- Cantidad de veces comprada:{compras_clientes} veces")
 
    
def porcentaje_gastos(gastos:list) ->None:

    listaddo_gastos = list()
    porcentajes = list()

    for concepto,importe in gastos:
        listaddo_gastos.append(int(importe))
    
    monto_total_gastos = sum(listaddo_gastos)
    for concepto, importe in gastos:
        porcentajes.append((int(importe)/monto_total_gastos)*100)

    print("El total de los gastos es de:",sum(listaddo_gastos))

    porcentajes.sort()
    porcentajes.reverse()

    for porcentaje in porcentajes:
        for concepto,importe in gastos:
            if porcentaje == (int(importe)/monto_total_gastos)*100:
                print(f"El/La {concepto} representa el {porcentaje} % del gasto total con un importe de: {int(importe)}")
    

def dinero_recaudado(gastos:list, ventas:list) ->None:

    lista_ventas_por_productos = list()
    lista_gastos = list()

    for producto,nombre,precio,cantidad_stock,kilo_vendido,veces_comprado in ventas:
        lista_ventas_por_productos.append(int(precio)*int(kilo_vendido))
    
    print(f"El monto total de dinero recaudado es de: {sum(lista_ventas_por_productos)}")

    for concepto,importe in gastos:
        lista_gastos.append(int(importe))
    
    suma_total_gastos = sum(lista_gastos)

    restante = sum(lista_ventas_por_productos) - suma_total_gastos
    print(f"El monto total de los gastos de este mes es de: {suma_total_gastos}")

    if restante == 0:
        print(f"Si alcanzamos a cubrir los gastos de este mes, alcanzamos justo nos queda {restante} a favor, no tenemos ni deuda ni ganancia")
    
    elif restante > 0:
        print(f"Si alcanzamos a cubrir los gastos quedandonos a favor el siguiente saldo: {restante}")
    else:
        print(f"No alcanzamos a cubrir los gastos des este mes, nos estaria faltando para poder completar los gastos la cifra de:{restante*(-1)}")


def agregar_eliminar_gastos(gastos:list) ->None:

    listado_gastos = list()

    for concepto,importe in gastos:
        listado_gastos.append(concepto)
    
    decision = int(input("Por favor marque 1 si desea eliminar un gasto o 2 si desea agregar otro gasto "))

    if decision == 1:
        for id_gasto in range(len(listado_gastos)):
            print(f"{id_gasto+1}){listado_gastos[id_gasto]}")
        
        linea = int(input("Por favor marque el id de gasto a eliminar ")) - 1
        gastos.pop(linea)
        print(gastos)
    
    elif decision == 2:
        concepto = input("Ingrese el nombre del gasto ")
        importe = int(input("Por favor ingrese el importe de dicho gast "))
        gastos.append([concepto,importe])
        print(gastos)

    with open("gastos.csv","w")as archivo:
        archivo_a_escribir = csv.writer(archivo, delimiter=',')

        for concepto,importe in gastos:
            archivo_a_escribir.writerow((concepto,importe))
        
        if decision == 1:
            print("GASTO ELIMINADO")
        else:
            print("GASTO AGREGADO")

    print("Revisa el archivo gastos puesto que se modifico en base a tu decision!")


def reporte_incidencias(gastos:list, ventas:list) ->None:

    listado_gastos = list()
    listado_productos_vendidos = list()

    for concepto,importe in gastos:
        listado_gastos.append(int(importe))
    
    sumatoria_gastos_totales = sum(listado_gastos)
    print("Para un gasto total de:",sumatoria_gastos_totales)

    for id_producto,nombre,precio_kilo,cantidad_por_kilo,cantidad_kilo_vendida,veces_comprada in ventas:
        cantidad_producto = int(precio_kilo)*int(cantidad_kilo_vendida)
        print(f"El/La {nombre} representa una incidencia del {(cantidad_producto/sumatoria_gastos_totales)*100} % de los gastos totales")


def main() ->None:

    
    continuar = False
    while not continuar:
        decision_user = menu()
                                
        if decision_user == 1:
            ventas = cargar_informacion("ventas.csv")
            gastos = cargar_informacion("gastos.csv")
            print("Archivos procesados")

        elif decision_user ==2:
            agregar_eliminar_gastos(gastos)

        elif decision_user == 3:
            dinero_recaudado(gastos, ventas)

        elif decision_user == 4:
            mostrar_top_tres_productos(ventas)

        elif decision_user == 5:
            porcentaje_gastos(gastos)

        elif decision_user == 6:
            reporte_incidencias(gastos, ventas)

        else:
            print("\nIntroduciste una opcion invalida")
        
        decision_continuar = int(input("\nMarque 1 si desea continuar o 2 si desea salir del programa "))

        if decision_continuar == 1:
            print("\nSigamos entonces")
        else:
            continuar = True
    
    print("chao")


main()
#En el nombre, de Dios, Amen.
