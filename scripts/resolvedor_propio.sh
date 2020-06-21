#! /bin/bash

INPUTSATDIR=./SatInput
OUTSATDIR=./SatOutput
OUTSATTIMEDIR=./SatOutputTimes

# Eliminamos carpetas que hayan sido creadas
# previamente
rm -rf $INPUTSATDIR/* > /dev/null 2>&1
rm -rf $OUTSATDIR/* > /dev/null 2>&1
rm -rf $OUTSATTIMEDIR/* > /dev/null 2>&1
rmdir $INPUTSATDIR > /dev/null 2>&1
rmdir $OUTSATDIR > /dev/null 2>&1
rmdir $OUTSATTIMEDIR > /dev/null 2>&1

# Eliminamos soluciones previas
rm sol_*.txt > /dev/null 2>&1
rm 'Reporte de ejecucion Sat propio.txt' > /dev/null 2>&1

# Creamos directorios de salida
mkdir $INPUTSATDIR
mkdir $OUTSATDIR
mkdir $OUTSATTIMEDIR

# Ejecutamos el resolvedor propio
python3 ../main_sat_solver.py $1