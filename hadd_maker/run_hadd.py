import os
import sys

DATA_PREFIX = os.environ["EOS_DIR"]

FOLDER_NAME = sys.argv[1]


for folder in os.listdir(os.path.join(DATA_PREFIX, FOLDER_NAME)):
    print(os.path.join(FOLDER_NAME, folder))
    os.system("condor_submit directory={dir} filename={filename} hadd_ls.sub".format(dir=os.path.join(FOLDER_NAME, folder),
                                                                                     filename=os.environ["MERGED_FILENAME"]))
