import numpy as np
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image
from keras.layers import GlobalMaxPool2D
from keras.applications.resnet50 import ResNet50,preprocess_input
from keras.models import Sequential
from tqdm import tqdm

model = ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))

model.trainable = False
model = Sequential([model,GlobalMaxPool2D()])

def extract_features(img_path, model):
    # Load the image
    img = image.load_img(img_path, target_size=(224, 224))

    
    img_array = image.img_to_array(img)

   
    img_array = np.expand_dims(img_array, axis=0)

   
    img_array = preprocess_input(img_array)

    
    features = model.predict(img_array).flatten()

    # Normalize vector (important for similarity search)
    normalized_features = features / np.linalg.norm(features)

    return normalized_features

import os
filenames = []

for file in os.listdir("resized"):
    filenames.append(os.path.join("resized",file))
    
    
feature_list = []

for file in tqdm(filenames):
    feature_list.append(extract_features(file,model))
    
    
    
import pickle

pickle.dump(filenames,open("file.pkl","wb"))
pickle.dump(feature_list,open("embedding.pkl","wb"))