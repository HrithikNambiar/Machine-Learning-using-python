Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

data = keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels)= data.load_data()
#normlization
train_images = train_images /255
test_images = test_images/255
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
model = keras.Sequential([
    keras.layers.Flatten(input_shape = (28,28)),
    keras.layers.Dense(128,activation ="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer = "adam", loss="sparse_categorical_crossentropy",metrics=["accuracy"])
model.fit(train_images,train_labels,epochs=7)


for i in range(5):
    plt.grid()
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("Actual : "+ class_names[test_labels[i]])
    plt.title("prediction : " + class_names[np.argmax(prediction[i])])
    plt.show()
