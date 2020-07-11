#! /bin/bash

INPUTSATDIR=./SatInput
OUTSATDIR=./SatOutput
OUTSATTIMEDIR=./SatOutputTimes
REPORTSDIR=./Reports
SOLSATDIR=./SatSols
SUDOKUFILE=${1##*/}
SATINPUT="sat_*_$SUDOKUFILE"
SATOUTPUT="sol_sat_*_$SUDOKUFILE"
ALLSATOUTPUT="sol_sat_$SUDOKUFILE"
REPORTFILE="sol_sat_$SUDOKUFILE"

# Eliminamos soluciones y reportes previos
# para el archivo de entrada de instancias de sudoku
rm -rf $INPUTSATDIR/$SATINPUT > /dev/null 2>&1
rm -rf $OUTSATDIR/$SATOUTPUT > /dev/null 2>&1
rm -rf $OUTSATTIMEDIR/$ALLSATOUTPUT > /dev/null 2>&1
rm -rf $REPORTSDIR/$REPORTFILE
rm -rf $SOLSATDIR/$ALLSATOUTPUT

# Creamos directorios de salida
mkdir $INPUTSATDIR > /dev/null 2>&1
mkdir $OUTSATDIR > /dev/null 2>&1
mkdir $OUTSATTIMEDIR > /dev/null 2>&1
mkdir $REPORTSDIR > /dev/null 2>&1
mkdir $SOLSATDIR > /dev/null 2>&1

# Ejecutamos el resolvedor propio
# Tomamos T = 5 segs
python3 ../main_sat_solver.py $1 3