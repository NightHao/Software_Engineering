from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import argparse
import cv2

class DetectCamera:
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

test = DetectCamera()
test.image_processing()