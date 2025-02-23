import cv2
import numpy as np
import pydicom


def segment_image(file_path):
    """
    Beolvassa a DICOM képet a megadott file_path alapján, normalizálja,
    és egy dummy szegmentációt készít (például egy kör a kép közepén).

    Visszatér az eredeti kép (normalizált) és a maszk tömbbel.
    """
    try:
        ds = pydicom.dcmread(file_path)
        image = ds.pixel_array.astype(np.float32)
        # Normalizálás 0-1 közé
        image = (image - np.min(image)) / (np.max(image) - np.min(image))

        height, width = image.shape
        mask = np.zeros((height, width), dtype=np.uint8)
        center = (width // 2, height // 2)
        radius = min(center) // 2
        # Dummy: rajzolunk egy kitöltött kört a kép közepére
        cv2.circle(mask, center, radius, 1, -1)
        return image, mask
    except Exception as e:
        print("Hiba a DICOM beolvasásakor:", e)
        return None, None
