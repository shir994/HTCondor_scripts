#!/bin/bash
source $SHIP_CVMFS_SETUP_FILE
#source $FAIRSHIP_DIR/config.sh
set -ux
folders=(`find "$3" -name $2`)
hadd "$1" $(eval echo ${folders[@]}) && xrdcp "$1" "$3"/"$1"
