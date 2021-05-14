#from pythonProject.PIA_conta.tablas import SEPARADOR
import pandas as pd
import numpy as np
SEPARADOR="*"
print("\n\n")
i=0
nombre=["CL","CE","CR"]
tiempo=["1er. Semestre","2do. Semestre"]
print("\t\tPRESUPUESTO MAESTRO\n")
print("\t\tI. Presupuesto de Operación.\n")
lista=[]
total_presupuesto1=[]
lista_presupuestoV=[]
while i<3:
    total=0
    lista=[]
    print(f"\nProducto {nombre[i]}")
    for j in tiempo:
        print(j)
        u_vender=int(input("Escribe unidades a vender: "))
        precio_de_venta=float(input("Escribe el precio de venta:"))
        total=total+u_vender*precio_de_venta
        lista.append([int(u_vender),int(precio_de_venta),int(u_vender*precio_de_venta)])
    lista_presupuestoV.append(lista)
    total_presupuesto1.append(int(total))
    print("\n")
    i+=1

print(lista_presupuestoV)
print(total_presupuesto1)
#lista_presupuestoV=[[[12000, 300, 3600000], [10000, 320, 3200000]], [[13500, 280, 3780000], [11800, 310, 3658000]], [[7000, 185, 1295000], [8500, 200, 1700000]]]
#total_presupuesto1=[6800000, 7438000, 2995000]
#lista_presupuestoV=[[[1000, 200, 2000000], [5000, 220, 1100000]], [[6000, 100, 600000], [4000, 120, 480000]], [[5000, 150, 750000], [5000, 150, 750000]]]
#total_presupuesto1=[3100000, 1080000,1500000]

tabla1=[]
contador=0
for i in lista_presupuestoV:
    print(f"Producto {nombre[contador]}")
    presupuesto_de_ventas = {"1er. Semestre":i[0], "2do. Semestre":i[1], \
                        "Total":["","",total_presupuesto1[contador]]}
    contador+=1
    cedula1 = pd.DataFrame(presupuesto_de_ventas)
    cedula1.index = ["Unidades a vender", "Precio de venta", "IMporte de venta"]
    print(cedula1)
    tabla1.append(cedula1)
    print("\n")
total_ventasxSem=0
for i in total_presupuesto1:
    total_ventasxSem+=i
print(f"\nTotal de ventas por Semestre => {total_ventasxSem}")

print(tabla1[0].at["Unidades a vender","1er. Semestre"])
print(tabla1[1].at["Unidades a vender","1er. Semestre"])
print(SEPARADOR*30)

#*********----PARTE 2----***********

print("\n\t\t2-Determinacion del saldo de Clientes y Flujos de Entradas\n")
titulo=int(input("Escribe el año del Balance"))
#titulo=2015
saldo_de_clientes=float(input(f"Saldo de clientes {titulo}: "))
#saldo_de_clientes=80000
total_clientes=saldo_de_clientes+total_ventasxSem
print("Entradas de Efectivo:")
cobranza_anio1=saldo_de_clientes
porcentaje=float(input("Inserta el porcentaje del año 2"))
porcentaje2=float(input("Inserta el porcentaje del año 1"))
#porcentaje=0.8
cobranza_anio2=total_ventasxSem*porcentaje
total_cobranza=cobranza_anio1+cobranza_anio2
saldo_de_clientesT=total_clientes-total_cobranza
print("\n")
print("\n\nDeterminacion del saldo de Clientes y Flujos de Entradas")
tabla2={"Importe":["","","",saldo_de_clientes,cobranza_anio2,"",""],"Total":[saldo_de_clientes,total_ventasxSem,total_clientes,"","",total_cobranza,saldo_de_clientesT]}
tabla=pd.DataFrame(tabla2)
tabla.index=["Saldo de clientes", "Ventas", "Total de Clientes","Cobranza del año 1","Cobranza del año 2","Total de Entradas","Saldo de Clientes"]
print(tabla)
print(SEPARADOR*30)

#*********----PARTE 3----***********
#comentarizar lista3t y listatotal
print("\n\t\t3. Presupuesto de Producción \n")
lista3t=[]
i=0
t=0
lista3total=[]
while i<3:
    print(f"\nProducto {nombre[i]}")
    inventario_final=int(input(f"Escribe el inventario final {tiempo[0]}"))
    n=0
    lista3=[]
    for j in tiempo:
        t=tabla1[i].at["Unidades a vender",j]+inventario_final
        inventario_inicial=t-inventario_final
        if n==0:
            lista3.append([tabla1[i].at["Unidades a vender",j],inventario_final,t,inventario_final,inventario_inicial])
        else:
            inventario_final2=int(input(f"Escribe el inventario final {tiempo[n]}"))
            t2=tabla1[i].at["Unidades a vender",j]+inventario_final2
            inventario_inicialt=t2-inventario_final
            lista3.append([tabla1[i].at["Unidades a vender",j],inventario_final2,t2,inventario_final,inventario_inicialt])
        n+=1
    lista3t.append(lista3)
    i+=1

    
print(lista3t)
for i in lista3t:
    posicion1=i[0][0]+i[1][0]

    lista3total.append([posicion1,i[1][1],posicion1+i[1][1],i[0][1],posicion1+i[1][1]-i[0][1]])
print(lista3total)
#lista3t=[[[12000, 10000, 22000, 10000, 12000], [10000, 6500, 16500, 10000, 6500]], [[13500, 8500, 22000, 8500, 13500], [11800, 7500, 19300, 8500, 10800]], [[7000, 6000, 13000, 6000, 7000], [8500, 5000, 13500, 6000, 7500]]]
#lista3total=[[22000, 6500, 28500, 10000, 18500], [25300, 7500, 32800, 8500, 24300], [15500, 5000, 20500, 6000, 14500]]

tabla3=[]
contador=0
for i in lista3t:
    print(f"Producto {nombre[contador]}")
    presupuesto_de_ventas = {"1er. Semestre":i[0], "2do. Semestre":i[1], \
                        "Total":lista3total[contador]}
    contador+=1
    cedula3 = pd.DataFrame(presupuesto_de_ventas)
    cedula3.index = ["Unidades a vender", "(+) Inventario final", "Total de Unidades","(-)Inventario inicial","(=)Unidades a Producir"]
    tabla3.append(cedula3)
    
    print("\n")
for i in tabla3:
    print(i)
print(SEPARADOR*30)
int(input("Continua numero....."))
#***************Part1e 4*******************
print("\n\t\t 4. Presupuesto de Requerimiento de Materiales\n")
#quitar los comentarios con solo hacer un comentario en lista4completa
tiempo4=["1er. Semestre","2do. Semestre","Total"]
indicador=0
lista4=[]
lista4_completa=[]
t4=0
for i in tabla3:
    
    print(f"Producto {nombre[indicador]}")
    
    for j in tiempo4:
        lista4=[]
        requerimiento=float(input("Requerimiento material: "))
        print(t4)
        for x in tiempo4:
            t4=i.at["(=)Unidades a Producir",x]
            lista4.append([requerimiento,requerimiento*t4])
        lista4_completa.append(lista4)    
    indicador+=1
    print("\n")
print(lista4_completa)
#lista4_completa=[[[1.0, 12000.0], [1.0, 6500.0], [1.0, 18500.0]], [[0.5, 6000.0], [0.5, 3250.0], [0.5, 9250.0]], [[10.0, 120000.0], [10.0, 65000.0], [10.0, 185000.0]], [[1.2, 16200.0], [1.2, 12960.0], [1.2, 29160.0]], [[0.6, 8100.0], [0.6, 6480.0], [0.6, 14580.0]], [[25.0, 337500.0], [25.0, 270000.0], [25.0, 607500.0]], [[2.0, 14000.0], [2.0, 15000.0], [2.0, 29000.0]], [[1.0, 7000.0], [1.0, 7500.0], [1.0, 14500.0]], [[5.0, 35000.0], [5.0, 37500.0], [5.0, 72500.0]]]
contador=0
listeng=[0,1,2]
material=["A","B","C"]
tabla4=[]
contador=0
contador1=0
print(nombre[0])
for i in lista4_completa:
    
    if contador ==3:
        print("*"*60)
        contador=0
        print(nombre[contador+1])
        nombre.pop(0)
    
    presupuesto_de_requsrimiento = {"1er. Semestre":i[0], "2do. Semestre":i[1], \
                            "Total":i[2]}
    cedula4 = pd.DataFrame(presupuesto_de_requsrimiento)
        
    cedula4.index = [f"Requerimiento de material {material[contador]}", "Total de Material requerido"]
    print(cedula4)
    tabla4.append(cedula4)
    contador+=1
nombre=["CL","CE","CR"]
print("***************")

sumatablaA4=0
sumatablaB4=0
sumatablaC4=0
LISTA_TABLA4=[]
listasumaA=[]
listasumaB=[]
listasumaC=[]

for i in range(0,9,3):
    sumatablaA4+=tabla4[i].at[f"Total de Material requerido","1er. Semestre"]
    sumatablaB4+=tabla4[i].at[f"Total de Material requerido","2do. Semestre"]
    sumatablaC4+=tabla4[i].at[f"Total de Material requerido","Total"]
listasumaA.append(sumatablaA4)
listasumaB.append(sumatablaB4)
listasumaC.append(sumatablaC4)
sumatablaA4=0
sumatablaB4=0
sumatablaC4=0
for i in range(1,9,3):
    sumatablaA4+=tabla4[i].at[f"Total de Material requerido","1er. Semestre"]
    sumatablaB4+=tabla4[i].at[f"Total de Material requerido","2do. Semestre"]
    sumatablaC4+=tabla4[i].at[f"Total de Material requerido","Total"]
listasumaA.append(sumatablaA4)
listasumaB.append(sumatablaB4)
listasumaC.append(sumatablaC4)
sumatablaA4=0
sumatablaB4=0
sumatablaC4=0
for i in range(2,9,3):
    sumatablaA4+=tabla4[i].at[f"Total de Material requerido","1er. Semestre"]
    sumatablaB4+=tabla4[i].at[f"Total de Material requerido","2do. Semestre"]
    sumatablaC4+=tabla4[i].at[f"Total de Material requerido","Total"]
listasumaA.append(sumatablaA4)
listasumaB.append(sumatablaB4)
listasumaC.append(sumatablaC4)
sumatablaA4=0
sumatablaB4=0
sumatablaC4=0
lista4=[]
lista4.append(listasumaA)
lista4.append(listasumaB)
lista4.append(listasumaC)

presupuesto_de_requerimiento4 = {"1er. Semestre":listasumaA, "2do. Semestre":listasumaB, \
                            "Total":listasumaC}
total_cedula4 = pd.DataFrame(presupuesto_de_requerimiento4)
total_cedula4.index = ["Material A", "Material B","Material C"]
print(total_cedula4)

#*********************-----5----*****************
print("\n\t\t5. Presupuesto de Compra de Materiales\n")
print(total_cedula4.at[f"Material {material[0]}","1er. Semestre"])
#nomas cometaizen lista5Total y vuelvan a marcar lo comentado
i=0

lista5Total=[]
n=0
while i<3:
    lista5=[]
    inventario_final=int(input(f"Escribe el inventario final de {material[i]}"))
    n=0
    for j in tiempo:
        
        requerimiento5=total_cedula4.at[f"Material {material[i]}",j]
        if n==1:
            inventario_final=int(input(f"Escribe el inventario final de {material[i]} {j}"))
            total5=requerimiento5+inventario_final
            material_comprar=total5-lista5[0][1]
            precio=float(input(f"Escribe el precio de la compra de {material[i]}: "))
            total5material=material_comprar*precio
            lista5.append([requerimiento5,inventario_final,total5,lista5[0][1],material_comprar,precio,total5material])
    
        else:
            total5=requerimiento5+inventario_final
            material_comprar=total5-inventario_final
            precio=float(input(f"Escribe el precio de la compra de {material[i]}: "))
            total5material=material_comprar*precio
            n+=1
            lista5.append([requerimiento5,inventario_final,total5,inventario_final,material_comprar,precio,total5material])
    
    lista5Total.append(lista5)
    i+=1
print(lista5Total)


#lista5Total=[[[42200.0, 5000, 47200.0, 5000, 42200.0, 10.0, 422000.0], [34460.0, 3000, 37460.0, 5000, 32460.0, 12.0, 389520.0]], [[21100.0, 3000, 24100.0, 3000, 21100.0, 2.0, 42200.0], [17230.0, 2500, 19730.0, 3000, 16730.0, 3.0, 50190.0]], [[492500.0, 2000, 494500.0, 2000, 492500.0, 1.0, 492500.0], [372500.0, 1800, 374300.0, 2000, 372300.0, 2.0, 744600.0]]]
lista5_sumaT=[]
lista5_sumafinal=[]

suma5_1=0
suma5_2=0
suma5_3=0
suma5_5=0
for i in lista5Total:
    suma5_1=0
    suma5_5=0
    for j in i:
        
        suma5_1+=j[0]
        suma5_2=j[1]
        suma5_3=j[3]
        suma5_5+=j[6]
    
    lista5_sumafinal.append([suma5_1,suma5_2,suma5_2+suma5_1,suma5_3,(suma5_2+suma5_1)-suma5_3,0,suma5_5])

n=0
for i in lista5Total:
    
    i.append(lista5_sumafinal[n])
    n+=1

n=0
compras5_1=0
compras5_2=0

compras_totales5=0
tabla5=[]
for i in lista5Total:
    print(f"Material {material[n]}")
    presupuesto_de_requerimiento5 = {"1er. Semestre":i[0], "2do. Semestre":i[1], \
                            "Total":i[2]}
    compras5_1+=i[0][6]
    compras5_2+=i[1][6]
    total_cedula5 = pd.DataFrame(presupuesto_de_requerimiento5)
    total_cedula5.index = ["Requerimiento de materiales", "Inventario Final","Total de Materiales","Inventario Inicial","Material a comprar","Precio de Compra","Total de Material A en $:"]
    tabla5.append(total_cedula5)
    print(total_cedula5)
    n+=1
    
#Es importante tener en cuenta la variable compras_totales5 para las siguientes tablas
compras_totales5=compras5_1+compras5_2
print(compras_totales5)
#************************6********************
print("\t\t6. Determinación del saldo de Proveedores y Flujo de Salidas\n")
#Escribe saldo de provedores y porcentaje6
provedores=float(input("Escribe el saldo de proveedores: "))
porcentaje6=float(input("Escribe el porcentaje de las compras presupuestadas: "))
#provedores=33500
#porcentaje6=0.5
total_proveedores6=compras_totales5+provedores
por_proveedores61=compras_totales5*porcentaje6
por_proveedores62=provedores+por_proveedores61
total_salidas_6=total_proveedores6-por_proveedores62
proveedores_y_flujo = {"Importe":["","","",provedores,por_proveedores61,"",""], "Total":[provedores,compras_totales5,total_proveedores6,"","",por_proveedores62,total_salidas_6]}
total_cedula6 = pd.DataFrame(proveedores_y_flujo)
total_cedula6.index = ["Saldo de Proveedores", "Compras","Total de Proveedores","Por Proveedores de 1","Por Proveedores de 2","Total de Salidas2 ","Saldo de Proveedores del año 2"]
print(total_cedula6)
print(SEPARADOR*30)
int(input("escribe un numeros"))
print("\n\t\t7. Presupuesto de Mano de Obra Directa \n")


horas1=float(input("Escribe las horas del primer producto: "))
horas2=float(input("Escribe las horas del segundo producto: "))
horas3=float(input("Escribe las horas del tercer producto: "))
cuota71=float(input("Escribe la couta por hora primer semestre: "))
cuota72=float(input("Escribe la cuota por hora segundo semestre"))
'''horas1=2.0
horas2=1.0
horas3=1.5
cuota71=15.0
cuota72=18.0'''
cuotas=[cuota71,cuota72]
horas_total7=[horas1,horas2,horas3]

tabla7=[]
tabla7new=[]
n=0
for i in tabla3:
    tabla7new=[]
    x=0
    for j in tiempo:
        unidades_producir7=i.at["(=)Unidades a Producir",j]
        total_horas7=unidades_producir7*horas_total7[n]
        tabla7new.append([unidades_producir7,horas_total7[n],total_horas7,cuotas[x],total_horas7*cuotas[x]])
        x+=1
    tabla7.append(tabla7new)
    n+=1

total7=[]

for i in tabla7:
    unity7=0
    horasreq7=0
    total_horas_req7=0
    importe_mod=0
    for j in i:
        unity7+=j[0]
        horasreq7=j[1]
        total_horas_req7+=j[2]
        importe_mod+=j[4]
    total7.append([unity7,horasreq7,total_horas_req7,"",importe_mod])
i=0

while i<3:
    tabla7[i].append(total7[i])
    i+=1



n=0
total7_1=0
total7_2=0
t71=0
t72=0
tabla7_other=[]
for i in tabla7:
    print(f"Material {nombre[n]}")
    presupuesto_de_requerimiento7 = {"1er. Semestre":i[0], "2do. Semestre":i[1], \
                            "Total":i[2]}
    total7_1+=i[0][4]
    total7_2+=i[1][4]
    t71+=i[0][2]
    t72+=i[1][2]
    total_cedula7 = pd.DataFrame(presupuesto_de_requerimiento7)
    total_cedula7.index = ["Unidades a producir","Horas requeridas por unidad","Total de horas requeridas","Cuota por hora","Importe de M.O.D."]
    tabla7_other.append(total_cedula7)
    print(total_cedula7)
    print("\n")
    n+=1
totatales7=total7_1+total7_2
tt7=t71+t72

print("Total de horas requeridas por semestre: ",tt7)
print("Total de M.O.D. por semestre: ",totatales7)
print("\n\t\t8. Presupuesto de Gastos Indirectos de Fabricación \n")
#Comentarizar la matriz presupuesto8 para seguir a bajo

presupuesto8=[]
columna=["1er. Semestre","2do. Semestre","Total"]
d8=0
s8=0
m8=0
e8=0
v8=0
suma8t=0
for i in columna:
    if i=="Total":
        presupuesto8.append([d8,s8,m8,e8,v8,suma8t])
    else:
        print(f"{i}")
        depreciacion8=float(input("Escribe la depreciacion : "))
        d8+=depreciacion8
        seguros8=float(input("Escribe el seguro: "))
        s8+=seguros8
        mantenimiento8=float(input("Escribe el mantenimiento: "))
        m8+=mantenimiento8
        energeticos8=float(input("Escribe el energetico: "))
        e8+=energeticos8
        varios8=float(input("Escribe una cantidad de varios: "))
        v8+=varios8
        suma8=depreciacion8+seguros8+mantenimiento8+energeticos8+varios8
        suma8t+=suma8
        presupuesto8.append([depreciacion8,seguros8,mantenimiento8,energeticos8,varios8,suma8])

#presupuesto8=[[40000.0, 12500.0, 33000.0, 40000.0, 12500.0, 138000.0], [40000.0, 12500.0, 25000.0, 35000.0, 12500.0, 125000.0], [80000.0, 25000.0, 58000.0, 75000.0, 25000.0, 263000.0]]
print(presupuesto8)
presupuesto8_t = {"1er. Semestre":presupuesto8[0], "2do. Semestre":presupuesto8[1], \
                            "Total":presupuesto8[2]}

total_cedula8 = pd.DataFrame(presupuesto8_t)
total_cedula8.index = ["Depreciación","Seguros","Mantenimiento","Energéticos","Varios","Total G.I.F. por semestre"]
print(total_cedula8)
total_GIF=total_cedula8.at["Total G.I.F. por semestre","Total"]
tt8=tt7#variable de cedula7
print("Total de G.I.F. ",total_GIF)
print("(/) Total horas M.O.D. Anual:",tt8)
c_total8=round((total_GIF/tt8),2)
print("(=) Costo por Hora de G.I.F. ",c_total8)
estado_flujo=total_GIF-total_cedula8.at["Depreciación","Total"]#Variable despues de las tablas
print(SEPARADOR*30)
print("\n\t\t9. Presupuesto de Gastos de Operación\n")
presupuesto9=[]

columna=["1er. Semestre","2do. Semestre","Total"]
d9=0
s9=0
m9=0
e9=0
v9=0
suma9t=0
for i in columna:
    if i=="Total":
        presupuesto9.append([d9,s9,m9,e9,v9,suma9t])
    else:
        print(f"{i}")
        depreciacion9=float(input("Escribe la depreciacion : "))
        d9+=depreciacion9
        seguros9=float(input("Escribe el sueldos y salarios: "))
        s9+=seguros9
        mantenimiento9=float(input("Escribe el comisiones: "))
        m9+=mantenimiento9
        energeticos9=float(input("Escribe el varios: "))
        e9+=energeticos9
        varios9=float(input("Escribe una Interes por prestamo: "))
        v9+=varios9
        suma9=depreciacion9+seguros9+mantenimiento9+energeticos9+varios9
        suma9
        suma9t+=suma9
        presupuesto9.append([depreciacion9,seguros9,mantenimiento9,energeticos9,varios9,suma9])
#presupuesto9=[[7500.0, 125000.0, 86750.0, 10000.0, 2500.0, 231750.0], [7500.0, 125000.0, 85580.0, 8000.0, 2500.0, 228580.0], [15000.0, 250000.0, 172330.0, 18000.0, 5000.0, 460330.0]]
print(presupuesto9)
presupuesto9_t = {"1er. Semestre":presupuesto9[0], "2do. Semestre":presupuesto9[1], \
                            "Total":presupuesto9[2]}

total_cedula9 = pd.DataFrame(presupuesto9_t)
total_cedula9.index = ["Depreciación","Sueldos y Salarios","ComisioneVarios","Varios","Intereses por Préstamo","Total de Gastos de Operación:"]
print(total_cedula9)
int(input("Escribe un numero"))
print("\n\t\t10. Determinación del Costo Unitario de Productos Terminados \n")
columna10=["Costo","Cantidad","Costo Unitario"]

i=0
j=0
lista10=[]
lista10_T=[]
material=["A","B","C"]
while i<9:
    j=0
    lista10=[]
    while j<3:
        n=tabla4[i].at[f"Requerimiento de material {material[j]}","1er. Semestre"]
        lista10.append(n)
        j+=1
        i+=1
    lista10_T.append(lista10)
j=0
for i in lista10_T:
    i.append(tabla7_other[j].at["Horas requeridas por unidad","1er. Semestre"])
    i.append(tabla7_other[j].at["Horas requeridas por unidad","1er. Semestre"])
    j+=1


columna=["Costo","Cantidad","Costo Unitario"]
j=0
p10=[]

maeterialA10=float(input("Escribe la depreciacion : "))
            
maeterialB10=float(input("Escribe el seguro: "))
            
maeterialC10=float(input("Escribe el mantenimiento: "))
            
Mano10=float(input("Escribe el energetico: "))
#quitar los valores del ciclo
while j<3:
    a10=1
    b10=1
    c10=1
    mo10=1
    g10=1
    suma10t=0
    suma10=0
    presupuesto10=[]
    
    for i in columna:
        if i=="Costo Unitario":
            presupuesto10.append([a10,b10,c10,mo10,g10,(a10+b10+c10+mo10+g10)])
        elif i=="Cantidad":
            presupuesto10.append([lista10_T[j][0],lista10_T[j][1],lista10_T[j][2],lista10_T[j][3],lista10_T[j][4],""])
            a10*=lista10_T[j][0]
            b10*=lista10_T[j][1]
            c10*=lista10_T[j][2]
            mo10*=lista10_T[j][3]
            g10*=lista10_T[j][4]
            #suma10=lista10_T[0][0]+lista10_T[0][1]+lista10_T[0][2]+lista10_T[0][3]+suma10
        else:
            
            maeterialA10=maeterialA10
            #maeterialA10=12
            maeterialB10=maeterialB10
            #maeterialB10=3
            maeterialC10=maeterialC10
            #maeterialC10=2
            Mano10=Mano10
            #Mano10=18
            
            Gastos10=c_total8
            
            a10*=maeterialA10
            b10*=maeterialB10
            c10*=maeterialC10
            mo10*=Mano10
            g10*=Gastos10
            
            
            presupuesto10.append([maeterialA10,maeterialB10,maeterialC10,Mano10,Gastos10,""])
    p10.append(presupuesto10)
    j+=1

tabla10=[]
n=0
for i in p10:
    print("\n",nombre[n])
    presupuesto10_t = {"Costo":i[0], "Cantidad":i[1], \
                                "Costo Unitario":i[2]}
    total_cedula10 = pd.DataFrame(presupuesto10_t)
    total_cedula10.index = ["Material A","Material B","Material C","Mano de Obra","Gastos Indirectos de Fabricación","Costo Unitario"]
    tabla10.append(total_cedula10)
    print(total_cedula10)
    n+=1

print("\n\t\t11. Valuación de Inventarios Finales\n")
tabla11=[]#Primera tabla inventario final de materiales
a11=tabla5[0].at["Inventario Final","2do. Semestre"]
b11=tabla5[1].at["Inventario Final","2do. Semestre"]
c11=tabla5[2].at["Inventario Final","2do. Semestre"]
ca11=maeterialA10*a11
cb11=maeterialB10*b11
cc11=maeterialC10*c11
suma11=ca11+cb11+cc11
presupuesto11_t = {"Unidades":[a11,b11,c11,""], "Costo Unitario":[maeterialA10,maeterialB10,maeterialC10,""],"Costo Total":[ca11,cb11,cc11,suma11]}
total_cedula11 = pd.DataFrame(presupuesto11_t)
total_cedula11.index = ["Material A","Material B","Material C","Inventario Final de Materiales"]
tabla11.append(total_cedula11)
print(total_cedula11)
print("-"*160)
print("\nInventario final de producto")

tabla11_t=[]
an11=tabla10[0].at["Costo Unitario","Costo Unitario"]
bn11=tabla10[1].at["Costo Unitario","Costo Unitario"]
cn11=tabla10[2].at["Costo Unitario","Costo Unitario"]


a11=tabla3[0].at["(+) Inventario final","2do. Semestre"]
b11=tabla3[1].at["(+) Inventario final","2do. Semestre"]
c11=tabla3[2].at["(+) Inventario final","2do. Semestre"]
ca11=an11*a11
cb11=bn11*b11
cc11=cn11*c11
suma11=ca11+cb11+cc11
presupuesto11_t = {"Unidades":[a11,b11,c11,""], "Costo Unitario":[an11,bn11,cn11,""],"Costo Total":[ca11,cb11,cc11,suma11]}
total_cedula11 = pd.DataFrame(presupuesto11_t)
total_cedula11.index = ["Material CL","Material CE","Material CR","Inventario Final de Materiales"]
tabla11_t.append(total_cedula11)
print(total_cedula11)
print("\n\n\t\t\t\tII. Presupuesto financiero\n")

saldo_inicial=float(input("Escribe el saldo inicial: "))#45000
material_disponible=saldo_inicial+compras_totales5
inventario_final12=tabla11[0].at["Inventario Final de Materiales","Costo Total"]
matriales_utilizados=material_disponible-inventario_final12
costo_produccion=matriales_utilizados+totatales7+total_GIF
inventario_inicial_PT=float(input("Escribe el inventario final de los productos termiados:\n"))#135000
ttp=costo_produccion+inventario_inicial_PT
inventario_final_PT=tabla11_t[0].at["Inventario Final de Materiales","Costo Total"]
costo_venta=ttp-inventario_final_PT
estado_C = {"Costos":[saldo_inicial,compras_totales5,material_disponible,inventario_final12,matriales_utilizados,totatales7,total_GIF,costo_produccion,inventario_inicial_PT,ttp,inventario_final_PT,costo_venta]}
total_estado_C = pd.DataFrame(estado_C)
total_estado_C.index = ["Saldo Inicial de Materiales","(+) Compras de Materiales","(=) Material Disponible","(-) Inventario Final de Materiales","(=) Materiales Utilizados","(+) Mano de Obra Directa","(+) Gastos de Fabricación Indirectos","(=) Costo de Producción","(+) Inventario Inicial de Productos Terminados","(=) Total de Producción Disponible","(-) Inventario Final de Productos Terminados","(=) Costo de Ventas"]
print(total_estado_C)
print("*"*80)#segunda parte

print("\n\t\tEstados de Resultados")
costo_ER=total_estado_C.at["(=) Costo de Ventas","Costos"]
UB=total_ventasxSem-costo_ER
GO=total_cedula9.at["Total de Gastos de Operación:","Total"]
UOP=UB-GO
isr=0.3#float(input("Escribe en el procentaje del ISR: "))
ptu=0.1#float(input("Escribe en el procentaje del PTU: "))
isr_ER=UOP*isr
ptu_ER=UOP*ptu
ER_Total=UOP-isr_ER-ptu_ER
estado_r = {"Costos":[total_ventasxSem,costo_ER,UB,GO,UOP,isr_ER,ptu_ER,ER_Total]}
total_estado_r = pd.DataFrame(estado_r)
total_estado_r.index = ["Ventas","(-) Costo de Ventas","(=) Utilidad Bruta","(-) Gastos de Operación","(=) Utilidad de Operación","(-) ISR","(-) PTU","(=) Utilidad Neta"]
print(total_estado_r)
print("*"*60)
print("\n\t\tEstado de flujo efectivo\n")
saldo_inicial_E=float(input("Escribe el saldo inicial: "))#100000
print("Entradas")

cobranza1_E=tabla.at["Cobranza del año 2","Importe"]
cobranza2_E=tabla.at["Saldo de clientes","Total"]
#####
Total_entradas=cobranza1_E+cobranza2_E
Efectivo_d=Total_entradas+saldo_inicial_E
#####
provedores1_1=total_cedula6.at["Saldo de Proveedores del año 2","Total"]
provedores2_1=total_cedula6.at["Por Proveedores de 1","Importe"]
pagoMOD=totatales7#7
pagoGIF=total_GIF-total_cedula8.at["Depreciación","Total"]
pagoGO=total_cedula9.at["Total de Gastos de Operación:","Total"]-total_cedula9.at["Depreciación","Total"]
CAF=float(input("Escribe la Compra de Activo Fijo (Maquinaria): "))#85000
pago_isr=float(input("Escribe Pago ISR: "))#50000
isr_ER=0
####
Total_salidas=provedores1_1+provedores2_1+pagoMOD+pagoGIF+pagoGO+CAF+pago_isr+isr_ER
print(Total_salidas)
estado_f = {"uno":["",cobranza1_E,cobranza2_E,"","",provedores1_1,provedores2_1,pagoMOD,pagoGIF,pagoGO,CAF,pago_isr,isr_ER,"",""],"dos":[saldo_inicial_E,"","",Total_entradas,Efectivo_d,"","","","","","","","",Total_salidas,(Efectivo_d-Total_salidas)]}
total_estado_f = pd.DataFrame(estado_f)
total_estado_f.index = ["Saldo Inicial de Efectivo","Cobranza 2","Cobranza 1","Total de Entradas","Efectivo Disponible","Proveedores 2","Proveedores 1","Pago Mano de Obra Directa","Pago Gastos Indirectos de Fabricación","Pago de Gastos de Operación","Compra de Activo Fijo (Maquinaria)","Pago ISR 1","Pago ISR2","Total de Salidas","Flujo de Efectivo Actual"]
print(total_estado_f)
