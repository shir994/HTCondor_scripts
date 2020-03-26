import numpy as np
import os
import sys


def get_mask(muons, bound):
    return np.logical_and(muons[:, -4] >= bound[0],  muons[:, -4] <= bound[1]) 

def get_files_size(root_folder, filename):
    _size=0
    for folder in os.listdir(root_folder):
        print(os.path.join(root_folder, folder, filename))
        try:
            muons_part = np.load(os.path.join(root_folder, folder, filename))            
            _size += get_mask(muons_part, bound).sum()#len(np.unique(muons_part[:, :2], axis=0))
        except IOError as e:
            print(e)
            continue
    return _size

def save_file(up_folder, size, root_folder, filename, saved_name):
    muons = np.empty([size, 16])
    index = 0
    for folder in os.listdir(root_folder):
        print(os.path.join(root_folder, folder, filename))
        try:
            muons_part = np.load(os.path.join(root_folder, folder, filename))
            muons_part = muons_part[get_mask(muons_part, bound)]
        except IOError as e:
            print(e)
            continue
        muons[index : index + len(muons_part), :] = muons_part
        index += len(muons_part)
    np.save(saved_name, muons)


bound = (-39999999, -6417.2000)
ROOT_FOLDER = sys.argv[1]
counter = 0
for folder in os.listdir(ROOT_FOLDER):
    file_name = "veto_" + folder + ".npy"
    if os.path.exists(file_name):
        continue
    size = get_files_size(os.path.join(ROOT_FOLDER, folder), "all_veto.npy")
    save_file(folder, size, os.path.join(ROOT_FOLDER,folder), "all_veto.npy", file_name)
    counter += 1
    print("Count", counter)
print(size)





