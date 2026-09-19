"""
Conversor de Unidades
======================
Programa que permite realizar conversiones entre:
    - Celsius <-> Fahrenheit
    - Kilómetros <-> Millas
    - Pesos Mexicanos (MXN) <-> Dólares (USD)

Autor: (Nombre del alumno)
"""

# Tasa de cambio fija (RF05 / RF06). Puede ajustarse según se requiera.
TASA_MXN_USD = 18.50  # 1 USD = 18.50 MXN


# ---------------------------------------------------------------------
# Funciones de conversión (lógica pura, reutilizable y fácil de probar)
# ---------------------------------------------------------------------

def celsius_a_fahrenheit(celsius: float) -> float:
    """RF01: Convierte grados Celsius a Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """RF02: Convierte grados Fahrenheit a Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)


def km_a_millas(km: float) -> float:
    """RF03: Convierte kilómetros a millas."""
    millas = km * 0.621371
    return round(millas, 2)


def millas_a_km(millas: float) -> float:
    """RF04: Convierte millas a kilómetros."""
    km = millas / 0.621371
    return round(km, 2)


def mxn_a_usd(mxn: float, tasa: float = TASA_MXN_USD) -> float:
    """RF05: Convierte Pesos Mexicanos a Dólares usando una tasa fija."""
    if tasa <= 0:
        raise ValueError("La tasa de cambio debe ser mayor que cero.")
    usd = mxn / tasa
    return round(usd, 2)


def usd_a_mxn(usd: float, tasa: float = TASA_MXN_USD) -> float:
    """RF06: Convierte Dólares a Pesos Mexicanos usando una tasa fija."""
    if tasa <= 0:
        raise ValueError("La tasa de cambio debe ser mayor que cero.")
    mxn = usd * tasa
    return round(mxn, 2)


# ---------------------------------------------------------------------
# Interfaz de consola (capa separada de la lógica, para poder probar
# las funciones de conversión de forma aislada con pytest)
# ---------------------------------------------------------------------

MENU = """
==== CONVERSOR DE UNIDADES ====
1. Celsius -> Fahrenheit
2. Fahrenheit -> Celsius
3. Kilómetros -> Millas
4. Millas -> Kilómetros
5. Pesos Mexicanos (MXN) -> Dólares (USD)
6. Dólares (USD) -> Pesos Mexicanos (MXN)
0. Salir
================================
"""


def solicitar_numero(mensaje: str) -> float:
    """RNF02: Solicita un valor numérico validando la entrada del usuario."""
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("⚠️  Entrada inválida. Por favor ingresa un valor numérico.")


def main():
    while True:
        print(MENU)
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        elif opcion == "1":
            valor = solicitar_numero("Ingresa el valor en Celsius: ")
            print(f"Resultado: {celsius_a_fahrenheit(valor)} °F")

        elif opcion == "2":
            valor = solicitar_numero("Ingresa el valor en Fahrenheit: ")
            print(f"Resultado: {fahrenheit_a_celsius(valor)} °C")

        elif opcion == "3":
            valor = solicitar_numero("Ingresa el valor en kilómetros: ")
            print(f"Resultado: {km_a_millas(valor)} millas")

        elif opcion == "4":
            valor = solicitar_numero("Ingresa el valor en millas: ")
            print(f"Resultado: {millas_a_km(valor)} km")

        elif opcion == "5":
            valor = solicitar_numero("Ingresa el valor en MXN: ")
            print(f"Resultado: {mxn_a_usd(valor)} USD")

        elif opcion == "6":
            valor = solicitar_numero("Ingresa el valor en USD: ")
            print(f"Resultado: {usd_a_mxn(valor)} MXN")

        else:
            print("⚠️  Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
