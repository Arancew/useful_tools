import cv2
image = cv2.imread('mapbox.tif')

one=1700
x = 2200  # x坐标
y = 1900 # y坐标
x1 = x+one  # x坐标
y1 = y+one # y坐标
cropped_image = image[y:y1, x:x1]

cv2.imwrite('cropped_image.jpg', cropped_image)
cv2.destroyAllWindows()







