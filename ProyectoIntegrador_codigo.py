conversionesOp = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 39.3701, 3.2808, 6.2137e-4, 1.0936, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 6.022e26, 35.2745, 2.2046, 9.807, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0.0166666, 2.77777e-4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 273.15, 459.67, 273.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 1e-5, 9.8692e-6, 7.5e-3, 1.45038e-4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 1e-3, 6.102e4, 35.31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 1e-18 , 1e-15, 1e-12, 1e-9, 1e-6, 1e-3, 1e-2, 1e-1, 1e3, 1e6, 1e9, 1e12, 1e15, 1e18]
]

unidades = [
    ['','','','','','','','','','','','','','',''],
    ['','metros', 'metros', 'metros', 'metros', '', '', '', '', '', '', '', '', '', ''],
    ['','kilogramos', 'kilogramos', 'kilogramos', 'kilogramos', '', '', '', '', '', '', '', '', '', ''],
    ['','segundos', 'segundos', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', 'grados Kelvin', 'grados Kelvin', 'grados Celcius', 'grados Celcius', 'grados Fahrenheit', '', '', '', '', '', '', '', ''],
    ['','pascales', 'pascales', 'pascales', 'pascales', 'atmósferas', '', '', '', '', '', '', '', '', ''],
    ['','metros cúbicos', 'metros cúbicos', 'metros cúbicos', '', '', '', '', '', '', '', '', '', '', ''],
    ['','unidades', 'unidades', 'unidades', 'unidades', 'unidades', 'unidades', 'unidades', 'unidades', 'unidades', 'unidades', 'unidades', 'unidades', 'unidades', 'unidades']
]

conversionesLtt = [
    ['','','','','','','','','','','','','','',''],
    ['','in', 'ft', 'mi', 'yd', '', '', '', '', '', '', '', '', '', ''],
    ['','uma', 'on', 'lb', 'N', '', '', '', '', '', '', '', '', '', ''],
    ['','min', 'hrs', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['','°C', '°F', 'K', '°F', '°C', '', '', '', '', '', '', '', '', ''],
    ['','bar', 'atm', 'mmHg', 'lb/in^2', 'pas', '', '', '', '', '', '', '', '', ''],
    ['','lt', 'in^3', 'ft^3', '', '', '', '', '', '', '', '', '', '', ''],
    ['','a','f','p','n','µ','m','c','d','k','M','G','T','P','E']
]


def menuPrincipal():
    opcion = int(input("""
    ¿Qué magnitud quieres convertir?
    1 - Longitud
    2 - Masa
    3 - Tiempo
    4 - Temperatura
    5 - Presión
    6 - Volumen
    7 - Quiero convertir unidades usando prefijos

"""))
    while 0 < opcion < 9:
        print('''
    ¿Qué unidades/prefijos quieres convertir?''')
        break

    if (opcion == 1):
        print('''
    1. m - in
    2. m - ft
    3. m - mi
    4. m - yd2
        ''')
        opcion2 = int(input())
        return (opcion, opcion2)

    elif (opcion == 2):
        print("""
    1. kg - uma
    2. kg - on
    3. kg - lb
    4. kg - peso en Tierra
        """)
        opcion2 = int(input())
        return (opcion, opcion2)

    elif (opcion == 3):
        print("""
    1. s - min
    2. s - hr
        """)
        opcion2 = int(input())
        return (opcion, opcion2)

    elif (opcion == 4):
        print("""
    1. K - °C
    2. K - °F
    3. °C - K
    4. °C - °F
    5. °F - °C
        """)
        opcion2 = int(input())
        return (opcion, opcion2)

    elif (opcion == 5):
        print("""
    1. pas - bar
    2. pas - atm
    3. pas - mmHg
    4. pas - lb/in^2
    5. atm - pas
        """)
        opcion2 = int(input())
        return (opcion, opcion2)

    elif (opcion == 6):
        print("""
    1. m^3 - lt
    2. m^3 - in^3
    3. m^3 - ft^3
        """)
        opcion2 = int(input())
        return (opcion, opcion2)

    elif (opcion == 7):
        print("""
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
        opcion2 = int(input())
        return (opcion, opcion2)
    
    else: 
        print("Opción no válida")


def conversiones():
    datosMenu =  menuPrincipal()
    i = datosMenu[0]
    j = datosMenu[1]
    operador = conversionesOp[i][j]
    entrada = unidades[i][j]
    salida = conversionesLtt[i][j]
    v = float (input(f"Introduce {entrada}: "))
    
    if i == 4 and j <= 2:
        temperatura = v - operador
        print (v,entrada,'=',temperatura,salida)
    
    elif i == 4 and j == 3:
        temperatura2 = v + operador
        print (v,entrada,'=',temperatura2,salida)
    
    elif i == 4 and j == 4:
        temperatura3 = (v * 1.8) + 32
        print (v,entrada,'=',temperatura3,salida)
    
    elif i == 4 and j == 5:
        temperatura4 = (v - 32) / 1.8
        print(v,entrada,'=',temperatura4,salida)

    else: 
        conversion = v * operador
        print (v,entrada,'=',conversion,salida)


def continuar(c):
    while c == 1:
        conversiones()
        c = int(input("""
    ¿Deseas hacer otra conversión?
    1 - Sí
    2 - No

"""))
        continue
    else: 
        print('''
Gracias por usar esta calculadora :)
        ''')


print('''
CALCULADORA DE CONVERSIONES
Basada en el SI
T1208
''')
conversiones()
c = int(input("""
    ¿Deseas hacer otra conversión?
    1 - Sí
    2 - No

"""))
continuar(c)