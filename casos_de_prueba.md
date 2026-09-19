# Casos de Prueba — Conversor de Unidades

| ID   | Descripción de la prueba                              | Requerimiento | Entradas                | Resultado esperado | Resultado obtenido |
|------|--------------------------------------------------------|---------------|--------------------------|---------------------|----------------------|
| TC01 | Convertir Celsius a Fahrenheit con varios valores       | RF01          | 0, 100, -40, 37 °C       | 32.0, 212.0, -40.0, 98.6 °F | ✅ Aprobado (PASSED) |
| TC02 | Convertir Fahrenheit a Celsius                          | RF02          | 32 °F, 212 °F            | 0.0 °C, 100.0 °C    | ✅ Aprobado (PASSED) |
| TC03 | Convertir kilómetros a millas con varios valores        | RF03          | 0, 1, 10, 42.195 km      | 0.0, 0.62, 6.21, 26.22 millas | ✅ Aprobado (PASSED) |
| TC04 | Convertir millas a kilómetros                           | RF04          | 1 milla                  | ≈1.61 km            | ✅ Aprobado (PASSED) |
| TC05 | Convertir MXN a USD usando la tasa fija (18.5)          | RF05          | 185 MXN, tasa=18.5       | 10.0 USD            | ✅ Aprobado (PASSED) |
| TC06 | Convertir USD a MXN usando la tasa fija (18.5)          | RF06          | 10 USD, tasa=18.5        | 185.0 MXN           | ✅ Aprobado (PASSED) |
| TC07 | Validar manejo de error con tasa de cambio inválida     | RNF02         | 100 MXN, tasa=0          | Lanza ValueError    | ✅ Aprobado (PASSED) |
| TC08 | Verificar precisión de dos decimales en el resultado    | RNF01         | 36.6 °C                  | Resultado con máx. 2 decimales | ✅ Aprobado (PASSED) |

**Evidencia de ejecución:** ver archivo `resultado_pytest.txt`, generado al correr:

```
pytest -v -m unit
```

Resultado: **14 passed in 0.02s** (algunos casos incluyen varias combinaciones mediante `@pytest.mark.parametrize`, por eso hay 14 ejecuciones para los 8 casos de prueba documentados).
