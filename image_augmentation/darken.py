import cv2
import os
import numpy as np
import shutil
import argparse

def darkenImages(filePath,pathOut):
    for filename in os.listdir(filePath):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            image_path = filePath + filename
            image_pathOut = pathOut + 'darkened_' + filename
            image = cv2.imread(image_path)
            darken = np.ones(image.shape, dtype = 'uint8') * 70
            darken_image = cv2.subtract(image, darken)
            cv2.imwrite(image_pathOut, darken_image)
            continue
        else:
            continue
    print("Images successfully darkened.")

def duplicateAnnotation(filePath,pathOut):
    for filename in os.listdir(filePath):
        if "classes" in filename:
            continue
        if filename.endswith('.txt'):
            shutil.copy(filePath+filename, pathOut+filename)
            os.rename(pathOut+filename, pathOut+'darkened_'+filename)
            continue
        else:
            continue
    print('Annotation files duplicated.')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filePath', type=str, help='path/to/images/')
    parser.add_argument('pathOut', type=str, help='empty/image/directory/')
    args = parser.parse_args()

    darkenImages(filePath = args.filePath, 
                   pathOut = args.pathOut)
    duplicateAnnotation(filePath = args.filePath, 
                        pathOut = args.pathOut)

if __name__=="__main__":
    main()
