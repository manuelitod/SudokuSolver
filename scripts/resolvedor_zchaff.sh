#! /bin/bash

INPUTSATDIR=./SatInput
OUTSATDIR=./SatOutput
OUTSATTIMEDIR=./SatOutputTimes
REPORTSDIR=./Reports
SOLSATDIR=./SatSols
SUDOKUFILE=${1##*/}
SATINPUT="sat_*_$SUDOKUFILE"
SATOUTPUT="sol_sat_zchaff_*_$SUDOKUFILE"
ALLSATOUTPUT="sol_sat_zchaff_$SUDOKUFILE"
REPORTFILE="sol_sat_zchaff_$SUDOKUFILE"

# Eliminamos soluciones y reportes previos
# para el archivo de entrada de instancias de sudoku
rm -rf $INPUTSATDIR/$SATINPUT > /dev/null 2>&1
rm -rf $OUTSATDIR/$SATOUTPUT > /dev/null 2>&1
rm -rf $OUTSATTIMEDIR/$ALLSATOUTPUT > /dev/null 2>&1
rm -rf $REPORTSDIR/$REPORTFILE
rm -rf $SOLSATDIR/$ALLSATOUTPUT

# Creamos directorios de salida
mkdir $INPUTSATDIR
mkdir $OUTSATDIR
mkdir $OUTSATTIMEDIR

# Ejecutamos el resolvedor propio
# Tomamos T = 2 segs
python ../main_zchaff.py $1 2
