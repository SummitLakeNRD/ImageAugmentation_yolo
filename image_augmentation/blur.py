import cv2
import os
import shutil
import argparse

ksize = (4,4) #good value for 416x416 yolo images

def blurImages(filePath,pathOut):      
    for filename in os.listdir(filePath):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            image_path = filePath + filename
            image_pathOut = pathOut+'blur_'+filename
            image = cv2.imread(image_path)
            blur = cv2.blur(image, ksize)
            cv2.imwrite(image_pathOut, blur)
            continue
        else:
            continue
    print('Images blurred.')

def duplicateAnnotation(filePath,pathOut):
    for filename in os.listdir(filePath):
        if "classes" in filename:
            continue
        if filename.endswith('.txt'):
            shutil.copy(filePath+filename, pathOut+filename)
            os.rename(pathOut+filename, pathOut+'blur_'+filename)
            continue
        else:
            continue
    print('Annotation files duplicated.')

def main():
    # use example: 'python blur.py path/to/images/ empty/image/directory/'
    parser = argparse.ArgumentParser()
    parser.add_argument('filePath', type=str, help='path/to/images/')
    parser.add_argument('pathOut', type=str, help='empty/image/directory/')
    args = parser.parse_args()
    blurImages(filePath = args.filePath, pathOut = args.pathOut)
    duplicateAnnotation(filePath = args.filePath,pathOut = args.pathOut)
        
if __name__ == '__main__':
	main()


