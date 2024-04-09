import os
import time
import uuid
import cv2

IMAGE_PATH = "Data/Collected_Images"

signs = ["Hello", "Yes", "No", "Thanks", "I Love You", "Please"]

number_of_images = 30

for sign in signs:
    img_path = os.path.join(IMAGE_PATH, sign)
    os.makedirs(img_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    print("Collecting images for {}".format(sign))
    time.sleep(5)

    for imgnum in range(number_of_images):
        success, img = cap.read()
        image_name = os.path.join(IMAGE_PATH, sign, sign + "." + "{}.jpg".format(str(uuid.uuid1())))
        cv2.imwrite(image_name, img)
        cv2.imshow("Sign: {}".format(sign), img)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    cap.release()

