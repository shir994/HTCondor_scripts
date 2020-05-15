#!/bin/bash
source $SHIP_CVMFS_SETUP_FILE
alienv printenv FairShip/latest >> ./config.sh
source config.sh
set -ux
echo "Starting script."
DIR=$1
ProcId=$2
LSB_JOBINDEX=$((ProcId+1))
NJOBS=$3
OUTFILE=$4
if eos stat "$EOS_DIR"/"$DIR"/"$LSB_JOBINDEX"/"$OUTFILE"; then
	echo "Target exists, nothing to do."
	exit 0
else
    if ! eos stat "$EOS_DIR"/"$DIR"/"$LSB_JOBINDEX"/ship.conical.MuonBack-TGeant4.root; then
        echo "ship root file does not exist, exit"
        exit 0
    fi
    python "$FAIRSHIP"/macro/flux_map.py --inputfile "$EOS_DIR"/"$DIR"/"$LSB_JOBINDEX"/ship.conical.MuonBack-TGeant4.root -o $OUTFILE
	xrdcp $OUTFILE root://eospublic.cern.ch/"$EOS_DIR"/"$DIR"/"$LSB_JOBINDEX"/"$OUTFILE"
fi
