import base64
import numpy as np
import cv2
from io import BytesIO
from PIL import Image

class converter:
    """
    Image conversion between OpenCV and PIL
    Convert request image file to b64 encoded string
    """
    @staticmethod
    def pil_to_cv(img_pil):
        img_cv = np.array(img_pil)
        # Convert RGB to BGR
        img_cv = img_cv[:, :, ::-1]
        return img_cv
    
    @staticmethod
    def cv_to_pil(img_cv):
        # Convert BGR to RGB
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        return img_pil
    
    @classmethod
    def request_file_to_b64(cls, file):
        img = Image.open(file)
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        b64 = base64.b64encode(buffered.getvalue())
        return b64