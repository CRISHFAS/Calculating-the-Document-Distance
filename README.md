# docdist1.py - Cálculo de Distancia de Documentos

Este proyecto de investigación calcula la "distancia" entre dos archivos de texto, medida como el ángulo entre sus vectores de frecuencia de palabras. Esta distancia se expresa en radianes.

## Funcionamiento del Algoritmo

### Proceso General
1. **Lectura de Archivos:** Se leen dos archivos de texto especificados.
2. **Extracción de Palabras:** El texto se convierte en una lista de palabras alfanuméricas en minúsculas.
3. **Conteo de Frecuencia:** Se cuenta la frecuencia de cada palabra.
4. **Ordenación de Palabras:** Las listas de palabras/frecuencia se ordenan alfabéticamente.
5. **Cálculo de Distancia:** Se calcula el ángulo entre los vectores de frecuencia de palabras utilizando el producto interno y la norma de los vectores.

### Fórmula Matemática
Si x = (x1, x2, ..., xn) es el primer vector (xi = frecuencia de la palabra i) y y = (y1, y2, ..., yn) es el segundo vector, entonces el ángulo entre ellos se define como:


\[ d(x,y) = \arccos\left(\frac{\text{producto\_interno}(x,y)}{\text{norma}(x) \cdot \text{norma}(y)}\right) \]


donde:


\[ \text{producto\_interno}(x,y) = x1 \cdot y1 + x2 \cdot y2 + ... + xn \cdot yn \]




\[ \text{norma}(x) = \sqrt{\text{producto\_interno}(x,x)} \]



## Uso

### Ejecución del Script

1. **Preparar los Archivos de Texto:**
   Crea dos archivos de texto (`file1.txt` y `file2.txt`) con el contenido que deseas comparar.

2. **Ejecutar el Script:**
   Abre una terminal y navega al directorio donde se encuentra `docdist1.py`. Luego ejecuta el siguiente comando:

   ```sh
   python docdist1.py file1.txt file2.txt
    ```

3. **Salida Esperada:** 
    El script imprimirá la cantidad de líneas, palabras y palabras distintas en cada archivo, así como la distancia en radianes entre los dos documentos.

    **salida de eljemplo**

    ```console
    Archivo file1.txt :
    3 líneas,
    147 palabras,
    95 palabras distintas
    Archivo file2.txt :
    3 líneas,
    125 palabras,
    65 palabras distintas
    La distancia entre los documentos es: 1.075040 (radianes)
    ```
## Casos de Uso
1. **Análisis de Similaridad de Sentimientos**
Comparar opiniones de usuarios en redes sociales, foros o encuestas para identificar tendencias y patrones en los sentimientos.

2. **Detección de Plagio**
Identificar posibles casos de copia al comparar trabajos académicos o artículos, midiendo la similitud en su contenido.

3. **Clasificación de Documentos**
Organizar documentos en categorías específicas basadas en su contenido, útil para sistemas de gestión de correos electrónicos o archivos.

4. **Recomendaciones de Lectura**
Sugerir libros, artículos o documentos similares a los que un usuario ha leído previamente.

5. **Motores de Búsqueda**
Mejorar la relevancia de los resultados en motores de búsqueda, comparando la consulta del usuario con documentos indexados.

6. **Resumen de Documentos**
Combinar el algoritmo con técnicas de resumen automático para proporcionar resúmenes que destaquen las partes más relevantes de un texto.

7. **Análisis de Discurso Político**
Comparar discursos políticos para identificar cambios en el contenido y el tono a lo largo del tiempo.

8. **Investigación Académica**
Comparar artículos de investigación para identificar trabajos relacionados y posibles colaboraciones entre investigadores.

9. **Agrupación de Noticias**
Agrupar noticias similares para proporcionar diferentes perspectivas sobre un mismo evento.

10. **Análisis de Publicaciones en Redes Sociales**
Analizar publicaciones para agruparlas por temas y detectar tendencias en tiempo real.

### Posibles Extensiones
- Implementación de Otras Métricas
Agregar soporte para otras métricas de similitud, como la distancia de Jaccard o el coeficiente de similitud de Coseno.

- Interfaz Gráfica de Usuario (GUI)
Desarrollar una interfaz gráfica para facilitar la comparación de documentos sin necesidad de usar la línea de comandos.

- Integración con Bases de Datos
Permitir la comparación de documentos almacenados en bases de datos para aplicaciones empresariales más grandes.

- Análisis de Idioma
Extender el soporte para analizar y comparar documentos en múltiples idiomas, no solo en español.

- Visualización de Resultados
Incorporar visualizaciones gráficas para mostrar la similitud entre documentos de manera más intuitiva.

- Automatización de Procesos
Automatizar la comparación de documentos en sistemas de gestión de contenido o plataformas de aprendizaje en línea.

