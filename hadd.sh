#!/bin/bash
source $SHIP_CVMFS_SETUP_FILE
alienv printenv FairShip/latest >> ./config.sh
source config.sh
set -ux
#folders=($(ls $2))
#no need for filename anymore
folders=(`find "$3" -name $2`)
hadd "$1" $(eval echo ${folders[@]}) && xrdcp "$1" "$3"/"$1"
