#!/bin/bash
source $SHIP_CVMFS_SETUP_FILE
source $FAIRSHIP_DIR/config.sh
set -ux
echo "Starting script."
DIR=$1
OUTFILE=$2
if eos stat `dirname "${DIR}"`/"$OUTFILE"; then
    echo "Target exists, nothing to do."
    exit 0
else
    python read_tree_and_reco.py "$DIR" "$OUTFILE" 
    xrdcp "$OUTFILE" root://eospublic.cern.ch/`dirname "${DIR}"`/"$OUTFILE"
    xrdcp "${OUTFILE%.*}.root" root://eospublic.cern.ch/`dirname "${DIR}"`/"${OUTFILE%.*}.root"
fi
