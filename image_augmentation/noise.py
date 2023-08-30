import cv2
import os
import shutil
import numpy as np 
from argparse import ArgumentParser

def noise(filePath, pathOut):
    for filename in os.listdir(filePath):
        filename = filename.lower()
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            image_path = filePath + filename
            image_pathOut = pathOut+'noise_'+filename
            image = cv2.imread(image_path)
            mean = 0
            stddev = 200
            noise = np.zeros(image.shape, np.uint8)
            cv2.randn(noise, mean, stddev)
            noisy = cv2.add(image, noise)
            cv2.imwrite(image_pathOut, noisy)
        else:
            continue
    print('Images made noisy.')

def duplicateAnnotation(filePath, pathOut):
    for filename in os.listdir(filePath):
        if "classes" in filename:
            continue
        if filename.endswith('.txt'):
            shutil.copy(filePath+filename, pathOut+filename)
            os.rename(pathOut+filename, pathOut+'noise_'+filename)
            continue
        else:
            continue
    print('Annotation files duplicated.')


def main():
    # use example: 'python blur.py path/to/images/ empty/image/directory/'
    parser = ArgumentParser()
    parser.add_argument('filePath', type=str, help='path/to/images/')
    parser.add_argument('pathOut', type=str, help='empty/image/directory/')
    args = parser.parse_args()
    noise(filePath = args.filePath, pathOut = args.pathOut)
    duplicateAnnotation(filePath = args.filePath, pathOut = args.pathOut)
        
if __name__ == '__main__':
	main()