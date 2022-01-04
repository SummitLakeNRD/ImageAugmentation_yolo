import cv2
import os
import numpy as np
import shutil
import argparse

def brightenImages(filePath,pathOut):
    for filename in os.listdir(filePath):
        if filename.endswith('png') or filename.endswith('.jpg'):
            image_path = filePath + filename
            image_pathOut = pathOut + 'brightened_' + filename
            image = cv2.imread(image_path)
            brighten = np.ones(image.shape, dtype = 'uint8') * 60
            brighen_image = cv2.add(image, brighten)
            cv2.imwrite(image_pathOut, brighen_image)
            continue
        else:
            continue
    print("Images successfully brightened.")

def duplicateAnnotation(filePath,pathOut):
    for filename in os.listdir(filePath):
        if "classes" in filename:
                continue
        if filename.endswith('.txt'):
                shutil.copy(filePath+filename, pathOut+filename)
                os.rename(pathOut+filename, pathOut+'brightened_'+filename)
                continue
        else:
                continue
    print('Annotation files duplicated.')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filePath', type=str, help='path/to/images/')
    parser.add_argument('pathOut', type=str, help='empty/image/directory/')
    args = parser.parse_args()

    brightenImages(filePath = args.filePath, 
                   pathOut = args.pathOut)
    duplicateAnnotation(filePath = args.filePath, 
                        pathOut = args.pathOut)

if __name__=="__main__":
    main()
