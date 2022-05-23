import argparse
import detect_mask as mask
import show 
class DetectMain:
    def __init__(self):
        self.image_model=mask.DetectImage()
        self.camera_model=mask.DetectCamera()
        self.screen = show.ShowOnMonitor() 
    def opt(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-s','--source', type=str, default='IMG_4340.jpg', help='image path')
        self.opt = parser.parse_args()
    def detect(self):
        self.opt()
        Input=self.opt.source
        if(Input=="cam"):
            res, res_image = self.camera_model.image_processing()
            self.screen.show(res, res_image)
        else:
            self.image_model.opt(Input)
            res, res_image=self.image_model.image_processing()
            self.screen.show(res, res_image)
detector=DetectMain()
detector.detect()