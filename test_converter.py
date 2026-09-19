"""
Pruebas unitarias para el módulo converter.py
Ejecutar con:  pytest -v
Ejecutar solo las marcadas como unit:  pytest -v -m unit
"""

import pytest
from converter import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    km_a_millas,
    millas_a_km,
    mxn_a_usd,
    usd_a_mxn,
)


# ---------------------------------------------------------------------
# TC01 - RF01: Conversión de Celsius a Fahrenheit
# ---------------------------------------------------------------------
@pytest.mark.unit
@pytest.mark.parametrize(
    "celsius, esperado",
    [
        (0, 32.0),      # punto de congelación
        (100, 212.0),   # punto de ebullición
        (-40, -40.0),   # punto donde ambas escalas coinciden
        (37, 98.6),     # temperatura corporal aproximada
    ],
)
def test_celsius_a_fahrenheit(celsius, esperado):
    """TC01: Verifica que la conversión Celsius -> Fahrenheit sea correcta."""
    resultado = celsius_a_fahrenheit(celsius)
    assert resultado == esperado


# ---------------------------------------------------------------------
# TC02 - RF02: Conversión de Fahrenheit a Celsius
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_fahrenheit_a_celsius():
    """TC02: Verifica que la conversión Fahrenheit -> Celsius sea correcta."""
    assert fahrenheit_a_celsius(32) == 0.0
    assert fahrenheit_a_celsius(212) == 100.0


# ---------------------------------------------------------------------
# TC03 - RF03: Conversión de Kilómetros a Millas
# ---------------------------------------------------------------------
@pytest.mark.unit
@pytest.mark.parametrize(
    "km, esperado",
    [
        (0, 0.0),
        (1, 0.62),
        (10, 6.21),
        (42.195, 26.22),  # distancia de un maratón
    ],
)
def test_km_a_millas(km, esperado):
    """TC03: Verifica que la conversión km -> millas sea correcta."""
    resultado = km_a_millas(km)
    assert resultado == esperado


# ---------------------------------------------------------------------
# TC04 - RF04: Conversión de Millas a Kilómetros
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_millas_a_km():
    """TC04: Verifica que la conversión millas -> km sea correcta."""
    assert millas_a_km(1) == pytest.approx(1.61, abs=0.01)


# ---------------------------------------------------------------------
# TC05 - RF05: Conversión de Pesos Mexicanos a Dólares
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_mxn_a_usd():
    """TC05: Verifica que la conversión MXN -> USD use correctamente la tasa fija."""
    resultado = mxn_a_usd(185, tasa=18.5)
    assert resultado == 10.0


# ---------------------------------------------------------------------
# TC06 - RF06: Conversión de Dólares a Pesos Mexicanos
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_usd_a_mxn():
    """TC06: Verifica que la conversión USD -> MXN use correctamente la tasa fija."""
    resultado = usd_a_mxn(10, tasa=18.5)
    assert resultado == 185.0


# ---------------------------------------------------------------------
# TC07 - RNF: Validación de tasa de cambio inválida (manejo de errores)
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_tasa_invalida_lanza_error():
    """TC07: Verifica que una tasa de cambio <= 0 lance un ValueError."""
    with pytest.raises(ValueError):
        mxn_a_usd(100, tasa=0)


# ---------------------------------------------------------------------
# TC08 - RNF01: Precisión de al menos dos decimales en el resultado
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_precision_dos_decimales():
    """TC08: Verifica que los resultados se redondeen a 2 decimales."""
    resultado = celsius_a_fahrenheit(36.6)
    # El resultado no debe tener más de 2 decimales
    assert round(resultado, 2) == resultado
