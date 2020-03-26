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
tree = file.Get("cbmsim")
print("Total entries:{}".format(tree.GetEntries()))

new_filename = sys.argv[2]
pruned_file = ROOT.TFile(new_filename, "recreate")
new_tree = tree.CloneTree(0)


MUON = 13
STRAW_FIRST = 1
STRAW_LAST = 4
events_reco = 0
events_has_one_hit = 0
for index, event in enumerate(tree):
    if index % 50000 == 0:
        print(index)

    mc_pdgs = []
    for hit in event.MCTrack:
        mc_pdgs.append(hit.GetPdgCode())

    mc_index_to_hits_detID = defaultdict(set)
    for hit in event.strawtubesPoint:
        if hit.GetTrackID() >= 0 and\
           abs(mc_pdgs[hit.GetTrackID()]) == MUON:
               det_id = first_n_digits(hit.GetDetectorID(), 1)
               mc_index_to_hits_detID[hit.GetTrackID()].add(det_id)

    if len(mc_index_to_hits_detID) > 0:
        events_has_one_hit += 1

    for mc_index, det_ids in mc_index_to_hits_detID.items():
        if STRAW_FIRST in det_ids:
            new_tree.Fill()
            events_reco += 1
            break


new_tree.Write()
pruned_file.Close()

print('N events saved(reco): {}'.format(events_reco))
print('N events has one hit: {}'.format(events_has_one_hit))

bl_tree = file.Get("BranchList")

newFile = ROOT.TFile(new_filename, "UPDATE")
new_tree = bl_tree.Write("BranchList", 1)
newFile.Close()
