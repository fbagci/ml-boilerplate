import base64
import numpy as np
import cv2
import json
from PIL import Image
import yaml


class rw:
    """
    Read image from path \n
    Write image to path \n
    Read b64 in json format from txt file \n
    Write b64 in json format to txt file \n
    """
    @staticmethod
    def read_img(img_fpath, img_format="cv"):
        if img_format == "cv":
            img = cv2.imread(img_fpath)
        elif img_format == "pil":
            img = Image.open(img_fpath)
        return img

    @staticmethod
    def write_img(img, img_fpath, img_format):
        if img_format is "cv":
            cv2.imwrite(img_fpath, img)
        elif img_format is "pil":
            img.save(img_fpath)
        print(f"Saved to {img_fpath}")

    @staticmethod
    def read_b64_from_file(full_path):
        with open(full_path, "r") as txt_file:
            b64_str = txt_file.read()
        b64_json = json.loads(b64_str)
        b64 = b64_json["image"]
        return b64

    @staticmethod
    def write_b64_to_file(b64, full_path):
        b64_json_str = str({"image":b64}).replace("'", "\"")
        with open(full_path, "w") as txt_file:
            txt_file.write(b64_json_str)

    @staticmethod    
    def get_config(config_fpath = "./config.yml"):
        """
        Read config from yml
        """
        with open(config_fpath, "r") as stream:
            conf = yaml.safe_load(stream)
        return conf