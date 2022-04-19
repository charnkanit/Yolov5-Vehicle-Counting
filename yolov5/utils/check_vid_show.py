import cv2
import numpy as np
def check_imshow():
    # Check if environment supports image displays
    try:
        #assert not is_docker(), 'cv2.imshow() is disabled in Docker environments'
        #assert not is_colab(), 'cv2.imshow() is disabled in Google Colab environments'
        cv2.imshow('test', np.zeros((1, 1, 3)))
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        return True
    except Exception as e:
        #LOGGER.warning(f'WARNING: Environment does not support cv2.imshow() or PIL Image.show() image displays\n{e}')
        return False


if check_imshow():
    print("ok")
else:
    print("not ok")