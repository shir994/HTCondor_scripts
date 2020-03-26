from __future__ import print_function
import os
import sys

DATA_PREFIX = os.environ["EOS_DIR"]
FOLDER_NAME = sys.argv[1]

FILENAME = os.environ["MERGED_FILENAME"]
OUTPUTNAME = os.environ["OUTPUTNAME"]
     

with open(os.path.join(sys.argv[2], 'file_to_reco.txt'), 'w') as f:
    for folder in os.listdir(os.path.join(DATA_PREFIX, FOLDER_NAME)):
        #if folder not in ["check_old_script"]:
        print(os.path.join(DATA_PREFIX, FOLDER_NAME, folder, FILENAME), ", ", OUTPUTNAME, file=f, sep="")

