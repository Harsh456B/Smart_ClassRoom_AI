# import libraries

# image data generator ko import karege for loading or process a image 
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential #cnn  model ke liya
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten #cnn layer

# used optimer for optimed themodel
from tensorflow.keras.optimizers import Adam

# data path 
train_dir = 'data/emotions/train'
test_dir = 'data/emotions/test'

# image data generator
train_generator = ImageDataGenerator(rescale=1./255,  # pixel values 0–1 me convert
                                   rotation_range=20,
                                   zoom_range=0.2,  # zoom in or zoom out
                                   horizontal_flip=True)  # image horizontal flip

test_generator = ImageDataGenerator(rescale=1./255)

# load train data
train_data = train_generator.flow_from_directory(train_dir,
                                                    target_size=(48, 48),
                                                    color_mode='grayscale',
                                                    batch_size=32,
                                                    class_mode='categorical')
# load test data
test_data = test_generator.flow_from_directory(test_dir,
                                                    target_size=(48, 48),
                                                    color_mode='grayscale',
                                                    batch_size=32,
                                                    class_mode='categorical')

# cnn model
model = Sequential()

# 1st cnn layer 
model.add(Conv2D(32, (3, 3), input_shape=(48, 48, 1), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Dropout(0.25))

# 2nd cnn layer 
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Dropout(0.25))

# 3rd cnn layer 
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

# Output Layer (7 emotions)
model.add(Dense(7, activation='softmax'))

model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    train_data,
    epochs=10,
    validation_data=test_data
)

model.save('models/emotion_model.h5')
