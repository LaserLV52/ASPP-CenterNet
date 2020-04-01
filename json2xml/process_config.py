"""
Copyright (c) College of Mechatronics and Control Engineering, Shenzhen University.
All rights reserved.

Description :


Author：Team Li
"""

## bdd100k obj types ##
## if you don't wanne some types ,just delete those types in this list.
extracted_categorys_from_bdd100k = ['person', 'rider', 'bus', 'bike', 'truck', 'motor', 'car']

# extracted_conditions = {'daytime': ['night', 'dawn/dusk'],
#                         'obj_size_thresh': {'vehicle': 0.0008,
#                                               'person': 0.0008,
#                                               'traffic light': 0.0006,
#                                             'traffic sign': 0.0006},
#                         'weather':['clear']
#                         }
extracted_conditions = [0.001, 0.0011111]

name_dict = {'vehicle': ['car', 'truck', 'bus'],
             'person': ['person', 'rider'],
             'two-wheelers':['bike','motor']}

img_size = (720 ,1280)