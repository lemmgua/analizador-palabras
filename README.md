## ¿Qué es?
Se trata de un programa desarrollado con el objetivo de analizar palabras y conseguir información acerca de palabras. Proporciona información básica desde la longitud o las vocales, hasta información sobre diptongos, triptongos, hiatos y recuento de letras
## ¿Cómo se utiliza?
Al iniciar, el programa te mostrará una interfaz con un título y una entrada del texto en el centro. A medida que se vaya escribiendo, la interfaz se actualizará para mostrar información en tiempo real de la palabra introducida.
## ¿Con qué herramientas está desarrollado?
Las herramientas utilizadas o *Tech Stack* está basado primariamente en Python, para el propio funcionamiento del programa, y HTML, CSS y JavaScript para la interfaz visual de este. Finalmente, ambas partes se juntan en un único programa utilizando una herramienta llamada [EEL](https://github.com/python-eel/Eel), que crea servidores web locales, y permite vincular funciones de Python al JavaScript para que estas puedan ser llamadas desde el *frontend*.
## ¿Cómo funciona?
Debajo de la superficie, el programa utiliza las expresiones regulares del lenguaje de programación Python para detectar sílabas, siguiendo patrones comunes. Cuando se encuentra una coincidencia, se añade como sílaba, y se elimina esa parte de la palabra, y se vuelve a repetir, hasta que la palabra no tiene más caracteres.