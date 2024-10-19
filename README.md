
# Simulación de Uniswap Pool en Python

Este repositorio contiene una simulación sencilla de un **pool de liquidez** de Uniswap, implementada en Python. La simulación permite intercambiar **ETH** por **tokens** utilizando la ecuación de constante de producto de Uniswap (Automated Market Maker - AMM). El código incluye una explicación detallada de cada paso del cálculo, desde las condiciones iniciales del pool hasta el cálculo del fee y los balances ajustados tras el intercambio.

## Descripción

Uniswap es una plataforma de intercambio descentralizado (DEX) que utiliza un creador de mercado automatizado (AMM). En esta simulación, implementamos la ecuación básica de producto constante:

```
k = x * y
```

Donde:
- **x** es la cantidad de **ETH** en el pool.
- **y** es la cantidad de **TOKEN** en el pool.
- **k** es una constante que se mantiene igual después de cada intercambio, asegurando el equilibrio entre ETH y TOKEN en el pool.

Este proyecto permite realizar intercambios entre ETH y TOKEN, calculando cuántos tokens recibirás por una cantidad específica de ETH ingresada, aplicando un **fee** del 0.01% típico de Uniswap. Además, el script muestra el ajuste de los balances de ETH y TOKEN en el pool después del intercambio, y explica cada paso del cálculo con lujo de detalle.

---

## Ejemplo detallado de intercambio

A continuación, se presenta un ejemplo de cómo se realiza el cálculo cuando se intercambian 0.1 ETH por tokens:

### 1. Condiciones iniciales del pool:
- **ETH en el pool**: `x = 1 ETH`
- **TOKEN en el pool**: `y = 100 TOKEN`
- **Constante de producto**: `k = x * y = 1 * 100 = 100`

Esta ecuación debe mantenerse constante después del intercambio.

### 2. Cantidad de ETH a intercambiar:
Vas a intercambiar **0.1 ETH**, pero Uniswap aplica una comisión (fee) por cada intercambio. En este caso, el **fee tier** es del 0.01%, lo que significa que el fee es:

```
Fee = 0.1 * 0.0001 = 0.00001 ETH
```

### 3. ETH efectivo:
La cantidad de **ETH efectiva** que realmente se intercambia (después de descontar el fee) es:

```
ETH efectiva = 0.1 - 0.00001 = 0.09999 ETH
```

### 4. Nuevo balance de ETH en el pool:
El nuevo balance de **ETH** en el pool será:

```
x_nuevo = 1 + 0.09999 = 1.09999 ETH
```

### 5. Nuevo balance de TOKEN en el pool:
Para calcular el nuevo balance de tokens, utilizamos la constante de producto:

```
y_nuevo = k / x_nuevo = 100 / 1.09999 ≈ 90.909917 TOKEN
```

### 6. Tokens recibidos:
La cantidad de **tokens recibidos** es la diferencia entre el balance inicial y el nuevo balance de tokens en el pool:

```
Tokens recibidos = 100 - 90.909917 = 9.090083 TOKEN
```

### 7. Resumen final del intercambio:
- **ETH enviado**: 0.1 ETH
- **Fee cobrado**: 0.00001 ETH
- **ETH efectivo**: 0.09999 ETH
- **Tokens recibidos**: 9.090083 TOKEN

### 8. Balance del pool después del intercambio:
- **Nuevo balance de ETH**: `1.09999 ETH`
- **Nuevo balance de TOKEN**: `90.909917 TOKEN`

---

## Requisitos

- Python 3.x

## Instrucciones

1. Clona el repositorio:
   ```bash
   git clone https://github.com/fsaldivar/poolUniswap.git
   ```

2. Ejecuta el script en tu entorno local:
   ```bash
   python3 pool.py
   ```

---

## Explicación del Código

### Funciones Clave:

1. **swap_eth_for_token**:
   Esta función toma como entrada una cantidad de **ETH** a intercambiar y realiza los siguientes pasos:
   - Aplica el **fee** correspondiente (0.01% del ETH enviado).
   - Calcula la cantidad de **ETH efectiva** que se añadirá al pool.
   - Actualiza el balance de **ETH** en el pool.
   - Utiliza la **constante de producto** para calcular el nuevo balance de **TOKEN**.
   - Calcula la cantidad de **tokens recibidos**.
   - Imprime todos los pasos y detalles del cálculo.

2. **Ecuación de producto constante**:
   La constante de producto `k = x * y` asegura que el valor total en el pool (ETH y tokens) se mantenga equilibrado en un 50% para cada activo, aunque las cantidades exactas varíen.

---

## Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](LICENSE).
