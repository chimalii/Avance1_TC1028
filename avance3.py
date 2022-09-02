def metros(n1):
    if opcion == 1 and opcion_2 == 1:
        m_in = n1 * 39.3701
        return m_in 
    elif opcion == 1 and opcion_2 == 2:
        m_ft = n1 * 3.28084
        return m_ft
    elif opcion == 1 and opcion_2 == 3:
        m_mi = n1 * 0.000621371
        return m_mi
    elif opcion == 1 and opcion_2 == 4:
        m_yd = n1 * 1.09361
        return m_yd

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
    1. kg - on
    2. kg - lb
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
    3. m^3 - in^3
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
    11.	G (1 * 10^9)
    12.	T (1 * 10^12)
    13.	P (1 * 10^15)
    14.	E (1* 10^18)
    """)

opcion_2 = int(input())
if opcion_2 == 1:
    n1 = float(input("Introduce metros: "))
    print(f"{n1} m = {metros(n1)} in")

elif opcion_2 == 2:
    n1 = float(input("Introduce metros: "))
    print(f"{n1} m = {metros(n1)} ft")

elif opcion_2 == 3:
    n1 = float(input("Introduce metros: "))
    print(f"{n1} m = {metros(n1)} yd")

elif opcion_2 == 3:
    n1 = float(input("Introduce metros: "))
    print(f"{n1} m = {metros(n1)} mi")

elif opcion_2 == 3:
    n1 = float(input("Introduce metros: "))
    print(f"{n1} m = {metros(n1)} yd")