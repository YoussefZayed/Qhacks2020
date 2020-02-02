    
import os
import json
from tensorflow.python.lib.io import file_io
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.models import Sequential, load_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np




def train(epoc = 100):
    model = Sequential()
    model.add(Input((6,)))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    model =load_model('sound2.h5')
    df = pd.read_csv("pd_speech_features.csv")
    labels = df["Status"]
    df = df.drop(columns=["Status"], axis=1)
    X_train, X_test, Y_train, Y_test = train_test_split(df, labels, test_size=0.2, random_state=15324)
    X_train, X_validation, Y_train, Y_validation = train_test_split(X_train, Y_train, test_size=0.25, random_state=205)
    history = model.fit(X_train, Y_train, validation_data=(X_validation, Y_validation), epochs=100)
    model.evaluate(X_test, Y_test)
    plt.plot(history.history["loss"])
    plt.plot(history.history["val_loss"])

    model.save("sound2.h5")


def predict(arr):
    model =load_model('sound2.h5')
    test = np.array(arr)
    test = np.reshape(test,(1,6))
    print(model.predict(test))

if __name__ == "__main__":
    for _ in range(10):
        train(100)
    predict([1,0.024923,0.22018,0.013534,0.015444,0.019314])
    predict([0,0.024067,0.20747,0.011582,0.014153,0.021818])
    predict([0,0.087788,0.76832,0.051024,0.054779,0.059937])

