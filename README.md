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

### Executing program

* Run tracking
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
* Train your own weight with custom data
1. Change to yolov5 directory
```
$ cd yolov5
```
2. Prepare your custom data in /datasets directory
```
# create and edit data.yaml
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
```
# create train and validation directory
$ mkdir train
$ mkdir valid
```
## Acknowledgments

[Ultralytics (Yolov5)](https://github.com/ultralytics/yolov5)

[Mikel Broström (Yolov5 + Deep Sort with OSNet)](https://github.com/mikel-brostrom/Yolov5_DeepSort_OSNet)

[MaryamBoneh (Vehicles Dataset)](https://github.com/MaryamBoneh/Vehicle-Detection)

