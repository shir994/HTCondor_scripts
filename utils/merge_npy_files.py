import numpy as np
import os
import sys


def get_files_size():
    _size=0
    for folder in os.listdir(sys.argv[1]):
        print(os.path.join(sys.argv[1], folder, sys.argv[2]))
        try:
            muons_part = np.load(os.path.join(sys.argv[1], folder, sys.argv[2]))
            _size += len(muons_part)
        except IOError as e:
            print(e)
            continue
    return _size

counter = 0
_size = get_files_size()
muons = np.empty([_size, 16])

index = 0
for folder in os.listdir(sys.argv[1]):
    print(os.path.join(sys.argv[1], folder, sys.argv[2]))
    try:
        muons_part = np.load(os.path.join(sys.argv[1], folder, sys.argv[2]))
    except IOError as e:
        print(e)
        continue
    muons[index : index + len(muons_part), :] = np.hstack([np.ones([len(muons_part), 1]) * int(folder), muons_part])
    index += len(muons_part)
    counter += 1
np.save(sys.argv[3], muons)
print("Files processed: {}".format(counter))
