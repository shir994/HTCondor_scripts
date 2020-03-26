import os
import sys


SUBFOLDER = os.environ["PRODUCTION_FOLDER"]
DATA_DIR = os.path.join(os.environ["EOS_DIR"], SUBFOLDER)
N_JOBS=13


with open("input_for_muon_prod.txt", "r") as f:
    for line in f:
        filepath, n_events, foldername = line.strip().split(", ")
        directory = os.path.join(DATA_DIR, foldername)
        if not os.path.exists(directory): 
            os.makedirs(directory)
        os.system("condor_submit directory={dir} N={n_jobs} muon_file={mf} n_events={ne} sim.sub".format(dir=os.path.join(SUBFOLDER, foldername),
                                                                                                         n_jobs=N_JOBS,
                                                                                                         mf=filepath,
                                                                                                         ne=n_events))
