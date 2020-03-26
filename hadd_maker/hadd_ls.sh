#!/bin/bash
source $SHIP_CVMFS_SETUP_FILE
source $FAIRSHIP_DIR/config.sh
set -ux
#folders=($(ls $2))
#no need for filename anymore
folders=(`find "$2" -name ship*.root`)
hadd "$1" $(eval echo ${folders[@]}) && xrdcp "$1" "$2"/"$1"
