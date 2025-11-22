# Conversor de Unidades Métrico/Imperial

Una aplicación de consola desarrollada en Python para convertir entre diferentes unidades del sistema métrico e imperial.

## Descripción

Este conversor permite realizar conversiones rápidas y precisas entre las unidades más comunes de:

- **Masa**: Kilogramos ↔ Libras
- **Longitud**: Metros ↔ Pies/Pulgadas, Kilómetros ↔ Millas
- **Temperatura**: Celsius ↔ Fahrenheit
- **Volumen**: Litros ↔ Galones US, Mililitros ↔ Onzas Fluidas

## Estructura del Proyecto
```
Conversor_unidades/
│
├── conversor.py          # Archivo principal para ejecutar la aplicación
├── masa.py              # Módulo de conversiones de masa
├── longitud.py          # Módulo de conversiones de longitud
├── temperatura.py       # Módulo de conversiones de temperatura
└── volumen.py           # Módulo de conversiones de volumen
```

## Requisitos

- Python 3.x

## Instalación y Uso

1. Clona o descarga este repositorio
2. Navega hasta el directorio del proyecto
3. Ejecuta el programa principal:
```bash
python conversor.py
```

## Funcionalidades

### Conversiones de Masa
- Kilogramos a Libras
- Libras a Kilogramos

### Conversiones de Longitud
- Metros a Pies y Pulgadas (formato ft'inch")
- Pies y Pulgadas a Metros
- Kilómetros a Millas
- Millas a Kilómetros

### Conversiones de Temperatura
- Celsius a Fahrenheit
- Fahrenheit a Celsius

### Conversiones de Volumen
- Litros a Galones US
- Galones US a Litros
- Mililitros a Onzas Fluidas
- Onzas Fluidas a Mililitros

## Navegación

La aplicación utiliza un sistema de menús intuitivo:

1. Selecciona la categoría de conversión (Masa, Longitud, Temperatura o Volumen)
2. Elige el tipo de conversión específico
3. Ingresa el valor a convertir
4. El resultado se mostrará en pantalla
5. Presiona Enter para continuar y realizar otra conversión

## Arquitectura

El proyecto está organizado en módulos separados para mantener el código limpio y reutilizable:

- Cada módulo (`masa.py`, `longitud.py`, `temperatura.py`, `volumen.py`) contiene una clase con métodos específicos para las conversiones de su categoría
- `conversor.py` importa y orquesta todos los módulos para proporcionar la interfaz de usuario completa

## Autor

Cristian Aranda @carandab

