# road_detection
# Road Damage Detection (YOLOv8)

## About the project

This project is about detecting road damage like potholes and cracks using a deep learning model.
The idea is to automate road inspection instead of doing it manually.

We used YOLOv8 for detection and tested it on video input. The model is also intended to run on Jetson Nano so that everything can work on-device (edge computing).

---

## What it does

* Detects potholes and cracks in road images/videos
* Draws bounding boxes on detected areas
* Works on video file (`road.mp4`)
* Can be deployed on Jetson Nano

---

## Model used

* YOLOv8n (nano version)
* Chosen because it is lightweight and fast
* Works better for real-time compared to heavier models

---

## Dataset

* Road Damage Dataset (RDD)
* Converted to YOLO format
* Initially had multiple classes (crack, damage, pothole, etc.)
* Later simplified to:

  * 0 → crack
  * 1 → pothole

---

## Results

* mAP50: ~36%
* Precision: ~40%
* Recall: ~44%

Not very high accuracy, but the model is able to detect potholes reasonably well in many cases.

---

## Folder structure

```
road_detection/
  train/
    images/
    labels/
  valid/
    images/
    labels/
  runs/
  test.py
  train.py
  data.yaml
  yolov8n.pt
  road.mp4
```

---

## How to run

### Install requirements

```
pip install ultralytics opencv-python
```

### Run detection

```
python test.py
```

or

```
yolo task=detect mode=predict model=yolov8n.pt source=road.mp4
```

---

## Notes

* OpenCV gives images in BGR format but YOLO handles it internally
* Output video is saved instead of displayed when running on Jetson

---

## Limitations

* Dataset is small
* Model sometimes gives low confidence
* Performance depends on lighting

---

## Future improvements

* Increase dataset size
* Train for more epochs
* Try YOLOv8s for better accuracy
* Optimize using TensorRT

---

## Author

Ishika Jain
Thapar Institute of Engineering & Technology

---
