import detect_mask as mask
import tkinter as tk
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageDraw, ImageFont
camera_detect=mask.DetectCamera()
camera_detect.change_model("keras_model_strong.h5")
res, pic =camera_detect.image_processing()
result = ["Pass", "Without mask", "No proper mask"]
draw = ImageDraw.Draw(pic)
myfont = ImageFont.truetype("C:/windows/fonts/Arial.ttf", size = 80)
fillcolor = "#CC3299"
draw.text((30,30), result[res], font = myfont, fill=fillcolor)
plt.imshow(pic)
plt.show()