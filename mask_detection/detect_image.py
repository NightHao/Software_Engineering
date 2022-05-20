from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import argparse
import cv2

class Detect:
    def __init__(self,opt):
        self.opt=opt
        self.model = load_model('keras_model.h5')
        
    def change_model(self, model): #可選擇model
        self.model = model
        
    def image_processing(self):
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # Replace this with the path to your image
        path=opt.source
        print('path:',path)
        image = Image.open(opt.source)
        #print(type(image))
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        #turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array
        # run the inference
        prediction = self.model.predict(data)
        
        return self.result(prediction, image)
        
    def result(self, prediction, image):
        image.show()#pillow 顯示圖片函式
        #print(prediction)
        print('WITH mask:','%2.1f' % (prediction[0][0]*100),'%')
        print('NO mask:','%2.1f' % (prediction[0][1]*100),'%')
        print('NOT proper mask:','%2.1f' % (prediction[0][2]*100),'%')
        print('\nresult:',end='')
        if prediction[0][0] > prediction[0][1] and prediction[0][0] > prediction[0][2]:
            print('WITH mask')
            return 0,image#傳結果和圖片
        elif prediction[0][1] > prediction[0][0] and prediction[0][1] > prediction[0][2]:
            print('NO mask')
            return 1,image
        else:
            print('NOT proper mask')
            return 2,image  

#可能需要統一相片編號
parser = argparse.ArgumentParser()
parser.add_argument('-s','--source', type=str, default='test.jpg', help='image path')

opt = parser.parse_args()
detector=Detect(opt)
detector.image_processing()

#取眾數判斷結果
def judge(images_state):
    with_mask, no_mask, not_proper_mask = 0, 0, 0
    for i in images_state:
        if images_state == 0:
            with_mask += 1
        elif images_state == 1:
            no_mask += 1
        else:
            not_proper_mask += 1
    mode = max(with_mask, no_mask, not_proper_mask)
    if mode == with_mask:
        return "With mask"
    elif mode == no_mask:
        return "No mask"
    else:
        return "Not proper mask"
