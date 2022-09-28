import cv2
# Location and Name of Image
image_Location = 'C:/Users/Microsoft/Desktop/'
image_Name = 'image.jpg'
# read and display the original image
image = cv2.imread(image_Location+image_Name)
cv2.imshow("Original_Image", image)
# convert the original image to gray scale image and display it
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_Image", gray_image)
# invert the gray scale image and display it
inverted_gray_image = 255 - gray_image
cv2.imshow("Inverted_Gray_Image", inverted_gray_image)
# bluer the inverted image and display it
blured_image = cv2.GaussianBlur(inverted_gray_image , (21,21) , 0)
cv2.imshow("Blured_Image", blured_image)
# invert the bluer image and display it
inverted_blur_image = 255 - blured_image
cv2.imshow("Inverted_Blur_Image", inverted_blur_image)
# create a pencil sketch image and display it
Pencil_Sketch_image = cv2.divide(gray_image, inverted_blur_image, scale=265)
cv2.imshow("Pencil_Sketch_Image", Pencil_Sketch_image)
cv2.waitKey(0)