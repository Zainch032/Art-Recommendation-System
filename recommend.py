import numpy as np
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, ResNet50
from keras.layers import GlobalMaxPool2D
from keras.models import Sequential
import pickle
import cv2
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load embeddings and filenames
features = np.array(pickle.load(open(os.path.join(script_dir, "model/embedding.pkl"),"rb")))
filenames = pickle.load(open(os.path.join(script_dir, "model/file.pkl"),"rb"))

# Build model
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))
base_model.trainable = False
model = Sequential([base_model, GlobalMaxPool2D()])

# Extract features
def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    result = model.predict(img_array).flatten()
    return result / np.linalg.norm(result)

# Recommendation function
def recommend(img_path, top_k=5):
    from sklearn.neighbors import NearestNeighbors

    knn = NearestNeighbors(n_neighbors=top_k, metric="euclidean")
    knn.fit(features)

    query_feature = extract_features(img_path)
    distances, indices = knn.kneighbors([query_feature])

    recommended_paths = [filenames[idx] for idx in indices[0][1:7]]
    return recommended_paths
