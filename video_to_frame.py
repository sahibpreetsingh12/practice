import cv2
vidcap = cv2.VideoCapture('/home/sahib/Downloads/10back.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("/home/sahib/Downloads/10rs/10+%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print(success,image,type(success),type(image))
  print('Read a new frame: ', success)
  count += 1
