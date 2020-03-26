#!/usr/bin/python
from __future__ import print_function

import ROOT
import os
import argparse
import math
import sys

from collections import defaultdict

def first_n_digits(num, n):
        return num // 10 ** (int(math.log(num, 10)) - n + 1)


DATA_DIR = sys.argv[1]


file = ROOT.TFile(DATA_DIR)
#ch.Add(args.input_file)


tree = file.Get("cbmsim")
print("Total entries:{}".format(tree.GetEntries()))

new_filename = sys.argv[2]
pruned_file = ROOT.TFile(new_filename, "recreate")
new_tree = tree.CloneTree(0)
pruned_file.Close()

print('N events saved(reco): {}'.format(events_reco))
print('N events has one hit: {}'.format(events_has_one_hit))


#old_file = ROOT.TFile.Open(os.path.join(DATA_DIR, "genie-nu_e.root"))
#h_old = file.Get("BranchList")
bl_tree = file.Get("BranchList")

newFile = ROOT.TFile(new_filename, "UPDATE")
new_tree = bl_tree.Write("BranchList", 1)
newFile.Close()
