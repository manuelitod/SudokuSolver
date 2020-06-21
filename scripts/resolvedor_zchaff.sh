#! /bin/bash

INPUTSATDIR=./SatInput
OUTSATDIR=./SatOutput
OUTSATTIMEDIR=./SatOutputTimes

# Eliminamos carpetas que hayan sido creadas
# previamente
rm -rf $INPUTSATDIR/sat_* > /dev/null 2>&1
rm -rf $OUTSATDIR/sol_sat_zchaff_* > /dev/null 2>&1
rm -rf $OUTSATTIMEDIR/sol_zchaff_* > /dev/null 2>&1
rmdir $INPUTSATDIR > /dev/null 2>&1
rmdir $OUTSATDIR > /dev/null 2>&1
rmdir $OUTSATTIMEDIR > /dev/null 2>&1

# Eliminamos soluciones previas
rm sol_sat_zchaff*.txt > /dev/null 2>&1
rm 'Reporte de ejecucion Sat Zchaff.txt' > /dev/null 2>&1

# Creamos directorios de salida
mkdir $INPUTSATDIR
mkdir $OUTSATDIR
mkdir $OUTSATTIMEDIR

# Ejecutamos el resolvedor propio
python3 ../main_zchaff.py $1
