"""Serving layer for climbing hold detection."""
from fastapi import FastAPI

app = FastAPI(title="Bouldering Climb Detector")


@app.get("/health")
def health():
    return {"status": "ok"}


# TODO: /detect endpoint that accepts an image and returns hold polygons + colors
