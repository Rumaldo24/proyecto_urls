[Parte 3-Desarrollo de un Algoritmo Eficiente.txt](https://github.com/user-attachments/files/17249501/Parte.3-Desarrollo.de.un.Algoritmo.Eficiente.txt)Requerimientos Técnicos

* Lenguaje de programación:

El programa está escrito en Python.
Python es una excelente opción para manejar grandes volúmenes de datos gracias a sus bibliotecas integradas para procesamiento de archivos y manejo eficiente de memoria.

* Código limpio y comentado:

El código está estructurado de manera sencilla y clara, con comentarios explicativos en cada sección clave.
Cada función tiene un propósito bien definido, y se utilizan nombres de variables descriptivos.

* Instrucciones sobre cómo ejecutar el programa:

* Instrucciones de ejecución:
  
Paso 1: Requerimientos previos

Asegúrate de tener Python 3.x instalado. Si no lo tienes, puedes descargarlo desde python.org.

Paso 2: Clona el repositorio o descarga el código

Coloca el archivo Python en una carpeta local.

Paso 3: Crear un archivo con las URLs

Crea un archivo de texto, por ejemplo urls.txt, que contenga las URLs que deseas procesar (cada URL en una línea).
Paso 4: Ejecutar el script

Abre una terminal y navega hasta la carpeta donde se encuentra el archivo Python.

Si tu archivo se llama procesar_urls.py y el archivo de URLs es urls.txt, puedes ejecutar el programa así:

  (python procesar_urls.py)

Si usas el código con paralelización para archivos más grandes, la ejecución sería similar, pero asegúrate de que tienes instaladas las dependencias necesarias.

* Dependencias:
Para la versión básica del programa, no hay dependencias adicionales. Solo necesitas Python instalado.[UploadingDocumentación del Algoritmo

Funcionamiento del Algoritmo:

Leer el archivo línea por línea:

El programa abre el archivo de texto que contiene las URLs y lo lee línea por línea para evitar cargar todo el archivo en memoria a la vez.
Cada línea del archivo es procesada y limpiada (se eliminan espacios en blanco y saltos de línea).

Filtros aplicados a las URLs:

Por cada URL leída, el programa verifica dos condiciones:
La URL debe contener la palabra "shop".
La URL debe terminar con la extensión ".html".
Si ambas condiciones se cumplen, la URL es agregada a un conjunto (set), lo que asegura que no haya duplicados.

Optimización con conjuntos:

Usamos un set para almacenar las URLs válidas porque los conjuntos en Python son muy eficientes para buscar, insertar y eliminar duplicados en tiempo constante O(1).

Devolución del resultado:

Una vez procesado todo el archivo, el programa devuelve el número total de URLs que cumplen con los criterios, junto con la lista de esas URLs.

Técnicas utilizadas para optimizar el rendimiento y el uso de memoria:
Lectura eficiente con generadores:

El programa usa un generador para iterar sobre las líneas del archivo, lo que permite procesar cada línea individualmente sin cargar el archivo completo en memoria.
Esto es particularmente útil cuando se trabaja con archivos grandes que podrían ocupar mucha memoria.

Desempeño esperado:

El algoritmo en su versión básica es capaz de procesar archivos grandes de manera eficiente, pero para archivos de decenas de millones de líneas, el uso de paralelización puede ser necesario para reducir el tiempo de ejecución.

En pruebas con archivos grandes (por ejemplo, varios millones de líneas), el algoritmo debería procesar las URLs en segundos o minutos, dependiendo del tamaño del archivo y del hardware en el que se ejecute.


[Parte 3-Desarrollo de un Algoritmo Eficiente.txt](https://github.com/user-attachments/files/17249509/Parte.3-Desarrollo.de.un.Algoritmo.Eficiente.txt)
