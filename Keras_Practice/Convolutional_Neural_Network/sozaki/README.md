# Reconizing types of Fruit

## Dataset
Retrieved dataset from [Kaggle](https://www.kaggle.com/moltean/fruits)

## Implementation
I used Keras' generators to grab the appropirate pictures of fruits in their respective directories and then classify by the names of the directories.

## Information
I have trained the neural network using less data to keep the time to train the CNN down.

## Running this script
- You need to have the Keras package for Python3 already installed before starting this program.
- Go into sozaki_fruit_recongnition.py and near the top there will be boolean variables, which will change what the code does when you run it.

## Find pictures from Google
You should have google images download after install all packages using pip3, if not run `pip3 install google_images_download`. Then run `googleimagesdownload -k "name of the images you want to seach" -l 20` (20 is the limit of images it downloads)
For example,
`googleimagesdownload -k "a bunch of apples" -l 20` searches for 'a bunch of apples' and only downloads 20 images

**for more information** please visit creator's [git repo](https://github.com/hardikvasa/google-images-download)

## Current Status
Loss: 1.015977989543568
Accuracy: ~88%

## Dataset
You need zip before unziping in linux(`sudo apt-get install zip`). You will need to unzip both zip files before running the code.
simply type: `unzip test_data.zip` and `unzip training_dataset.zip`
