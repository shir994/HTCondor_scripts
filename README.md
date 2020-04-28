Basic scripts to submit jobs to CERN batch system. If you will modify scripts, remember, that HTCondor Docker universe **DOES NOT** work with `/afs`, only `/eos`.

How to: 

- define `EOS_DIR`, `CONDOR_ROOT` in `set_global_envs.sh`. Define geometry file and directory where you want to save results on EOS by setting `PRODUCTION_FOLDER` and `MAGNET_GEO` in `set_paths_flux.sh`.
- `source set_global_envs.sh && source set_paths_flux.sh`
- `mkdir $CONDOR_ROOT/error $CONDOR_ROOT/output $CONDOR_ROOT/log` (this need to be done only once)
- `python3 generate_dag_file.py`
- `condor_submit_dag dag_submit.tmp`.

How to use:
### Step 1
Set up variables names, used during submission. EOS_DIR is your usual `username` EOS folder. `CONDOR_ROOT` is the folder where you want HTCondor to write output, error and log messages. `MAGNET_GEO_FULL_PATH` is the shield geofile you want to test. For example, `MAGNET_GEO_FULL_PATH=/eos/experiment/ship/data/magnet_geofiles/magnet_geo_to_test_oliver.root`. It must be an absolute path to the file. `MAGNET_GEO` is determined automatically, do not change it. `PRODUCTION_FOLDER` is where the whole output will be written on the EOS, i.e. all output will be saved at `EOS_DIR/PRODUCTION_FOLDER`.
### Step 2
Set the variables above.
### Step 3 (important)
Create folders for log/output/error logs. This is important to do, otherwise you jobs might stuck idle forever!
### Step 4
Generate DAG submission file. It will created jobs to process 67 muon. It will subsequently run `sim.sub->flux.sub` and in the and will create final output file of the flux in the `EOS_DIR/PRODUCTION_FOLDER`.
### Step 5
Submit jobs to cluster.

In the end, you should have the follwoing output structure
```
EOS_DIR/PRODUCTION_FOLDER
|
|
|____1
|    |
|    └____0
|    |     ship.conical.MuonBack-TGeant4.root
|    |     flux.root
|    |
|     ...
|    └____N_JOBS
...
└____67
```
