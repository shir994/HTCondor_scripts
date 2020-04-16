#!/bin/bash
alienv printenv FairShip/latest >> ./config.sh
source config.sh
echo `klist`
set -ux
echo "Starting script."
DIR=$1
ProcId=$2
LSB_JOBINDEX=$((ProcId+1))
NJOBS=$3
OUTFILE=$4
EOS_DIR=$5
if xrdfs root://eospublic.cern.ch/ stat "$EOS_DIR"/"$DIR"/"$LSB_JOBINDEX"/"$OUTFILE"; then
	echo "Target exists, nothing to do."
	exit 0
else
    xrdcp root://eospublic.cern.ch/"$EOS_DIR"/"$DIR"/"$LSB_JOBINDEX"/ship.conical.MuonBack-TGeant4.root ship.conical.MuonBack-TGeant4.root  
    python "$FAIRSHIP"/macro/flux_map.py --inputfile ship.conical.MuonBack-TGeant4.root -o $OUTFILE
	xrdcp $OUTFILE root://eospublic.cern.ch/"$EOS_DIR"/"$DIR"/"$LSB_JOBINDEX"/"$OUTFILE"
fi
