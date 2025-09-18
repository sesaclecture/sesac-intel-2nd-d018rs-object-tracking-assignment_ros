# YOLOv5

## Set up
```
python3 -m venv .venv
source .venv/bin/activate
(.venv) pip install -r requirements.txt
(.venv) python -m pytest
```

### CPU Training
```
(.venv) python train.py \
  --data <path_to_dataset>/data.yaml \
  --weights yolov5m.pt \
  --epochs 10 --patience 0 --img 640 --batch 16 \
  --name rps_yolov5m
```

### XPU Training
```
(.venv) python train_xpu.py \
  --data <path_to_dataset>/data.yaml \
  --weights yolov5m.pt \
  --epochs 10 --patience 0 --img 640 --batch 30 \
  --name rps_yolov5m_xpu
```