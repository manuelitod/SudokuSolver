# SudokuSolver

## Resolver sudokus con ambos Sat solvers y una gráfica de comparación

Para realizar la ejecución de ambos algoritmos (Resolvedor Sat propio y Zchaff) sobre una entrada de Sudokus es necesario ejecutar el script 'plot_maker.sh', ubicado en la carpeta 'scripts'. Dicho script recibe como único argumento la dirección relativa del archivo que contiene las instancias de sudoku a resolver.
    
Un ejemplo de ejecución podría ser:

```
sh plot_maker.sh ../files/InstanciaEjemplo.txt
```

## Resolver sudokus utilizando solo resolvedor Sat propio

Se debe realizar la ejecución del script 'resolvedor_propio.sh', ubicado en la carpeta 'scripts' tomando como argumento la dirección relativa del archivo que contiene las instancias de sudoku a resolver.

Un ejemplo de ejecución podría ser:

```
sh resolvedor_propio.sh ../files/InstanciaEjemplo.txt
```

## Resolver sudokus utilizando solo Sat Zchaff

Se debe realizar la ejecución del script 'resolvedor_zchaff', ubicado en la carpeta 'scripts' tomando como argumento la dirección relativa del archivo que contiene las instancias de sudoku a resolver.

Un ejemplo de ejecución podría ser:

```
sh resolvedor_zchaff.sh ../files/InstanciaEjemplo.txt
```

## Funcionamiento de la ejecución:

A continuación se describirá el flujo de ejecución de una llamada al script descrito en el manual de uso.

Luego de ser ejecutado el script principal, éste procederá a ejecutar otros dos scripts. El primero, llamado 'resolvedor_propio', hace referencia al resolvedor de SAT creado por nosotros. Posteriormente se ejecutará el segundo, llamado 'resolvedor_zchaff', que hace referencia a ZCHAFF.

## Directorios creados

Los scripts 'resolvedor_propio' y 'resolvedor_zchaff' crean y utilizan los siguientes directorios
dentro de la carpeta scripts:

* Reports
* SatInput
* SatOutput
* SatOutputTimes
* SatSols

Por cada archivo de instancias de sudoku se crearán ficheros dentro de estos directorios.

Tenga en cuenta que si se realizan multiples ejecuciones con el mismo archivo de entrada los ficheros de salida solo contendran información de la última ejecución realizada.

### Directorio Reports

En este directorio se crearan los ficheros con los reportes de ejecución para cada archivo
de entrada de sudokus.

El reporte tendrá la siguiente estructura por cada resolución de instancia de Sudoku presentes en el archivo de entrada.

```
Instancia número X
Entrada: Sudoku de entrada en formato legible.
Salida: Sudoku de salida en formato legible.
En caso de no ser solucionado en el tiempo T, se utilizará una descripción pertinente. 
(Se agoto el tiempo de ejecución)
Tiempo de ejecución: El tiempo de ejecución en ms para la solución de la instancia.
```

Además se guaradará un gráfico comparativo entre el resolvedor propio y el algoritmo zchaff con el nombre sol_sat_<Nombre_archivo_instancias_sudoku>_grafica_tiempo.png

### Directorio SatOutputTimes

En este directorio se crearan los archivos con el tiempo de ejecución por instancia que tomo solucionar el problema utilizando el resolvedor propio o el zchaff.

### Directorio SatSols

En este directorio se crearan los archivos con la solución a las instancias de sudoku en formato de sudoku.

En caso de que una instancia no haya podido ser solucionada se opto por colocar 'Instance Timeout' o 'Instance Unsatisfacible' para ser consistentes con el output del algoritmo Zchaff en estos casos.

#### Archivos creados

En los directorios mencionados anteriormente la convención para la creación de ficheros es la siguiente:

* Para el caso del resolvedor SAT propio los archivos serán llamados de la siguiente manera: sol_sat_<Nombre_archivo_instancias_sudoku>.txt

* Para el caso del resolvedor SAT zfhaff los archivos serán llamados de la siguiente manera: sol_sat_zchaff_<Nombre_archivo_instancias_sudoku>.txt

### Directorio SatInput

En este directorio se crearan los archivos de entrada con la representación CNF para cada instancia de sudoku.

* Los archivos serán nombrados la siguiente manera: sat_<numero_instancia_sudoku>_<Nombre_archivo_instancias_sudoku>.txt

### Directorio SatOutput

En este directorio se crearan los archivos de salida con la solución en formato CNF para cada instancia de sudoku.

* Para el caso del resolvedor SAT propio los archivos serán llamados de la siguiente manera: sol_sat_<numero_instancia_sudoku>_<Nombre_archivo_instancias_sudoku>.txt

* Para el caso del resolvedor SAT zfhaff los archivos serán llamados de la siguiente manera: sol_sat_zchaff_<numero_instancia_sudoku>_<Nombre_archivo_instancias_sudoku>.txt

## Ejecución de resolvedor_propio.sh

resolvedor_propio.sh creará los directorios necesarios para almacenar la información de la resolución del sudoku, mediante el uso del comando mkdir, previo a lo anterior eliminará todos los ficheros asociados al archivo instancias de sudoku, mediante el uso del comando rm. A continuación se ejecuta el archivo main_sat_solver.py, el cual recibe como primer argumento la dirección al archivo que contiene las instancias y como segundo argumento un entero que hace referencia al tiempo límite por instancia.

Una vez en el main del resolvedor propio se procede a crear un arreglo con cada una de las instancias encontardas en el archivo cuyo nombre fue pasado como argumento y se crea el archivo que finalmente contendrá la solución de todas las instancias. A continuación, y por cada una de las instancias de sudokus obtenidas del archivo, se procede a realizar lo siguiente:

Se crea una nueva instancia de la clase 'Translator', a la cual se le aplica el método 'translate', con lo cual se pasan a una instancia de la clase 'Sat' los literales y las clausulas generadas de forma automática por el constructor de 'Translator'. Una vez se tiene la instancia de Sat, con todo lo que necesita para resolver, se procede a ejecutar el método de dicha clase 'write_solution', el cual ejecuta el método 'solve' que resuelve la instancia y escribe el resultado y el tiempo de ejecución en un archivo contenido en el directorio 'SatInput'

Una vez tenemos las salidas del resolvedor de SAT escritas en los correspondientes archivos, procedemos a leer dichos archivos desde el main, usando el método 'get_sudoku_from_sat', que a su vez traduce dicha salida en un string cuyo contenido es la secuencia de números que solucionan la instancia inicial, en caso de tener solución. Por último se ejecuta el método 'write_sudoku_sol', el cual escribe dicha secuencia de números en el archivo de la solución final

## Ejecución de resolvedor_zchaff.sh. 

La implementación del resolvedor de zchaff es análoga a la anterior.

## Comparación de resultados

Una vez obtenido el archivo de solución del resolvedor propio y el de ZCHAFF, procedemos a ejecutar el archivo 'main_plt_maker.py', el cual lee ambos archivos e instancia a instancia obtiene el tiempo de ejecución y muestra su comparación en una gráfica.

## Diseño de la solución:

### Clase SAT

La clase SAT ubicada en el archivo (/classes/Sat.py) contiene la implementación de un algoritmo DPLL con asignación de literales aletorios. Su complejidad en tiempo es O(m*2^n) siendo n el número de literales en la clausula y m la cantidad de clausulas.

#### Método Solve:

Este método lleva a cabo de forma recursiva la resolución del enunciado ingresado en cnf, ya que de esta forma el flujo de ejecución se lleva a cabo como un árbol, para el cual el padre es la ejecución de solve que llamó a la ejecución actual y los hijos son las ejecuciones de solve que serán llamados a continuación. De esta forma resulta sencillo y hasta intuitivo llevar a cabo el backtracking que es requerido para hallar la combinación de variables que satisfacen la expresión cnf.

En cada recursión se procede a llamar el método 'pure literal', el cual retorna como primer valor las clausulas que no poseen ningún literal puro y como segundo valor los literales puros. Luego se ejecuta 'unit_propagation', que retorna como primer valor las clausulas modificadas (habiendo quitado los literales unitarios negados en ellas) y como segundo valor los literales unitarios. Lo antes descrito nos sirve para filtrar la información ingresada a la siguiente ejecución del método solve y que, de esta forma, a medida que se avanza en la ejecución vaya disminuyendo la cantidad de operaciones a realizar.

Con el filtrado mencionado anteriormente se irán eliminando y simplificando cláusulas y añadiendo literales a la variable 'assignment', la cual contendrá en la hoja del árbol los literales que representan la solución. De encontrarse alguna incongruencia entre las clausulas y los valores asignados, los métodos pure_literal y unit_propagation lo reportarán al método solve, el cual detendrá su ejecución y retornará el flujo a su padre.

### Clase Translator

La clase Translator ubicada en el archivo (/classes/translator_txt_cnf.py) contiene la implementación de métodos que permiten generar las clausulas necesarias para modelar un Sudoku a un problema Sat.

### Método generate_literals

Este método nos genera la representación para cada literal de las clausulas del problema SAT. Se utilizó una clase 'Literal' para almacenar los valores correspondientes a la construcción del mismo, tales como: Fila, Columna, Valor dentro del Sudoku y valor del literal.

### Método gen_sudoku_cells_preps

En este método generá un hash con los literales presentes en la instancia sudoku a resolver. Además genera las clausulas unitarias [literal].

### Método gen_completeness_preps

Este método genera todas las clausulas de completitud del sudoku. Para ello se toma el arreglo de literales y se realiza la sub-división en arreglos de tamaño n^2.

Se realizó la optimización de excluir arreglos que contengan literales presentes en el hash creado en el método anterior.

### Método gen_not_prep

Dado un arreglo de literales este método genera clausulas de unicidad (-l1,-l2) para cada uno de los literales presentes en el arreglo.

Se realizó la optimización de agregar estas clausulas de unicidad con el valor de verdad de los literales presentes en el sudoku.

Para una entrada de literales: [1,2,3] este método retornará: [-1,-2],[-1,-3],[-2,-3] asumiendo que ninguno de estos literales esta presente en el sudoku.

### Método gen_uniqueness_preps

Este metodo genera todas las clausulas de unicidad del sudoku. Para ello por cada clausula de completitud se utiliza el método auxiliar 'gen_not_prep' para obtener las clasusulas de unicidad.

### Método gen_validity_preps

Este metodo generara todas las clausulas de validez del sudoku. Por cada fila, columna y sección del sudoku se obtienen los literales de cada uno de ellos y se utiliza el método gen_not_prep para generar las clausulas de validez.
