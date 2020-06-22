#! /bin/bash

FILE=${1##*/}
SATPROPIOPREFIX="sol_sat_"
SATZCHAFFPREFIX="sol_sat_zchaff_"
SATPROPIOTIMEFILE="$SATPROPIOPREFIX$FILE"
SATZCHAFFTIMEFILE="$SATZCHAFFPREFIX$FILE"

# Corremos los scripts de resolucion
./resolvedor_propio.sh $1
./resolvedor_zchaff.sh $1

# Ploteamos
python3 ../main_plt_maker.py $1 $SATPROPIOTIMEFILE $SATZCHAFFTIMEFILE
