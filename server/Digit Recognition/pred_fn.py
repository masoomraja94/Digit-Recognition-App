import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image

with open("model.json", "r") as file:
    model = model_from_json(file.read())
model.load_weights("model.h5")

def preprocess_image(img):
    img = image.load_img(img, color_mode="grayscale", target_size=(28, 28, 1))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img

def encode_image(img):
    img = preprocess_image(img)
    feature_vector = img.reshape(1, 28, 28, 1)
    return feature_vector

def pred_val(img):
    enc = encode_image(img)
    pred = model.predict_classes(enc)[0]
    return pred
