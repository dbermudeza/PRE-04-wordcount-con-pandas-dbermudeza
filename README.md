# Contador de Palabras con Pandas

## ¿Qué es este repositorio?

Este proyecto implementa un **contador de palabras** que procesa archivos de texto y calcula la frecuencia de aparición de cada palabra. Es una herramienta útil para análisis de texto que utiliza la librería Pandas de Python para realizar el procesamiento de datos de forma eficiente.

## ¿Qué hace?

El programa realiza las siguientes tareas:

1. **Lee archivos de texto**: Procesa todos los archivos `.txt` ubicados en un directorio de entrada
2. **Limpia el texto**: Convierte el contenido a minúsculas y elimina puntuación
3. **Divide en palabras**: Segmenta el texto limpio en palabras individuales
4. **Cuenta frecuencias**: Utiliza Pandas para contar cuántas veces aparece cada palabra
5. **Genera resultados**: Guarda un archivo con las palabras y sus frecuencias ordenadas alfabéticamente
6. **Crea indicador de éxito**: Genera un archivo `_SUCCESS` para confirmar que el procesamiento completó exitosamente

## ¿Cómo funciona?

El flujo de procesamiento es el siguiente:

1. El programa toma dos parámetros: 
   - **Directorio de entrada**: Carpeta que contiene los archivos de texto a procesar
   - **Directorio de salida**: Carpeta donde se guardarán los resultados

2. **Procesamiento de datos**:
   - Lee cada archivo `.txt` del directorio de entrada
   - Normaliza el texto (minúsculas, sin puntuación)
   - Extrae todas las palabras y las agrupa en una lista
   - Utiliza Pandas `Series.value_counts()` para contar frecuencias

3. **Almacenamiento de resultados**:
   - Crea un DataFrame con dos columnas: `word` (palabra) y `count` (frecuencia)
   - Guarda el resultado en formato TSV (tabulaciones) en el archivo `part-00000`
   - Genera un archivo `_SUCCESS` vacío como indicador de finalización exitosa

## Estructura del proyecto

```
files/
  ├── input/        # Directorio con archivos de texto a procesar
  └── output/       # Directorio con resultados del procesamiento
homework/
  └── word_count.py # Código principal del contador de palabras
tests/
  └── test_homework.py # Pruebas unitarias
```

# Configuración en MacOS y Linux

## Instalación del ambiante de desarrollo

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
source setup.sh
```

## Calificación del laboratorio

Ejecute los siguientes comandos en el terminal:

```bash
./tests/run.sh
```

# Configuración en Windows

## Instalación del ambiante de desarrollo

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv
.venv\Scripts\activate
setup
```

## Calificación del laboratorio

Ejecute los siguientes comandos en el terminal:

```bash
tests\run
```
