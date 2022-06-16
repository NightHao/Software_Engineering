from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import argparse
import cv2
import tkinter as tk
from tkinter import ttk
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
        self.model = load_model('keras_model_strong.h5')

    def change_model(self, model):
        self.model = load_model(model)
    def image_processing(self):
        cap = cv2.VideoCapture(0)
        res_judge = []
        while(len(res_judge) < 20):
            # 從攝影機擷取一張影像
            ret, frame = cap.read()
            
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            image = Image.fromarray(np.uint8(frame))

            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)

            image_array = np.asarray(image)

            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            data[0] = normalized_image_array

            prediction = self.model.predict(data)
            frame_and_cap = [frame, cap]
            res, res_frame =  self.result(prediction, frame_and_cap)
            res_judge.append(res)
            #return self.result(prediction, frame_and_cap)
        cv2.imwrite("output.jpg", res_frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        res_image = Image.open("output.jpg")
        max_times = max(res_judge, key=res_judge.count)
        return (max_times, res_image)
            
    def result(self, prediction, image):
        frame, cap = image
        if prediction[0][0] > prediction[0][1] and prediction[0][0] > prediction[0][2]:
            #cv2.putText(frame, 'WITH mask', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 3, cv2.LINE_AA)
            return (0, frame)
        elif prediction[0][1] > prediction[0][0] and prediction[0][1] > prediction[0][2]:
            #cv2.putText(frame, 'NO mask', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 3, cv2.LINE_AA)
            return (1, frame)
        else:
            #cv2.putText(frame, 'NOT proper mask', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 3, cv2.LINE_AA)
            return (2, frame)
        # 顯示圖片
        #cv2.imshow('frame', frame)
        
    def camera_release(self, cap):
        # 釋放攝影機
        cap.release()

        # 關閉所有 OpenCV 視窗
        cv2.destroyAllWindows()

#照片偵測
class DetectImage(Detect):
    def __init__(self):
        self.model = load_model('keras_model.h5')
    
    def opt(self,path):
        self.path=path
       
    def change_model(self, model): #可選擇model
        self.model = model
        
    def image_processing(self):
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        path=self.path
        print('path:',path)
        image = Image.open(path)
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        prediction = self.model.predict(data)
        
        return self.result(prediction, image)
        
    def result(self, prediction, image):
        #image.show()#pillow 顯示圖片函式
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

#detector=DetectImage()
#detector.opt()
#detector.image_processing()
#test.image_processing()