def metros(m):
    if opcion == 1 and opcion_2 == 1:
        return m * 39.3701 
# elif opcion == 1 and opcion_2 == 2: 
    elif opcion_2 == 2:
        return m * 3.28084
    elif opcion_2 == 3:
        return m * (1/1609.344)
    elif opcion_2 == 4:
        return m * 1.09361

def kilogramos(kg):
    if opcion == 2 and opcion_2 == 1:
        return kg * (6.022 * (10**26))
    elif opcion_2 == 2:
        return kg * 35.2745
    elif opcion_2 == 3:
        return kg * 2.20462

def segundos(s):
    if opcion == 3 and opcion_2 == 1:
        return s * (1/60)
    elif opcion_2 == 2:
        return s * (1/3600)

def temp(T):
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

def presion(P):
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

def volumen(m3):
    if opcion == 6 and opcion_2 == 1: 
        return m3 * (10**-3)
    elif opcion_2 == 2:
        return m3 * (6.102*10**4)
    elif opcion_2 == 3: 
        return m3 * 35.31      

def prefijos(u):
    if opcion == 7 and opcion_2 == 1: 
        return u * (10**-18)
    elif opcion_2 == 2:
        return u * (10**-15)
    elif opcion_2 == 3: 
        return u * (10**-12)
    elif opcion_2 == 4:
        return u * (10**-9)
    elif opcion_2 == 5: 
        return u * (10**-6)
    elif opcion_2 == 6:
        return u * (10**-3)
    elif opcion_2 == 7: 
        return u * (10**-2)
    elif opcion_2 == 8:
        return u * (10**-1)
    elif opcion_2 == 9: 
        return u * (10**3)
    elif opcion_2 == 10:
        return u * (10**6)
    elif opcion_2 == 11: 
        return u * (10**9)
    elif opcion_2 == 12:
        return u * (10**12)
    elif opcion_2 == 13: 
        return u * (10**15)
    elif opcion_2 == 14:
        return u * (10**18)

def menu(opcion):
    #opcion = int(input())
    """
    print("""
    """
    ¿Qué magnitud quieres convertir?
    1 - Longitud
    2 - Masa
    3 - Tiempo
    4 - Temperatura
    5 - Presión
    6 - Volumen
    7 - Quiero convertir unidades usando prefijos
    """
    # opcion = int(input())

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
        1. a (1 * 10^-18)
        2. f (1 * 10^-15)
        3. p (1 * 10^-12)
        4. n (1 * 10^-9)
        5. µ (1 * 10^-6)
        6. m (1 * 10^-3)
        7. c (1 * 10^-2)
        8. d (1 * 10^-1)
        9. k (1 * 10^3)
        10. M (1 * 10^6)
        11. G (1 * 10^9)
        12.	T (1 * 10^12)
        13.	P (1 * 10^15)
        14.	E (1* 10^18)
        """)

def conversiones(opcion, opcion_2):
    # opcion_2 = int(input())
    if opcion == 1:
        m = float(input("Introduce metros: "))
        if opcion_2 == 1:
            print(f"{m} m = {metros(m)} in")
        elif opcion_2 == 2:
            print(f"{m} m = {metros(m)} ft")
        elif opcion_2 == 3:
            print(f"{m} m = {metros(m)} mi")
        elif opcion_2 == 4:
            print(f"{m} m = {metros(m)} yd")

    if opcion == 2:
        kg = float(input("Introduce kilogramos: "))
        if opcion_2 == 1:
            print(f"{kg} kg = {kilogramos(kg)} uma")
        elif opcion_2 == 2:
            print(f"{kg} kg = {kilogramos(kg)} on")
        elif opcion_2 == 3:
            print(f"{kg} kg = {kilogramos(kg)} lb")

    if opcion == 3:
        s = float(input("Introduce segundos: "))
        if opcion_2 == 1:
            print(f"{s} s = {segundos(s)} min")
        elif opcion_2 == 2:
            print(f"{s} s = {segundos(s)} hr")

    if opcion == 4:
        if opcion_2 == 1:
            T = float(input("Introduce grados Kelvin: "))
            print(f"{T} K = {temp(T)} °C")
        elif opcion_2 == 2:
            T = float(input("Introduce grados Kelvin: "))
            print(f"{T} K = {temp(T)} °F")
        elif opcion_2 == 3:
            T = float(input("Introduce grados Celcius: "))
            print(f"{T} °C = {temp(T)} K")
        elif opcion_2 == 4:
            T = float(input("Introduce grados Celcius: "))
            print(f"{T} °C = {temp(T)} °F")
        elif opcion_2 == 5:
            T = float(input("Introduce grados Fahrenheit: "))
            print(f"{T} °F = {temp(T)} °C")

    if opcion == 5:
        P = float(input("Introduce pascales: "))
        if opcion_2 == 1:
            print(f"{P} pas = {presion(P)} bar")
        elif opcion_2 == 2:
            print(f"{P} pas = {presion(P)} atm")
        elif opcion_2 == 3:
            print(f"{P} pas = {presion(P)} mmHg")
        elif opcion_2 == 4:
            print(f"{P} pas = {presion(P)} lb/in^2")
        elif opcion_2 == 5:
            print(f"{P} atm = {presion(P)} mmHg")

    if opcion == 6:
        m3 = float(input("Introduce metros cúbicos: "))
        if opcion_2 == 1:
            print(f"{m3} m^3 = {volumen(m3)} lt")
        elif opcion_2 == 2:
            print(f"{m3} m^3 = {volumen(m3)} in^3")
        elif opcion_2 == 3:
            print(f"{m3} m^3 = {volumen(m3)} ft^3")

    if opcion == 7:
        u = float(input("Introduce unidades: "))
        if opcion_2 == 1:
            print(f"{prefijos(u)} a")
        elif opcion_2 == 2:
            print(f"{prefijos(u)} f")
        elif opcion_2 == 3:
            print(f"{prefijos(u)} p")
        elif opcion_2 == 4:
            print(f"{prefijos(u)} n")
        elif opcion_2 == 5:
            print(f"{prefijos(u)} µ")
        elif opcion_2 == 6:
            print(f"{prefijos(u)} m")
        elif opcion_2 == 7:
            print(f"{prefijos(u)} c")
        elif opcion_2 == 8:
            print(f"{prefijos(u)} d")
        elif opcion_2 == 9:
            print(f"{prefijos(u)} k")
        elif opcion_2 == 10:
            print(f"{prefijos(u)} M")
        elif opcion_2 == 11:
            print(f"{prefijos(u)} G")
        elif opcion_2 == 12:
            print(f"{prefijos(u)} T")
        elif opcion_2 == 13:
            print(f"{prefijos(u)} P")
        elif opcion_2 == 14:
            print(f"{prefijos(u)} E")
    
def continuar(c):
    # c = int(input("""
    # ¿Deseas hacer otra conversión?
    # 1 - Sí
    # 2 - No
    # """))
    if c == 1:
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
Fin :)""")

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
