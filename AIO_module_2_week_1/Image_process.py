import matplotlib . image as mpimg
img = mpimg.imread('dog.jpeg')
#Lightness
# gray_img_01 = (img.max(axis=2) + img.min(axis=2)) / 2
#Average
# gray_img_01 = img.mean(axis = 2)
#Luminosity
gray_img_01 = img[:,:,0] * 0.21 + img[:,:,1] * 0.72 + img[:,:,2] * 0.07
print(gray_img_01 [0 , 0])
