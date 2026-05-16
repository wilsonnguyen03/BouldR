# API

FastAPI service that wraps the trained model and exposes a `/detect` endpoint
returning per-hold polygons and dominant colors.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
uvicorn main:app --reload
```
