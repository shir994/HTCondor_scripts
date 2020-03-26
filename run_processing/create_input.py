#!/usr/bin/python
from __future__ import print_function

import ROOT
import os


DATA_DIR = "/eos/experiment/ship/data/Mbias/background-prod-2018/"

#pythia8_Geant4_1.0_c1000_mu.root
with open("input_for_muon_prod.txt", 'w') as f:
    for root, dirs, file_names in os.walk(DATA_DIR):
        for file_name in file_names:
            strip_name = file_name.strip().split("_")
            if strip_name[-1] == "mu.root" and strip_name[-3] == "1.0":
                input_file = os.path.join(DATA_DIR, file_name)
                root_file = ROOT.TFile(input_file)
                tree = root_file.Get("cbmsim")
                print(input_file + ",", str(tree.GetEntries()) + ",", int(strip_name[-2][1:]) / 1000, file=f)

