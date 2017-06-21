import cv2 
import glob
import os

cascade_path = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)

input_dir_name = "img_test"
output_dir_name = input_dir_name + "_out"

try:
	os.mkdir(output_dir_name)
except:
	pass

photo_name = 'img_test_97.png'
img = cv2.imread("img_test/"+photo_name)
faces = cascade.detectMultiScale(img, minSize=(10,10))
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cut_img = img[y:y+h,x:x+w]
cv2.imshow('img',img)
cv2.imwrite("face_of_" + photo_name,cut_img)

'''for path_name in glob.glob(input_dir_name + "/*"):
	file_name = path_name.split("/")[1]
	img = cv2.imread(path_name)
	try:
		faces = cascade.detectMultiScale(img, minSize=(30,30))
		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       		cut_img = img[y:y+h,x:x+w]
	
		cv2.imshow('img',img)
		cv2.imwrite(output_dir_name + "/" + file_name,cut_img)
		cv2.destroyAllWindows()
	except:
		print(file_name)'''