import cv2
image = cv2.imread(r'D:\code\uav_ponit\Position_correction\data\mapbox.tif')
'''
老校区
one=2000
x = 2050  # x坐标
y = 1700 # y坐标
新校区
one=2300
x = 1050  # x坐标
y = 2150 # y坐标
'''
one=2000
x = 2050  # x坐标
y = 1700 # y坐标
x1 = x+one  # x坐标
y1 = y+one # y坐标
cropped_image = image[y:y1, x:x1]

cv2.imwrite('cropped_image.jpg', cropped_image)
cv2.destroyAllWindows()
print("[{},{}],[{},{}]".format(x,y,x1,y1))







