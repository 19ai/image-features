#!/usr/bin/env python3
# Count the number of files for each class label

import glob

data_files = glob.glob('./data/*.csv')
class_labels = {}

for file in data_files:
    label = file.split('-')[0].replace('\\', '/').split('/')[-1]
    if label not in class_labels:
        class_labels[label] = 1
    else:
        class_labels[label] = class_labels[label] + 1

for k,v in class_labels.items():
    print('{}: {}'.format(k,v))
