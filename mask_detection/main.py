import argparse
import detect_mask as mask
class detect_main:
    def __init__(self):
        self.image_model=mask.DetectImage()
        self.camera_model=mask.DetectCamera()
    def opt(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-s','--source', type=str, default='test.jpg', help='image path')
        self.opt = parser.parse_args()
    def detect(self):
        self.opt()
        Input=self.opt.source
        if(Input=="cam"):
            self.camera_model.image_processing()
        else:
            self.image_model.opt(Input)
            res,resImage=self.image_model.image_processing()

detector=detect_main()
detector.detect()
