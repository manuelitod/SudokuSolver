#! /bin/bash

FILE=${1##*/}
SATPROPIOPREFIX="sol_sat_"
SATZCHAFFPREFIX="sol_sat_zchaff_"
SATPROPIOTIMEFILE="$SATPROPIOPREFIX$FILE"
SATZCHAFFTIMEFILE="$SATZCHAFFPREFIX$FILE"

# Corremos los scripts de resolucion
sh resolvedor_propio.sh $1
sh resolvedor_zchaff.sh $1

# Ploteamos
python3 ../main_plt_maker.py $1 $SATPROPIOTIMEFILE $SATZCHAFFTIMEFILE
