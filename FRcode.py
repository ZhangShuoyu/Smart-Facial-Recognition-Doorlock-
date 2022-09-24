import cv2
import face_recognition
import smtplib
import imghdr
from email.message import EmailMessage

img = cv2.imread('Bill gates.jpg')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#faceLoc=face_recognition.face_locations(rgb_img)[0]
img_encoding = face_recognition.face_encodings(rgb_img)[0]
#cv2.rectangle(rgb_img,(faceLoc[3],faceLoc[0]),(faceLoc[1]),faceLoc[2]),(255,0,255),2)


img2 = cv2.imread('1.png')
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#faceLoc=face_recognition.face_locations(rgb_img2)[0]
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]
#cv2.rectangle(rgb_img2,(faceLoc2[3],faceLoc2[0]),(faceLoc2[1]),faceLoc2[2]),(255,0,255),2)

# Load some images to compare against
known_Yingzhe_image = face_recognition.load_image_file("Yingzhe.jpg")
known_Xiaotang_image = face_recognition.load_image_file("Xiaotang.jpg")
known_biden_image = face_recognition.load_image_file("Bill gates.jpg")

# Get the face encodings for the known images
Yingzhe_face_encoding = face_recognition.face_encodings(known_Yingzhe_image)[0]
Xiaotang_face_encoding = face_recognition.face_encodings(known_Xiaotang_image)[0]
biden_face_encoding = face_recognition.face_encodings(known_biden_image)[0]

known_encodings = [
    Yingzhe_face_encoding,
    Xiaotang_face_encoding,
    biden_face_encoding
]

# Load a test image and get encondings for it
image_to_test = face_recognition.load_image_file("New visitor.jpg")
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

# See how far apart the test image is from the known faces
# face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)
result = face_recognition.compare_faces(known_encodings, image_to_test_encoding,tolerance = 0.4)
print("Result: ", result)

#result = face_recognition.compare_faces([img_encoding], img_encoding2)
#print("Result: ", result)

#cv2.imshow("Img",img)
cv2.imshow("New visitor",image_to_test)
cv2.waitKey(5)

Sender_Email = "lpmyl2430784698@gmail.com"
Reciever_Email = "lpmyl2430784698@gmail.com"
#Password = '# '
Password = input('Enter your email account password: ')

newMessage = EmailMessage()                         
newMessage['Subject'] = "You have a new guest!" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('We just attached his/her pretty face!') 

with open('New visitor.jpg', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name

newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)
