
from ExamenFunciones import opc1_stock_plataf,opc2_busqueda_por_precio,opc3_buscar_code,opc3_actualizar_precio,opc4_val_clase,opc4_val_code,opc4_val_edit,opc4_val_gen,opc4_val_mult,opc4_val_plat,opc4_val_precio,opc4_val_stock,opc4_val_titulo,opc4_agregar_juego,opc5_elim_juego


juegoscatalog = {
    "G001":["Eclipse Runner", "pc", "accion", "T", True, "NovaStudio"],
    "G002":["Puzzle Atlas", "switch", "puzzle", "E", False, "BrightWorks"],
    "G003":["Sky Legends", "ps5", "aventura", "T", True, "OrionGames"],
    "G004":["Racing Pulse", "pc", "carreras", "E", True, "VelocityLab"],
    "G005":["Mystic Farm", "switch", "simulacion", "E", False, "GreenSeed"],
    "G006":["Shadow Tactics", "xbox", "estrategia", "M", False, "IronGate"]
}

inventariojuegos = {
    "G001":[9990, 7],
    "G002":[19990, 0],
    "G003":[42990, 3],
    "G004":[14990, 5],
    "G005":[17990, 9],
    "G006":[39990, 2]
}



while True:
    print("---GAMEHUB---")
    print("")
    print("1.- Stock por plataforma")
    print("2.- Búsqueda de juegos por rango de precio")
    print("3.- Actualizar precio de juego")
    print("4.- Agregar juego")
    print("5.- Eliminar juego")
    print("6.- Salir")
    print("")

    try:
        op = int(input("Ingrese una opción: "))
        if op in [1,2,3,4,5,6]:
            break
        else:
            print("Ingrese opción válida!")
            continue
    except ValueError:
            print("Ingrese opción válida!")
    if op == 1:
        opc1_stock_plataf(juegoscatalog,inventariojuegos)
    if op == 2:
        while True:
            try:
                valmin = int(input("Ingrese valor mínimo: "))
                if valmin > 0:
                    break
                else:
                    print("Ingrese número válido")
                    continue
            except ValueError:
                print("Ingrese número válido")
        while True:
            try:
                valmax = int(input("Ingrese valor máximo: "))
                if valmax > valmin:
                    break
                else:
                    print("Ingrese número válido")
                    continue
            except ValueError:
                print("Ingrese número válido")
        opc2_busqueda_por_precio(valmax,valmin,juegoscatalog,inventariojuegos)
        
    if op == 3:
        while True:
            code = input("Ingrese código del juego").upper()
            busqueda = opc3_buscar_code(code,inventariojuegos)
            if busqueda == False:
                print("No se encontro el juego")
            elif busqueda == True:
                while True:
                    try:
                        nuevoprec = int(input("Ingrese nuevo precio: "))
                        if nuevoprec > 0:
                            opc3_actualizar_precio(code,nuevoprec,inventariojuegos)
                            break
                        else:
                            print("Ingrese precio válido")
                            continue
                    except ValueError:
                        print("Ingrese número entero")
                        continue
            while True:
                seguir = input("¿Desea actualizar otro precio? (s/n)").lower
                if seguir not in ["s","n"]:
                    print("Ingrese opción válida")
                    continue
                else:
                    break
            if seguir == "s":
                continue
            else:
                break
    if op == 4:
        while True:
            codenew = input("Ingrese código de juego: ")
            codevalid = opc4_val_code(codenew,inventariojuegos)
            if codevalid == True:
                break
            elif codevalid == False:
                print("Código inválido")
        while True:
            titulonew = input("Ingrese nombre del juego: ")
            titulovalid = opc4_val_titulo(titulonew)
            if titulovalid == True:
                break
            elif titulovalid == False:
                print("Título inválido")
        while True:
            plataformanew = input("Ingrese plataforma: ")
            plataformavalid = opc4_val_plat(plataformanew)
            if plataformavalid == True:
                break
            elif plataformavalid == False:
                print("Plataforma inválida")
        while True:
            generonew = input("Ingrese género: ")
            generovalid = opc4_val_gen(generonew)
            if generovalid == True:
                break
            elif generovalid == False:
                print("Género inválido")
        while True:
            clasenew = input("Ingrese clasificación: ")
            clasevalid = opc4_val_clase(clasenew)
            if clasevalid == True:
                break
            elif clasevalid == False:
                print("Clasificación inválida")
        multivalid = opc4_val_mult()
        while True:
            editornew = input("Ingrese editor: ")
            editorvalid = opc4_val_edit(editornew)
            if editorvalid == True:
                break
            elif editorvalid == False:
                print("Editor inválido")
        while True:
            try:
                precionew = int(input("Ingrese precio del juego: "))
            except ValueError:
                print("Ingrese número entero")
            preciovalid = opc4_val_precio(precionew)
            if preciovalid == True:
                break
            elif preciovalid == False:
                print("Precio inválido")
        while True:
            try:
                stocknew = int(input("Ingrese stock: "))
            except ValueError:
                print("Ingrese número entero")
            stockvalid = opc4_val_stock(stocknew)
            if stockvalid == True:
                break
            elif stockvalid == False:
                print("Stock inválido")
        opc4_agregar_juego(juegoscatalog,codenew,titulonew,plataformanew,generonew,clasenew,multivalid,editornew,precionew,stocknew)
        print("Juego agregado!")
    if op == 5:
        codigoelim = input("Ingrese código del juego a eliminar: ").upper()
        busqueda = opc3_buscar_code(codigoelim,inventariojuegos)
        if busqueda == True:
            opc5_elim_juego(codigoelim,inventariojuegos,juegoscatalog)
            print("Juego eliminado")
        if busqueda == False:
            print("Juego no encontrado")
    if op == 6:
        break