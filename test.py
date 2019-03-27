##import os
##import cv2
##from imutils import paths
##import numpy as np
##from keras.preprocessing.image import ImageDataGenerator
##from keras.optimizers import Adam
##from keras.preprocessing.image import img_to_array
##ls=list(paths.list_images("/home/sahib/Downloads/train/dhoni"))
##data=[]
##labels=[]
##for path_iterator in ls:
##    img=cv2.imread(path_iterator)
##    img=cv2.resize(img,(150,150))
##    img=img_to_array(img)
##    data.append(img)
##    label_maker=path_iterator.split("/")[-2]
##    print(label_maker)
##    labels.append(label_maker)
##    
##print(len(labels))
##print(type(data[0]),data[0],data[0].shape)
##data = np.array(data, dtype="float") / 255.0
##labels = np.array(labels)
##print(labels)

import tensorflow as tf
import cv2

img=cv2.imread('/home/sahib/Downloads/waves.jpeg')
print(img.shape,type(img))
imgs=img[:,:,1]
print(img.shape,type(img))
print(imgs.shape,type(imgs))
cv2.imshow("s",img[:,:,:1])
cv2.waitKey(0)

##cv2.imshow('Window',img)
##cv2.waitKey(0)
