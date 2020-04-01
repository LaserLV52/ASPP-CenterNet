#1.1把bdd的json文件根据用户需求筛选出合适的标签，并储存成voc数据集类型的xml格式文件，并生成文件名合集txt
#-*-coding:utf-8-*-
import os
import random
import pascal_voc_io
import parseJson
import json

from skimage import io

from process_config import *

obj_cover_record = {'vehicle': [], 'person': [],  'two-wheelers': []}

obj_number_record = {'vehicle': 0, 'person': 0,  'two-wheelers': 0}

saveImg = True
saveAnotation = True

if __name__ == '__main__':
    ## bdd json file dir##
    dirName = "J:/Dataset/BDD100K/bdd100k_labels/bdd100k/labels/100k/val/"
    imgDir = 'J:/Dataset/BDD100K/bdd100k_images/bdd100k/images/100k/val/'

    ## where you wanne save the xml file ##
    savePath = "J:/Python program/CenterNet_2/bdd_labels_xml/"
    imgSavePath = 'J:/Python program/CenterNet_2/data/BDD/images/'

    i = 0
    with open('./vallist.txt', 'w') as file:
        for dirpath,dirnames,filenames in os.walk(dirName):
            #filenames = random.sample(filenames, 5000)
            for filepath in filenames:
                fileName = os.path.join(dirpath,filepath)
                xmlFileName, extension = os.path.splitext(filepath)
                #xmlFileName = filepath[:-5]
                #print("xml: ",xmlFileName)

                n_objs, cover_val_objs, objs = parseJson.parseJson(str(fileName), extracted_conditions, name_dict)
                if len(objs):
                    if saveAnotation:
                        i += 1
                        tmp = pascal_voc_io.PascalVocWriter(savePath=savePath,filename=xmlFileName,
                                                            imgSize=(720,1280,3), databaseSrc="BDD100K")
                        file.write('%s\n' % (str(xmlFileName)))
                        for obj in objs:
                            tmp.addBndBox(obj[0],obj[1],obj[2],obj[3],obj[4])
                        tmp.save()

                        for obj_type, n in n_objs.items():
                            obj_number_record[obj_type] += n
                        for obj_type, cover_val in cover_val_objs.items():
                            obj_cover_record[obj_type].extend(cover_val)
                    #elif saveImg:
                        imgName = filepath.split('.')[0]
                        imgName = os.path.join(imgDir, imgName+'.jpg')
                        img = io.imread(imgName)
                        io.imsave(imgSavePath+'/'+filepath.split('.')[0]+'.jpg',img)
        file.close()


    if saveAnotation:
        with open('./obj_num_record.txt', 'w') as file:
            file.write('Total imgs:%s\n' % (str(i)))
            for obj_type, n in obj_number_record.items():
                print('Obj_type:%s -- Total number:%s'%(obj_type, str(n)))
                file.write('Obj_type:%s -- Total number:%s\n'%(obj_type, str(n)))

        with open('./obj_cover_val_record.json', 'w') as file:
            json.dump(obj_cover_record, file)