
def opc1_stock_plataf(juegoscatalog,inventariojuegos):
    stockconso = 0
    busqued = input("Ingrese el nombre de la consola a consultar: ").lower
    for juego in juegoscatalog:
        if juego:[1] == busqued
        stockconso += inventariojuegos[juego][1]
    if stockconso == 0:
        print("No hubo resultados")
    else:
        print("Stock disponible: ",stockconso)

def opc2_busqueda_por_precio(valmin,valmax,juegoscatalog,inventariojuegos):
    for juegoo in inventariojuegos:
        if valmin <= inventariojuegos[juegoo][0] and valmax >= inventariojuegos[juegoo][0]:
            print("Nombre: ",juegoscatalog[juegoo][0]," Code: ",juegoscatalog[juegoo])

def opc3_buscar_code(code,inventariojuegos):
    for juegos in inventariojuegos:
        if code == inventariojuegos[juegos]:
            return True
    if code not in inventariojuegos:
        return False

def opc3_actualizar_precio(code,nuevoprec,inventariojuegos):
    inventariojuegos[code][0] = nuevoprec
    print("Precio cambiado correctamente!")

def opc4_val_code(codenew,inventariojuegos):
    for juegos in inventariojuegos:
        if inventariojuegos[juegos] == codenew:
            return False
    if codenew.strip() == "" or codenew in inventariojuegos:
        return False
    if codenew not in inventariojuegos and codenew.strip() != "":
        return True
    

def opc4_val_titulo(titulonew):
    if titulonew.strip() == "":
        return False
    else:
        return True
    
def opc4_val_plat(plataformanew):
    if plataformanew.strip() == "":
        return False
    else:
        return True
    
def opc4_val_gen(generonew):
    if generonew.strip() == "":
        return False
    else:
        return True
    
def opc4_val_clase(clasenew):
    if clasenew not in ["e","t","m"]:
        return False
    else:
        return True
    
def opc4_val_mult():
    while True:
        multipla = input("Ingrese si tiene multiplayer (s/n):")
        if multipla in ["s","n"]:
            break
        else:
            print("Ingrese opción válida")
    if multipla == "s":
        return True
    if multipla == "n":
        return False
    
def opc4_val_edit(editornew):
    if editornew.strip() == "":
        return False
    else:
        return True
    
def opc4_val_precio(precionew):
    if precionew > 0:
        return True
    else:
        return False
    
def opc4_val_stock(stocknew):
    if stocknew >= 0:
        return True
    else:
        return False
    
def opc4_agregar_juego(juegoscatalog,codenew,titulonew,plataformanew,generonew,clasenew,multivalid,editornew,precionew,stocknew):
    print("Agregando...")
    juegoscatalog = juegoscatalog.append([codenew][titulonew,plataformanew,generonew,clasenew,multivalid,editornew])
    inventariojuegos = inventariojuegos.append([codenew][precionew,stocknew])
    
def opc5_elim_juego(codigoelim,juegoscatalog,inventariojuegos):
    print("Eliminando...")
    juegoscatalog = juegoscatalog.remove(codigoelim)
    inventariojuegos = inventariojuegos.remove(codigoelim)