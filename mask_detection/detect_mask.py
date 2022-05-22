from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import argparse
import cv2
from abc import ABC, abstractclassmethod, abstractmethod

class Detect(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def change_model(self, model):
        pass
    @abstractmethod
    def image_processing(self):
        pass
    @abstractmethod
    def result(self, prediction, image):
        pass

#影像偵測
class DetectCamera(Detect):
    def __init__(self):
        self.model = load_model('keras_model.h5')
    
    def change_model(self, model):
        self.model = model
    def image_processing(self):
        cap = cv2.VideoCapture(0)

        while(True):
            # 從攝影機擷取一張影像
            ret, frame = cap.read()
            
            # Create the array of the right shape to feed into the keras model  
            # The 'length' or number of images you can put into the array is
            # determined by the first position in the shape tuple, in this case 1.
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            # Replace this with the path to your image
            image = Image.fromarray(np.uint8(frame))
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
            frame_and_cap = [frame, cap]
            self.result(prediction, frame_and_cap)
            
    def result(self, prediction, image):
        frame, cap = image
        #print(prediction)
        #print('WITH mask:','%2.1f' % (prediction[0][0]*100),'%')
        #print('NO mask:','%2.1f' % (prediction[0][1]*100),'%')
        #print('NOT proper mask:','%2.1f' % (prediction[0][2]*100),'%')
        #print('\nresult:',end='')
        if prediction[0][0] > prediction[0][1] and prediction[0][0] > prediction[0][2]:
            cv2.putText(frame, 'WITH mask', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 3, cv2.LINE_AA)
            #print('WITH mask')
        elif prediction[0][1] > prediction[0][0] and prediction[0][1] > prediction[0][2]:
            cv2.putText(frame, 'NO mask', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 3, cv2.LINE_AA)
            #print('NO mask') 
        else:
            cv2.putText(frame, 'NOT proper mask', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 3, cv2.LINE_AA)
            #print('NOT proper mask')
        
        # 顯示圖片
        cv2.imshow('frame', frame)

        # 若按下 q 鍵則離開迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.camera_release(cap)
            #break
    
    def camera_release(self, cap):
        # 釋放攝影機
        cap.release()

        # 關閉所有 OpenCV 視窗
        cv2.destroyAllWindows()

#照片偵測
class DetectImage(Detect):
    def __init__(self):
        self.model = load_model('keras_model.h5')
        
    def opt(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-s','--source', type=str, default='test.jpg', help='image path')
        self.opt = parser.parse_args()
    
    def change_model(self, model): #可選擇model
        self.model = model
        
    def image_processing(self):
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # Replace this with the path to your image
        path=self.opt.source
        print('path:',path)
        image = Image.open(self.opt.source)
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
#parser = argparse.ArgumentParser()
#parser.add_argument('-s','--source', type=str, default='test.jpg', help='image path')
#opt = parser.parse_args()

#detector=DetectImage()
#detector.opt()
#detector.image_processing()

test = DetectCamera()
test.image_processing()