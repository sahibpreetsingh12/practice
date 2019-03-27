import cv2
for i in range(1,14): 
    image = cv2.imread('/home/sahib/Downloads/train/virat/vk'+str(i)+'.jpeg',-1)
    #image1 = cv2.imread('/home/sahib/Downloads/train/dhoni/dh'+str(i)+'.jpeg',-1)
    
    
     
    cv2.imshow(str(i),image)
    #cv2.imshow(str(i),image1)
    print(image.shape)
    #print(image1.shape)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
