# import open cv for image processing
from pyexpat import model
import cv2
# impoert os for file and folder handdling
import os
import numpy as np
import pickle # save the model

data_dir="data/faces"

# list to store face images and their labels
faces = []
labels = []

# dictionary to map label id to label name
label_map = {}

label_id = 0
for person in os.listdir(data_dir):
    person_path = os.path.join(data_dir, person)

    # skip if folder is not
    if not os.path.isdir(person_path):
        continue

    label_map[label_id] = person

    # lopp through each image of person
    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        # read image JPG/PNG
        img = cv2.imread(img_path)

        if img is None:
            continue

        # convert image to grayscale
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        gray=cv2.resize(gray,(200,200))
        faces.append(gray)
        labels.append(label_id)
    label_id += 1

# covert list to array
faces =np.array(faces)
labels =np.array(labels)

# create LBPH ( Local Binary Pattern Histogram) face recognizer model
model=cv2.face.LBPHFaceRecognizer_create()

# train the model
model.train(faces,labels)

os.makedirs("models",exist_ok=True)

model.save("models/face_model.yml")

# save model id to os.name
with open("models/labels.pkl","wb") as f:
    pickle.dump(label_map,f)

print("Face recognition model trained successfully")
