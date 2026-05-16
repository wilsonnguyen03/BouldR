"""Train YOLO11-seg on climbing holds dataset."""
from ultralytics import YOLO


def main():
    model = YOLO("yolo11n-seg.pt")  # nano segmentation, pretrained on COCO

    model.train(
        data="data/dataset/data.yaml",  # update path once you download a dataset
        epochs=50,
        imgsz=640,
        batch=16,
        project="runs",
        name="holds-v1",
        patience=15,  # early stop if no improvement
    )


if __name__ == "__main__":
    main()
