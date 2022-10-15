def menuPrincipal():
    print("""
    ¿Qué magnitud quieres convertir?
    1 - Longitud
    2 - Masa
    3 - Tiempo
    4 - Temperatura
    5 - Presión
    6 - Volumen
    7 - Quiero convertir unidades usando prefijos
    """)

def metros(m, opcion_2):
    if opcion == 1 and opcion_2 == 1:
        return m * 39.3701 
    elif opcion_2 == 2:
        return m * 3.28084
    elif opcion_2 == 3:
        return m * (1/1609.344)
    elif opcion_2 == 4:
        return m * 1.09361

def kilogramos(kg, opcion_2):
    if opcion == 2 and opcion_2 == 1:
        return kg * (6.022 * (10**26))
    elif opcion_2 == 2:
        return kg * 35.2745
    elif opcion_2 == 3:
        return kg * 2.20462

def segundos(s, opcion_2):
    if opcion == 3 and opcion_2 == 1:
        return s * (1/60)
    elif opcion_2 == 2:
        return s * (1/3600)

def temp(T, opcion_2):
    if opcion == 4 and opcion_2 == 1: 
        return T - 273.15
    elif opcion_2 == 2:
        return T - 459.67
    elif opcion_2 == 3:
        return T + 273.15
    elif opcion_2 == 4:
        return (T - 32) / 1.8
    elif opcion_2 == 5:
        return (T * 1.8) + 32

def presion(P, opcion_2):
    if opcion == 5 and opcion_2 == 1: 
        return P / 10**5
    elif opcion_2 == 2:
        return P / 101325
    elif opcion_2 == 3:
        return P * 0.0075
    elif opcion_2 == 4:
        return P / 6894.745
    elif opcion_2 == 5:
        return P * 760

def volumen(m3, opcion_2):
    if opcion == 6 and opcion_2 == 1: 
        return m3 * (10**-3)
    elif opcion_2 == 2:
        return m3 * (6.102*10**4)
    elif opcion_2 == 3: 
        return m3 * 35.31      

def conPrefijos(u,opcion_2):
    prefijos = [1, 1e-18 , 1e-15, 1e-12, 1e-9, 1e-6, 1e-3, 1e-2, 1e-1, 1e3, 1e6, 1e9, 1e12, 1e15, 1e18]
    if opcion == 7:
        x = opcion_2
        cont = 0
        for opcion_2 in range(len(prefijos)): # range(len(prefijos)): esto imprime las multiplicaciones de lo introducido por todos los valores en la lista
            prefijo = u * (prefijos[opcion_2]) #(prefijos[opcion_2])         
            if cont < x:
                cont = cont+1
            else:
                print (prefijo) 
                break

def menu(opcion):

    if (opcion == 1):
        print("""
    ¿Qué unidades quieres convertir?
    1. m - in
    2. m - ft
    3. m - mi
    4. m - yd
        """)

    elif (opcion == 2):
        print("""
    ¿Qué unidades quieres convertir?
    1. kg - uma
    2. kg - on
    3. kg - lb
        """)

    elif (opcion == 3):
        print("""
    ¿Qué unidades quieres convertir?
    1. s - min
    2. s - hr
        """)

    elif (opcion == 4):
        print("""
    ¿Qué unidades quieres convertir?
    1. K - °C
    2. K - °F
    3. °C - K
    4. °C - °F
    5. °F - °C
        """)

    elif (opcion == 5):
        print("""
    ¿Qué unidades quieres convertir?
    1. pas - bar
    2. pas - atm
    3. pas - mmHg
    4. pas - lb/in^2
    5. atm - mmHg
        """)

    elif (opcion == 6):
        print("""
    ¿Qué unidades quieres convertir?
    1. m^3 - lt
    2. m^3 - in^3
    3. m^3 - ft^3
        """)

    elif (opcion == 7):
        print("""
    ¿Qué unidades quieres convertir?
    0. a (1 * 10^-18) 
    1. f (1 * 10^-15)
    2. p (1 * 10^-12)
    3. n (1 * 10^-9)
    4. µ (1 * 10^-6)
    5. m (1 * 10^-3)
    6. c (1 * 10^-2)
    7. d (1 * 10^-1)
    8. k (1 * 10^3)
    9. M (1 * 10^6)
    10. G (1 * 10^9)
    11.	T (1 * 10^12)
    12.	P (1 * 10^15)
    13.	E (1* 10^18)
        """)

def conversiones(opcion, opcion_2):
    # opcion_2 = int(input())
    if opcion == 1:
        m = float(input("Introduce metros: "))
        if opcion_2 == 1:
            print(f"{m} m = {metros(m, opcion_2)} in")
        elif opcion_2 == 2:
            print(f"{m} m = {metros(m, opcion_2)} ft")
        elif opcion_2 == 3:
            print(f"{m} m = {metros(m, opcion_2)} mi")
        elif opcion_2 == 4:
            print(f"{m} m = {metros(m, opcion_2)} yd")

    if opcion == 2:
        kg = float(input("Introduce kilogramos: "))
        if opcion_2 == 1:
            print(f"{kg} kg = {kilogramos(kg, opcion_2)} uma")
        elif opcion_2 == 2:
            print(f"{kg} kg = {kilogramos(kg, opcion_2)} on")
        elif opcion_2 == 3:
            print(f"{kg} kg = {kilogramos(kg, opcion_2)} lb")

    if opcion == 3:
        s = float(input("Introduce segundos: "))
        if opcion_2 == 1:
            print(f"{s} s = {segundos(s, opcion_2)} min")
        elif opcion_2 == 2:
            print(f"{s} s = {segundos(s, opcion_2)} hr")

    if opcion == 4:
        if opcion_2 == 1:
            T = float(input("Introduce grados Kelvin: "))
            print(f"{T} K = {temp(T, opcion_2)} °C")
        elif opcion_2 == 2:
            T = float(input("Introduce grados Kelvin: "))
            print(f"{T} K = {temp(T, opcion_2)} °F")
        elif opcion_2 == 3:
            T = float(input("Introduce grados Celcius: "))
            print(f"{T} °C = {temp(T, opcion_2)} K")
        elif opcion_2 == 4:
            T = float(input("Introduce grados Celcius: "))
            print(f"{T} °C = {temp(T, opcion_2)} °F")
        elif opcion_2 == 5:
            T = float(input("Introduce grados Fahrenheit: "))
            print(f"{T} °F = {temp(T, opcion_2)} °C")

    if opcion == 5:
        P = float(input("Introduce pascales: "))
        if opcion_2 == 1:
            print(f"{P} pas = {presion(P, opcion_2)} bar")
        elif opcion_2 == 2:
            print(f"{P} pas = {presion(P, opcion_2)} atm")
        elif opcion_2 == 3:
            print(f"{P} pas = {presion(P, opcion_2)} mmHg")
        elif opcion_2 == 4:
            print(f"{P} pas = {presion(P, opcion_2)} lb/in^2")
        elif opcion_2 == 5:
            print(f"{P} atm = {presion(P, opcion_2)} mmHg")

    if opcion == 6:
        m3 = float(input("Introduce metros cúbicos: "))
        if opcion_2 == 1:
            print(f"{m3} m^3 = {volumen(m3, opcion_2)} lt")
        elif opcion_2 == 2:
            print(f"{m3} m^3 = {volumen(m3, opcion_2)} in^3")
        elif opcion_2 == 3:
            print(f"{m3} m^3 = {volumen(m3, opcion_2)} ft^3")

    if opcion == 7:
        u = float(input("Introduce unidades: "))
        conPrefijos(u,opcion_2)
    
def continuar(c):
    if c == 1:
        menuPrincipal()
        opcion = int(input())
        menu(opcion)
        opcion_2 = int(input())
        conversiones(opcion, opcion_2)
        c = int(input("""
¿Deseas hacer otra conversión?
1 - Sí
2 - No

"""))
        continuar(c)
    else:
        print("""
Fin :)
""")

menuPrincipal()   
opcion = int(input())
# opcion_2 = int(input())
menu(opcion)
opcion_2 = int(input())
conversiones(opcion, opcion_2)
c = int(input("""
¿Deseas hacer otra conversión?
1 - Sí
2 - No

"""))
continuar(c)
