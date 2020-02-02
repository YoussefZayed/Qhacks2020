    
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
import sys
import soundget




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


def predict(path,g = 0):
    arr = soundget.getfeatures(path,g)
    model =load_model('sound2.h5')
    test = np.array(arr)
    test = np.reshape(test,(1,6))
    return(model.predict(test))

if __name__ == "__main__":
    predict(soundget.getfeatures(sys.argv[1],sys.argv[2]))


