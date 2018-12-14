import cv2

test = cv2.imread('./face.jpg')
gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

#plt.imshow(gray, cmap='gray')
cv2.imshow('Test Imag', gray) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

#load cascade classifier training file for haarcascade 
haar_face_cascade = cv2.CascadeClassifier('./model.xml')
faces = haar_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:     
    cv2.rectangle(test, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imshow('Test Imag', test) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

cv2.imwrite('./boundingbox.jpg',test)
