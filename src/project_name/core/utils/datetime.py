import base64
from datetime import datetime
import numpy as np
import cv2
from io import BytesIO
from PIL import Image

class dt:
    """
    Datetime related operations
    """
    @staticmethod
    def new_strftime(dt_format):
        time_str = datetime.utcnow().strftime(dt_format)
        return time_str