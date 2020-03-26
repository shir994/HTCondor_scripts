import numpy as np
import os
import sys


def get_files_size(root_folder, filename):
    _size=0
    for folder in os.listdir(root_folder):
        print(os.path.join(root_folder, folder, filename))
        try:
            muons_part = np.load(os.path.join(root_folder, folder, filename))            
            _size += len(np.unique(muons_part[:, :2], axis=0))
        except IOError as e:
            print(e)
            continue
    return _size

def save_file(up_folder, size, root_folder, filename):
    muons = np.empty([size, 3])
    index = 0
    for folder in os.listdir(root_folder):
        print(os.path.join(root_folder, folder, filename))
        try:
            muons_part = np.load(os.path.join(root_folder, folder, filename))
            muons_part = muons_part[np.unique(muons_part[:, :2], axis=0, return_index=True)[1]][:, [3,4,9]]
        except IOError as e:
            print(e)
            continue
        muons[index : index + len(muons_part), :] = muons_part
        index += len(muons_part)
    np.save("angles_" + up_folder +".npy", muons)

ROOT_FOLDER = sys.argv[1]
counter = 0
for folder in os.listdir(ROOT_FOLDER):
    if os.path.exists("angles_" + folder +".npy"):
        continue
    size = get_files_size(os.path.join(ROOT_FOLDER, folder), "all_veto.npy")
    save_file(folder, size, os.path.join(ROOT_FOLDER,folder), "all_veto.npy")
    counter += 1
    print("Count", counter)
print(size)





