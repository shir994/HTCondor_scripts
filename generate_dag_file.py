import os
import sys

N_JOBS = 13
FOLDER_NAME = os.environ["PRODUCTION_FOLDER"]
OUTFILE = os.environ["OUTFILE"]

DATA_DIR = os.path.join(os.environ["EOS_DIR"], FOLDER_NAME)

with open("input_for_muon_prod.txt", "r") as f:
    with open("dag_submit.tmp", "w") as output:
        file_count = 0
        for index, line in enumerate(f):
            filepath, n_events, foldername = line.strip().split(", ")
            directory = os.path.join(DATA_DIR, foldername)
            if not os.path.exists(directory): 
                os.makedirs(directory)
            print(f"JOB SUB{index} sim.sub", file=output)
            print(f"JOB FLUX{index} flux.sub", file=output)
            print("VARS SUB{index} directory=\"{dir}\" N=\"{n_jobs}\" muon_file=\"{mf}\" n_events=\"{ne}\"".format(dir=os.path.join(FOLDER_NAME, foldername),
                                                                                                  n_jobs=N_JOBS,
                                                                                                  mf=filepath,
                                                                                                  ne=n_events,
                                                                                                  index=index), file=output)
            print("VARS FLUX{index} directory=\"{dir}\" N=\"{n_jobs}\" outfile=\"{filename}\"".format(dir=os.path.join(FOLDER_NAME,
            foldername), filename=OUTFILE, n_jobs=N_JOBS, index=index), file=output)
            print(f"PARENT SUB{index} CHILD FLUX{index}", file=output)
            file_count += 1
        print("JOB HADD hadd.sub", file=output)
        print("VARS HADD directory=\"{dir}\" fluxfile=\"{outfile}\" filename=\"{finalfile}\"".format(dir=FOLDER_NAME,
        outfile=OUTFILE, finalfile="total_flux.root"), file=output)
        parent_str = " ".join([f"FLUX{index}" for index in range(file_count)])
        print("PARENT " + parent_str + " CHILD HADD", file=output)
        
