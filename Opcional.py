"""
Sesion 1
1. Definición: Define la notación O grande, Ω grande y Θ grande. ¿Cuál es la diferencia entre
ellas?

la notación O grande (O) se utiliza para describir un límite superior del tiempo de ejecución o el espacio utilizado por un algoritmo en función del tamaño de la entrada. Indica el peor caso posible.
la notación Ω grande (Ω) se utiliza para describir un límite inferior del tiempo de ejecución o el espacio utilizado por un algoritmo. Indica el mejor caso posible.
la notación Θ grande (Θ) se utiliza para describir un límite ajustado del tiempo

la diferencia entre ellas radica en que O grande proporciona un límite superior, Ω grande proporciona un límite inferior y Θ grande proporciona un límite ajustado, indicando que el algoritmo tiene un comportamiento asintótico tanto superior como inferior.


2. Funciones de Crecimiento: Ordena las siguientes funciones de crecimiento de menor a mayor:
n², log n, 2^n, n, 1. Justifica tu respuesta. 

el orden de las funciones de crecimiento de menor a mayor es : 1, log n, n , n^2, 2^n

se debe a que 1 es una constante y no crece con n, log n crece más lentamente que n, n crece linealmente, n² crece cuadráticamente y 2^n crece exponencialmente, siendo la función de crecimiento más rápida entre las mencionadas.



3. Importancia: ¿Por qué es importante la notación asintótica en el análisis de algoritmos?
Menciona al menos 3 razones.

la notación asintótica es importante en el análisis de algoritmos porque:

primero nos permite comparar la eficiencia de diferentes algoritmos 
segundo nos ayuda basicamente a predecir el rendiiento de un algoritmo a medida que la entrada de este mismo crece
tercero nos ayuda a comunicar de manera mas clara la complejidad de un algoritmo 


-----------------------------------------------------------------------------------------------------------------------------
Sesion 2
Analisis de algoritmo

complejidad del peor caso:

algoritmo1: O(n^2) ya que tiene dos bucles anidados que recorren n elementos cada uno.
algoritmo2: O(log n) ya que el valor de i se duplica en cada iteración, lo que resulta en un crecimiento logarítmico en relación con n.


comparacion: algoritmo2 es más eficiente que algoritmo1 para entradas grandes, ya que O(log n) crece mucho más lentamente que O(n^2).
        
mejor caso:si es posible que un algoritmo tenga una complejidad diferente en el mejor caso y en el peor caso. un ejemplo 
seria un algoritmo de búsqueda lineal tiene una complejidad de O(1) en el mejor caso (cuando el elemento buscado está en la primera posición) y
O(n) en el peor caso (cuando el elemento no está presente o está al final de la lista).

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sesion 3

¿cual es la relacion asintotica entre las funciones log_2 n y log_8 n? 
R: C

¿cual es la relacion asintotica entre 8^n y 4^n?
R: B

¿cual es la relacion asintotica entre n^3 log_2 n y 3n log_8 n?
a. A 


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 quiero qu responda de forma super concisa 
Sesion 4

Fundamentos

¿Por qué es importante analizar la complejidad asintótica de un algoritmo?
R: es importante para entender la eficiencia y escalabilidad del algoritmo.

¿Qué significa que un algoritmo tenga una complejidad de O(log n)?
R: esto significa que el tiempo de ejecucion del algoritmo crece logaritmicamenere con el tamañoi de la enrada 

¿Cómo se relaciona la notación asintótica con el tamaño de la entrada?
R: la notacion lo que hace es describir como cambia el rendimiento del algoritmo 
a medida que aumenta el tamaño de la entrada.

Funciones

¿Cuáles son las funciones de crecimiento más comunes en el análisis de algoritmos?
R: las funciones mas comunes son O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n).

¿Cómo se compara el crecimiento de una función lineal con una función logarítmica?
R: una función logarítmica crece más lentamente que una función lineal a medida que n aumenta.

¿Qué implica que una función tenga un crecimiento exponencial?
R: es que el tiempo de ejecución del algoritmo aumenta muy rápidamente con el tamaño de la entrada.

Algoritmos

¿Cómo se analiza la complejidad de un algoritmo recursivo?
R: se utiliza la relación de recurrencia para expresar la complejidad y luego se resuelve usando métodos como el teorema maestro o la expansión iterativa.


¿Qué es el teorema maestro y para qué se utiliza?
R: el teorema maestro es para resolver relaciones de recurrencia comunes en algoritmos recursivos, ayudando a determinar su complejidad temporal.


¿Cómo se puede determinar la complejidad promedio de un algoritmo?
R: se analiza el comportamiento del algoritmo sobre todas las posibles entradas y se calcula el tiempo de ejecución esperado.


¿Qué factores influyen en la complejidad de un algoritmo?
R: factores como la estructura de datos utilizada, la naturaleza del problema, la implementación del algoritmo y el tamaño de la entrada.

"""