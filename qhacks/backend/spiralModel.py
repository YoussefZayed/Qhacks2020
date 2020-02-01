from __future__ import absolute_import, division, print_function, unicode_literals

# Install TensorFlow

import tensorflow as tf
from PIL import Image
import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt



def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off') 
    plt.tight_layout()
    plt.show()

    

def train_Spiral (epochs= 10):
    while True:
        batch_size = 30
        
        IMG_HEIGHT = 256
        IMG_WIDTH = 256

        train_dir = "training/spiral/training"
        validation_dir = "training/spiral/testing"
        train_healthy_dir = os.path.join(train_dir, 'healthy')  # directory with our training healthy pictures
        train_parkinson_dir = os.path.join(train_dir, 'parkinson')  # directory with our training parkinson pictures
        validation_healthy_dir = os.path.join(validation_dir, 'healthy')  # directory with our validation healthy pictures
        validation_parkinson_dir = os.path.join(validation_dir, 'parkinson')  # directory with our validation parkinson pictures
        
        num_healthy_tr = len(os.listdir(train_healthy_dir))
        num_parkinson_tr = len(os.listdir(train_parkinson_dir))

        num_healthy_val = len(os.listdir(validation_healthy_dir))
        num_parkinson_val = len(os.listdir(validation_parkinson_dir))

        total_train = num_healthy_tr + num_parkinson_tr
        total_val = num_healthy_val + num_parkinson_val

        print('total training healthy images:', num_healthy_tr)
        print('total training parkinson images:', num_parkinson_tr)

        print('total validation healthy images:', num_healthy_val)
        print('total validation parkinson images:', num_parkinson_val)
        print("--")
        print("Total training images:", total_train)
        print("Total validation images:", total_val)


    
        
        image_gen_train = ImageDataGenerator(
                            rescale=1./255,
                            rotation_range=45,
                            width_shift_range=.15,
                            height_shift_range=.15,
                            horizontal_flip=True,
                            zoom_range=0.5
                            )

        train_data_gen = image_gen_train.flow_from_directory(batch_size=batch_size,
                                                            directory=train_dir,
                                                            shuffle=True,
                                                            target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                            class_mode='binary')
        augmented_images = [train_data_gen[0][0][0] for i in range(5)]

        image_gen_val = ImageDataGenerator(rescale=1./255)

        val_data_gen = image_gen_val.flow_from_directory(batch_size=batch_size,
                                                        directory=validation_dir,
                                                        target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                        class_mode='binary')
        model_new = Sequential([
            Conv2D(16, 3, padding='same', activation='relu', 
                input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
            MaxPooling2D(),
            Dropout(0.2),
            Conv2D(32, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Conv2D(64, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Dropout(0.2),
            Flatten(),
            Dense(512, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        model_new.load_weights('./checkpoints/my_checkpoint')

        model_new.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy'])

        model_new.summary()
        history = model_new.fit_generator(
            train_data_gen,
            steps_per_epoch=total_train // batch_size,
            epochs=epochs,
            validation_data=val_data_gen,
            validation_steps=total_val // batch_size
        )
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(epochs)

        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        #plt.show()

        test_image = image.load_img('training/test/V01HE01.png', target_size=(256,256))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        predictions = model_new.predict(test_image,batch_size=1)
        print(predictions)
        print("prediction for healthy is :" , predictions)
        test_image = image.load_img('training/test/V03PE01.png', target_size=(256,256))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        predictions = model_new.predict(test_image,batch_size=1)
        print(predictions)
        print("prediction for Park is :" ,predictions)
        model_new.save_weights('./checkpoints/my_checkpoint')


def train_wave (epochs= 10):
    while True:
        batch_size = 30
        
        IMG_HEIGHT = 256
        IMG_WIDTH = 256

        train_dir = "training/wave/training"
        validation_dir = "training/wave/testing"
        train_healthy_dir = os.path.join(train_dir, 'healthy')  # directory with our training healthy pictures
        train_parkinson_dir = os.path.join(train_dir, 'parkinson')  # directory with our training parkinson pictures
        validation_healthy_dir = os.path.join(validation_dir, 'healthy')  # directory with our validation healthy pictures
        validation_parkinson_dir = os.path.join(validation_dir, 'parkinson')  # directory with our validation parkinson pictures
        
        num_healthy_tr = len(os.listdir(train_healthy_dir))
        num_parkinson_tr = len(os.listdir(train_parkinson_dir))

        num_healthy_val = len(os.listdir(validation_healthy_dir))
        num_parkinson_val = len(os.listdir(validation_parkinson_dir))

        total_train = num_healthy_tr + num_parkinson_tr
        total_val = num_healthy_val + num_parkinson_val

        print('total training healthy images:', num_healthy_tr)
        print('total training parkinson images:', num_parkinson_tr)

        print('total validation healthy images:', num_healthy_val)
        print('total validation parkinson images:', num_parkinson_val)
        print("--")
        print("Total training images:", total_train)
        print("Total validation images:", total_val)


    
        
        image_gen_train = ImageDataGenerator(
                            rescale=1./255,
                            rotation_range=45,
                            width_shift_range=.15,
                            height_shift_range=.15,
                            horizontal_flip=True,
                            zoom_range=0.5
                            )

        train_data_gen = image_gen_train.flow_from_directory(batch_size=batch_size,
                                                            directory=train_dir,
                                                            shuffle=True,
                                                            target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                            class_mode='binary')
        augmented_images = [train_data_gen[0][0][0] for i in range(5)]

        image_gen_val = ImageDataGenerator(rescale=1./255)

        val_data_gen = image_gen_val.flow_from_directory(batch_size=batch_size,
                                                        directory=validation_dir,
                                                        target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                        class_mode='binary')
        model_new = Sequential([
            Conv2D(16, 3, padding='same', activation='relu', 
                input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
            MaxPooling2D(),
            Dropout(0.2),
            Conv2D(32, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Conv2D(64, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Dropout(0.2),
            Flatten(),
            Dense(512, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        model_new.load_weights('./checkpointsWave/my_checkpoint')

        model_new.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy'])

        model_new.summary()
        history = model_new.fit_generator(
            train_data_gen,
            steps_per_epoch=total_train // batch_size,
            epochs=epochs,
            validation_data=val_data_gen,
            validation_steps=total_val // batch_size
        )
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(epochs)

        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        #plt.show()

        test_image = image.load_img('training/test/V55HO09.png', target_size=(256,256))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        predictions = model_new.predict(test_image,batch_size=1)
        print(predictions)
        print("prediction for healthy is :" , predictions)
        test_image = image.load_img('training/test/V01PO01.png', target_size=(256,256))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        predictions = model_new.predict(test_image,batch_size=1)
        print(predictions)
        print("prediction for Park is :" ,predictions)
        model_new.save_weights('./checkpointsWave/my_checkpoint')
        

def testSpiral(path):
    batch_size = 30
        
    IMG_HEIGHT = 256
    IMG_WIDTH = 256
    image_gen_train = ImageDataGenerator(
                        rescale=1./255,
                        rotation_range=45,
                        width_shift_range=.15,
                        height_shift_range=.15,
                        horizontal_flip=True,
                        zoom_range=0.5
                        )


    image_gen_val = ImageDataGenerator(rescale=1./255)

    model_new = Sequential([
        Conv2D(16, 3, padding='same', activation='relu', 
            input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
        MaxPooling2D(),
        Dropout(0.2),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Dropout(0.2),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model_new.load_weights('./checkpoints/my_checkpoint')
    test_image = image.load_img(path, target_size=(256,256))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    predictions = model_new.predict(test_image,batch_size=1)
    return(predictions)

def testWave(path):
    batch_size = 30
        
    IMG_HEIGHT = 256
    IMG_WIDTH = 256
    image_gen_train = ImageDataGenerator(
                        rescale=1./255,
                        rotation_range=45,
                        width_shift_range=.15,
                        height_shift_range=.15,
                        horizontal_flip=True,
                        zoom_range=0.5
                        )

    image_gen_val = ImageDataGenerator(rescale=1./255)

    model_new = Sequential([
        Conv2D(16, 3, padding='same', activation='relu', 
            input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
        MaxPooling2D(),
        Dropout(0.2),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Dropout(0.2),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model_new.load_weights('./checkpoints/my_checkpoint')
    test_image = image.load_img(path, target_size=(256,256))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    predictions = model_new.predict(test_image,batch_size=1)
    return(predictions)
if __name__ == "__main__":
    print("\n\n\n\nThe result is:",testSpiral("V03PE01.png"))