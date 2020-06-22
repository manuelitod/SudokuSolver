# SudokuSolver

### Manual de uso:

Para hacer uso del Sudoku Solver es necesario ejecutar el script 'plot_maker.sh', ubicado en la carpeta 'scripts'. Dicho script recibe como único argumento la dirección relativa del archivo que contiene las instancias de sudoku a resolver.
    
Un ejemplo de ejecución podría ser:

```sh
plot_maker.sh ../files/InstanciaEjemplo.txt
```

### Funcionamiento de la ejecución:

A continuación se describirá el flujo de ejecución de una llamada al script descrito en el manual de uso.

Luego de ser ejecutado el script principal, éste procederá a ejecutar otros dos scripts. El primero, llamado 'resolvedor_propio', hace referencia al resolvedor de SAT creado por nosotros. Posteriormente se ejecutará el segundo, llamado 'resolvedor_zchaff', que hace referencia a ZCHAFF.

##### Ejecución de resolvedor_propio.sh

resolvedor_propio.sh creará los directorios necesarios para almacenar la información de la resolución del sudoku, mediante el uso del comando mkdir, previo a lo anterior eliminará los directorios posiblemente creados en ejecuciones anteriores, mediante el uso del comando rm. A continuación se ejecuta el archivo main_sat_solver.py, el cual recibe como primer argumento la dirección al archivo que contiene las instancias y como segundo argumento un entero que hace referencia al tiempo límite por instancia.

Una vez en el main del resolvedor propio se procede a crear un arreglo con cada una de las instancias encontardas en el archivo cuyo nombre fue pasado como argumento y se crea el archivo que finalmente contendrá la solución de todas las instancias. A continuación, y por cada una de las instancias de sudokus obtenidas del archivo, se procede a realizar lo siguiente:

Se crea una nueva instancia de la clase 'Translator', a la cual se le aplica el método 'translate', con lo cual se pasan a una instancia de la clase 'Sat' los literales y las clausulas generadas de forma automática por el constructor de 'Translator'. Una vez se tiene la instancia de Sat, con todo lo que necesita para resolver, se procede a ejecutar el método de dicha clase 'write_solution', el cual ejecuta el método 'solve' que resuelve la instancia y escribe el resultado y el tiempo de ejecución en un archivo contenido en el directorio 'SatInput'

Una vez tenemos las salidas del resolvedor de SAT escritas en los correspondientes archivos, procedemos a leer dichos archivos desde el main, usando el método 'get_sudoku_from_sat', que a su vez traduce dicha salida en un string cuyo contenido es la secuencia de números que solucionan la instancia inicial, en caso de tener solución. Por último se ejecuta el método 'write_sudoku_sol', el cual escribe dicha secuencia de números en el archivo de la solución final

##### Ejecución de resolvedor_zchaff.sh. 

La implementación del resolvedor de zchaff es análoga a la anterior.

##### Comparación de resultados

Una vez obtenido el archivo de solución del resolvedor propio y el de ZCHAFF, procedemos a ejecutar el archivo 'main_plt_maker.py', el cual lee ambos archivos e instancia a instancia obtiene el tiempo de ejecución y muestra su comparación en una gráfica.

### Diseño de la solución:

Los grandes pilares del solucionador de las instancias del sudoku se encuentran en solve (/classes/Sat.py),  build_preps (/classes/translator_txt_cnf.py).

##### Solve:

Este método lleva a cabo de forma recursiva la resolución del enunciado ingresado en cnf, ya que de esta forma el flujo de ejecución se lleva a cabo como un árbol, para el cual el padre es la ejecución de solve que llamó a la ejecución actual y los hijos son las ejecuciones de solve que serán llamados a continuación. De esta forma resulta sencillo y hasta intuitivo llevar a cabo el backtracking que es requerido para hallar la combinación de variables que satisfacen la expresión cnf.

En cada recursión se procede a llamar el método 'pure literal', el cual retorna como primer valor las clausulas que no poseen ningún literal puro y como segundo valor los literales puros. Luego se ejecuta 'unit_propagation', que retorna como primer valor las clausulas modificadas (habiendo quitado los literales unitarios negados en ellas) y como segundo valor los literales unitarios. Lo antes descrito nos sirve para filtrar la información ingresada a la siguiente ejecución del método solve y que, de esta forma, a medida que se avanza en la ejecución vaya disminuyendo la cantidad de operaciones a realizar.

Con el filtrado mencionado anteriormente se irán eliminando y simplificando cláusulas y añadiendo literales a la variable 'assignment', la cual contendrá en la hoja del árbol los literales que representan la solución. De encontrarse alguna incongruencia entre las clausulas y los valores asignados, los métodos pure_literal y unit_propagation lo reportarán al método solve, el cual detendrá su ejecución y retornará el flujo a su padre.

##### build_preps

Este es el método encargado de generar las cláusulas, haciendo uso de las dimensiones del sudoku que fueron obtenidas del archivo pasado como argumento al main. Para cada uno de los tipos de clausula se creeó un método distinto.

Clausulas de Casillas Asignadas: Estas clausulas se generan en el método 'gen_sudoku_cells_preps' y básicamente itera entre las casillas del sudoku y, de conseguir alguna cuyo valor sea distinto de cero, procede a añadir el literal como una clausula nueva.

Clausulas de Completitud: Creadas mediante el método 'gen_completeness_preps', 