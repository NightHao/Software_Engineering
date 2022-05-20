from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
image = Image.open('IMG_4340.jpg')
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
prediction = model.predict(data)
#print(prediction)
print('WITH mask:','%2.1f' % (prediction[0][0]*100),'%')
print('NO mask:','%2.1f' % (prediction[0][1]*100),'%')
print('NOT proper mask:','%2.1f' % (prediction[0][2]*100),'%')
print('\nresult:',end='')
if prediction[0][0] > prediction[0][1] and prediction[0][0] > prediction[0][2]:
    print('WITH mask')
elif prediction[0][1] > prediction[0][0] and prediction[0][1] > prediction[0][2]:
    print('NO mask')
else:
    print('NOT proper mask')
