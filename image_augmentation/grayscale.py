import cv2
import os
import shutil
import argparse

def grayscaleImages(filePath,pathOut):      
    for filename in os.listdir(filePath):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            image_path = filePath + filename
            image_pathOut = pathOut+'grayscale_'+filename
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(image_pathOut, gray)
            continue
        else:
            continue
    print('Images converted to grayscale.')

def duplicateAnnotation(filePath,pathOut):
    for filename in os.listdir(filePath):
        if "classes" in filename:
            continue
        if filename.endswith('.txt'):
            shutil.copy(filePath+filename, pathOut+filename)
            os.rename(pathOut+filename, pathOut+'grayscale_'+filename)
            continue
        else:
            continue
    print('Annotation files duplicated.')

def main():
    # use example: 'python grayscale.py path/to/images/ empty/image/directory/'
    parser = argparse.ArgumentParser()
    parser.add_argument('filePath', type=str, help='path/to/images/')
    parser.add_argument('pathOut', type=str, help='empty/image/directory/')
    args = parser.parse_args()
    grayscaleImages(filePath = args.filePath, pathOut = args.pathOut)
    duplicateAnnotation(filePath = args.filePath,pathOut = args.pathOut)
        
if __name__ == '__main__':
	main()


