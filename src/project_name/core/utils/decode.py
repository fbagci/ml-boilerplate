import base64
import numpy as np
import cv2
from io import BytesIO
from PIL import Image

class decoder:
    """
    Image decoding methods
    """
    @staticmethod
    def decode_b64(b64, img_format="pil"):
        im_bytes = base64.b64decode(b64)
        if img_format == "pil":
            img = Image.open(BytesIO(im_bytes))
        elif img_format == "cv":
            img_arr = np.frombuffer(im_bytes, dtype=np.uint8)
            img = cv2.imdecode(img_arr, flags=cv2.IMREAD_COLOR)
        return img