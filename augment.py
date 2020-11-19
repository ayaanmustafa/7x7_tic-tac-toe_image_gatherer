""" from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.15,
        zoom_range=0.25,
        horizontal_flip=True,
        fill_mode='nearest')

img = load_img('img15.png')  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='preview', save_prefix='img', save_format='.png'):
    i += 1
    if i > 20:
        break  # otherwise the generator would loop indefinitely
# example of horizontal shift image augmentation """

from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import os
path = "images_for_O\\just_before_augment"
total = os.listdir(path)
for imagei in total:
        img = path+"\\"+imagei
        # load the image
        img = load_img(img)
        # convert to numpy array
        data = img_to_array(img)
        # expand dimension to one sample
        samples = expand_dims(data, 0)
        # create image data augmentation generator
        datagen = ImageDataGenerator(
                rotation_range=1,
                width_shift_range=0.045,
                height_shift_range=0.045,
                shear_range=0.05,
                zoom_range=0.05,
                horizontal_flip=True,
                fill_mode='nearest')
        datagen.fit(samples)

        # prepare iterator
        for x, val in zip(datagen.flow(samples,                    #image we chose
                save_to_dir="D:\\Pygame_projects\\7x7_CNN\\images_for_O\\augmented",     #this is where we figure out where to save
                save_prefix='aug',        # it will save the images as 'aug_0912' some number for every new augmented image
                save_format='png'),range(8)) :     # here we define a range because we want 10 augmented images otherwise it will keep looping forever I think
                pass
