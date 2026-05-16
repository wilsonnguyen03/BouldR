"""Extract dominant color from a segmented hold region."""
import cv2
import numpy as np


def dominant_hsv(image_bgr: np.ndarray, mask: np.ndarray) -> tuple[int, int, int]:
    """
    Given a BGR image and a binary mask of one hold,
    return the dominant (H, S, V) color of that hold.

    Uses hue weighted by saturation to ignore shadows/highlights.
    """
    hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    pixels = hsv[mask > 0]

    if len(pixels) == 0:
        return (0, 0, 0)

    saturations = pixels[:, 1].astype(float)
    weights = saturations / (saturations.sum() + 1e-9)

    h_weighted = int(np.average(pixels[:, 0], weights=weights))
    s_median = int(np.median(pixels[:, 1]))
    v_median = int(np.median(pixels[:, 2]))

    return (h_weighted, s_median, v_median)


def hsv_to_name(h: int, s: int, v: int) -> str:
    """Map HSV to a rough color name. Tune these ranges to your gym."""
    if v < 40:
        return "black"
    if s < 30 and v > 200:
        return "white"
    if s < 40:
        return "gray"

    # OpenCV hue is 0-179
    if h < 10 or h >= 170:
        return "red"
    if h < 25:
        return "orange"
    if h < 35:
        return "yellow"
    if h < 85:
        return "green"
    if h < 130:
        return "blue"
    if h < 160:
        return "purple"
    return "pink"
