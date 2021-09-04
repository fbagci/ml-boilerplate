import base64
import cv2

class encoder:
    """
    Image encoding methods
    """
    @staticmethod
    def get_b64_from_img_file(img_fpath):
        img = cv2.imread(img_fpath)
        # im_arr: image in Numpy one-dim array format.
        _, im_arr = cv2.imencode('.jpg', img)
        im_bytes = im_arr.tobytes()
        b64 = base64.b64encode(im_bytes).decode("utf-8")
        return b64