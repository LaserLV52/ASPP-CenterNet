# ASPP-CenterNet
Road object detection for BDD-100k bsaed on CenterNet. The detection performance is better than original CenterNet with same backbone, especially in smaller size objects.


# Approaches
We use Hourglass as backbone and adopted atrous spatial pyramid pooling and space to depth methods. The idea of represent object as a center point and the format of output layers are same as original CenterNet.


# Use ASPP-CenterNet
First, prepare the corresponding pre-trained model.  
For object detection on images/ video, run:

    python demo.py  --demo /path/to/image/or/folder/or/video --load_model /path/to/pre-trained model

# Train your own dataset
1.Extract labels  
If you need to  filter the original dataset, use the bdd2voc.py in json2xml folder.  
You can extract your desired datasets according to weather conditions, object categories, area sizes, etc. 

2.Partition dataset  into training, validation, and test set.

3.Generate annotations files  
After extract and partition the dataset, use VOC2COCO labels.py to transform the .xml files into .json files.  
Then, put the .json files under the \data\BDD\annotations folder.  

4.Prepare images  
Put the dataset images under the \data\BDD\images folder.  

5.Train  
Run: 

    python main.py  
or  

    python main.py  --resume --load_model  /path/to/pre-trained model  
    
for default parameters.



# Test your model
Run:

    python test.py  --keep_res --load_model /path/to/pre-trained model

to test your model.
