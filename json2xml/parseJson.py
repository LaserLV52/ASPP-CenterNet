#-*-coding:utf-8-*-
#parse json，input json filename,output info needed by voc

import json
from process_config import *

def parseJson(jsonFile, extracted_conditions=None, name_dict=None):
    """ process the bdd100k raw json file
    jsonFile: full name of a josn file.
    extracted_conditions: labels that meet the condition would be extracted
    name_dict: bdd category to our category.
    """
    n_objs = {'vehicle': 0, 'person': 0, 'two-wheelers': 0}
    cover_val_objs = {'vehicle': [], 'person': [],  'two-wheelers': []}
    objs = []
    f = open(jsonFile)
    info = json.load(f)
    objects = info['frames'][0]['objects']
    weather = info['attributes']['weather']
    daytime = info['attributes']['timeofday']
    #if weather in extracted_conditions['weather'] and daytime in extracted_conditions['daytime']:
    for i in objects:
        obj = []
        if(i['category'] in extracted_categorys_from_bdd100k):
            if i['category'] in name_dict['vehicle']:
                obj_type = 'vehicle'
            elif i['category'] in name_dict['person']:
                obj_type = 'person'
            elif i['category'] in name_dict['two-wheelers']:
                obj_type = 'two-wheelers'
            else:
                obj_type = i['category']

            xmin = float(i['box2d']['x1'])
            ymin = float(i['box2d']['y1'])
            xmax = float(i['box2d']['x2'])
            ymax = float(i['box2d']['y2'])
            bbox = (xmin, ymin, xmax, ymax)
            condition, val = meet_size_condition(img_size, bbox, obj_type, extracted_conditions)
            if condition:
                obj.append(int(xmin))
                obj.append(int(ymin))
                obj.append(int(xmax))
                obj.append(int(ymax))
                obj.append(obj_type)
                objs.append(obj.copy())
                n_objs[obj_type] += 1
                cover_val_objs[obj_type].append(val)
    return n_objs, cover_val_objs, objs


def meet_size_condition(img_size, bbox, obj_type, size_condition):
    #thresh = size_condition[obj_type]
    thresh = size_condition

    obj_h = bbox[3] - bbox[1]
    obj_w = bbox[2] - bbox[0]
    cover_val = obj_w*obj_h / (img_size[0]*img_size[1])
    # if thresh[0] <= cover_val <= thresh[1] :
    #     return True, cover_val
    # else:
    #     return False, None
    if cover_val >= thresh:
        return True, cover_val
    else:
        return False, None
