import numpy as np
from PIL import Image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input,decode_predictions


model=VGG16(weights='imagenet',include_top=True)

print(models.layers)
