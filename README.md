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

* (Optional) Download pretrained weight [vehicle_weight](https://drive.google.com/file/d/1mNBeJozHTnMsFqX7KQWmgeeKAwikHu0U/view?usp=sharing)

### Executing program

* Run tracking 
```
python track.py --source 0  # webcam
                         img.jpg  # image
                         vid.mp4  # video
                         path/  # whole directory
                         'https://youtu.be/Link'  # YouTube
                         'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

## Acknowledgments

[Ultralytics (Yolov5)](https://github.com/ultralytics/yolov5)

[Mikel Broström (Yolov5 + Deep Sort with OSNet)](https://github.com/mikel-brostrom/Yolov5_DeepSort_OSNet)

[MaryamBoneh (Vehicles Dataset)](https://github.com/MaryamBoneh/Vehicle-Detection)

