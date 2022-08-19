# Avance1_TC1028
Selección del tema de proyecto y set up de repositorio
- El proyecto de centra en el desarrollo de unan calculadora de conversión de unidades de longitud, de metros a cualquiera de sus múltiplos o submúltiplos en el Sistema Internacional desde E (1*1018) hasta a (1*10-18).
- Primero se definen variables para equivalencias de unidades usando el 10^±n en el que n será la cantidad de ceros agregados a la multiplicación de 1 por cantidad de metros, positivo si las unidades son mayores a 1 y negativo si son menores a 0. 
Em = 1*10^18 m
Pm = 1*10^15 m
Tm = 1*10^12 m
Gm = 1*10^9 m
Mm = 1*10^6 m
km = 1*10^3 m
hm = 1*10^2 m
dam = 1*10^1 m
dm = 1*10^-1 m
cm = 1*10^-2 m
mm = 1*10^-3 m
µm = 1*10^-6 m
nm = 1*10^-9 m
pm = 1*10^-12 m
fm = 1*10^-15 m
am = 1*10^-18 m
Además unidad_1 será la cantidad de metros

Algoritmo
Pedir unidad_1 metros y guardarla
  Si unidad_1 > 0 mostrar “Convertir unidad_1 metros a: prefijo (Em, Pm, Tm…)“
  Guardar prefijo (Em, Pm, Tm…)
  Multiplicación unidad_1 por valor de prefijo y guardar operación
  Guardar multiplicación

Imprimir multiplicación.

Mostrar “¿Deseas ver cómo se calculó? Sí / No”
  Si Sí imprimir operación
  Si No Continuar
