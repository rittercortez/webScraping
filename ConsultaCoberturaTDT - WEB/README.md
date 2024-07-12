# 📺 Consulta de Cobertura TDT 📺

¡Bienvenido a mi repositorio de Git! Aquí encontrarás una herramienta diseñada para facilitar la búsqueda de información sobre la cobertura de la Televisión Digital Terrestre (TDT) en España. Este programa realiza un scraping de la página web oficial de la TDT del Ministerio de Asuntos Económicos y Transformación Digital de España, ahorrando tiempo y esfuerzo al proporcionar resultados directamente desde la aplicación.

## Descripción

La aplicación "Consulta de Cobertura TDT" permite a los usuarios ingresar un código postal y obtener rápidamente información sobre los centros emisores que dan cobertura TDT a la localidad correspondiente. Esta herramienta ahorra tiempo al evitar la necesidad de abrir un navegador, buscar la página web adecuada e ingresar manualmente el código postal.

Esta es una de las primeras versiones del programa, es una versión sencilla pero funcional.

## Funcionalidad

La aplicación realiza una búsqueda automatizada en la página web oficial de la TDT del Ministerio de Asuntos Económicos y Transformación Digital de España ([televisiondigital.mineco.gob.es](https://televisiondigital.mineco.gob.es/2DD-5G/Paginas/Que-tengo-que-hacer.aspx)). Utiliza técnicas de web scraping para extraer los datos de interés, presentándolos de manera clara y accesible en una interfaz gráfica de usuario (GUI) intuitiva.

### Características

- **Búsqueda Rápida**: Introduce un código postal y la aplicación buscará automáticamente la información de cobertura TDT correspondiente.
- **Selección de Opciones**: Si el código postal cubre múltiples localidades, puedes seleccionar la opción adecuada de un desplegable.
- **Resultados Detallados**: Muestra información detallada sobre los múltiplos digitales, centros emisores y canales de cada localidad.
- **Interfaz Gráfica Intuitiva**: Una GUI fácil de usar que simplifica el proceso de búsqueda y visualización de resultados.

## Cómo Funciona

1. **Entrada del Código Postal**: El usuario ingresa un código postal en el campo correspondiente y presiona "Buscar".
2. **Búsqueda Automática**: La aplicación envía una solicitud a la página web oficial de la TDT y realiza una búsqueda utilizando el código postal proporcionado.
3. **Selección de Localidad**: Si hay múltiples localidades para el código postal ingresado, la aplicación muestra un desplegable para que el usuario seleccione la opción adecuada.
4. **Visualización de Resultados**: Los resultados de la búsqueda se muestran en la GUI, incluyendo los múltiplos digitales, centros emisores y canales. También se muestra una imagen relacionada con la organización de los canales TDT.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal utilizado para desarrollar la aplicación.
- **Tkinter**: Biblioteca de Python para la creación de interfaces gráficas de usuario.
- **Selenium**: Herramienta de automatización utilizada para realizar el web scraping.
- **PIL (Pillow)**: Biblioteca de Python para manipulación de imágenes.
- **Threading**: Módulo de Python utilizado para manejar la concurrencia y mejorar la respuesta de la GUI.

![image](https://github.com/user-attachments/assets/7b63c97c-6e33-4d54-9ecc-4eb134d423ad)
![image](https://github.com/user-attachments/assets/f77036a8-3d7b-4835-a267-02e898580356)

