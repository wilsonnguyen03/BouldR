# ML

Training and inference for climbing hold detection.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Dataset

Download a climbing holds segmentation dataset (e.g. from Roboflow Universe)
and unzip into `data/dataset/`. Update the path in `train.py` if needed.

## Train

```powershell
python train.py
```

## Predict

```powershell
python predict.py path\to\image.jpg
```
