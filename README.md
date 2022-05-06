# Yolov5-Vehicle-Counting

A computer vision and artificial intelligence project to detect and counting vehicles.

## Description

This project is using YOLOV5 and Deep Sort Algorithm to perform object recognition and tracking realtime. 

### Dependencies

* OS: Windows/ Linux
* Python >= 3.8
```
pip install -r requirement.txt
```
### Installing

* (Optional) Download pretrained weight [vehicle_weight.pt](https://drive.google.com/file/d/1mNBeJozHTnMsFqX7KQWmgeeKAwikHu0U/view?usp=sharing)

### Executing program track.py to track object
1. Media source
```
$ python track.py --source 0  # webcam
                           img.jpg  # image
                           vid.mp4  # video
                           path/  # whole directory
                           'https://youtu.be/link'  # YouTube
                           'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```
2. Yolo Model
```
$ python track.py --source 0 --yolo_model yolov5n.pt 
                                          yolov5s.pt 
                                          yolov5m.pt       
                                          yolov5l.pt 
                                          yolov5x.pt 
                                          ...
```
3. Image size (pixels)
```
$ python track.py --source 0 --yolo_model yolov5n.pt --img 640  
                                                     --img 1280 
                       
```
4. How to save output
```
$ python track.py --source 0 --yolo_model yolov5n.pt --img 640  --save-vid
                                                                --show-vid
                                                                --save-txt
```
### Train your own weight with custom data
1. Change to yolov5 directory
```
$ cd yolov5
```
2. Prepare your custom data in /datasets directory

create datasets/data.yaml
```
$ cd datasets
$ nano data.yaml
```
```
# example of data.yaml
names:
- Car
- Motorcycle
- Truck
- Bus
- Bicycle
nc: 5                           #no. of classes
train: dataset/train/images     # path to train images directory
val: dataset/valid/images       # path to validation images directory
```
create train and validation directory
```
$ mkdir train valid
$ mkdir train/images train/labels valid/images valid/labels
```
check the directories are existed
```
$ ls */

# the output should be look like this
# 
# train/:
# images labels labels.cache
#
# valid/:
# images labels labels.cache
```
3. Put dataset in /datasets/train and /datasets/valid directories

* (Optional)download vehicles datasets from [MaryamBoneh/Vehicle-Detection](https://github.com/MaryamBoneh/Vehicle-Detection) by this [link](https://b2n.ir/vehicleDataset)

4. Edit yolo config in /models
```
$ nano /models/yolov5.yaml

# Example in case of using yolov5m.yaml -> change no. of classes in parameters section to match your classes. Like below!
# Parameters
nc: 5 #  <--- this one (number of classes)
depth_multiple: 0.67  # model depth multiple
width_multiple: 0.75  # layer channel multiple
anchors:
  - [10,13, 16,30, 33,23]  # P3/8
  - [30,61, 62,45, 59,119]  # P4/16
  - [116,90, 156,198, 373,326]  # P5/32
                  .
                  .
                  .
```
5. Run train.py (ex. img_size = 640px, batch_size = 16, epochs = 3)

For new train weight
```
$ python train.py --img 640 --batch 16 --epochs 48 --data models/custom_yolov5.yaml --weights '' --cache
```

For continue trained weight (trained weight name = 'custom_yolov5.pt')
```
$ python train.py --img 640 --batch 16 --epochs 48 --data models/custom_yolov5.yaml --weights custom_yolov5.pt --cache
```

## Acknowledgments

[Ultralytics (Yolov5)](https://github.com/ultralytics/yolov5)

[Mikel Broström (Yolov5 + Deep Sort with OSNet)](https://github.com/mikel-brostrom/Yolov5_DeepSort_OSNet)

[MaryamBoneh (Vehicles Dataset)](https://github.com/MaryamBoneh/Vehicle-Detection)

## Contributor
- Ridhirin Lukkanawaraporn
- [Siriphak Amrapal](https://www.linkedin.com/in/siriphak-amrapal)
- [Charnkanit Keawwong](www.linkedin.com/in/charnkanit-kaewwong)
