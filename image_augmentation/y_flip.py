from cgi import test
import cv2
import os
import shutil
import argparse

def flipImages(filePath, pathOut):
    for filename in os.listdir(filePath):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            image_path = filePath + filename
            image_pathout = pathOut + 'Yflip_' + filename
            image = cv2.imread(image_path)
            flipp = cv2.flip(image, 1)
            cv2.imwrite(image_pathout, flipp)
        else:
            continue
    print('Images successfully flipped along the horizontal axis')

def alterAnnotations(filePath, pathOut):
    for filename in os.listdir(filePath):
        textfile_path = filePath+filename
        outfile_path = pathOut+'Yflip_'+filename
        if 'classes' in filename:
            shutil.copy(filePath+filename, pathOut+filename)
            continue
        elif filename.endswith('.txt'):
            with open(textfile_path, 'r') as f:
                data = f.readlines()
            with open(outfile_path, 'w') as k:
                for line in data:
                    line = line.split(' ')
                    classVal = int(line[0])
                    xVal = float(line[1])
                    yVal = float(line[2])
                    width = float(line[3])
                    height = float(line[4])
                    new_xVal = round(1 - xVal, 6)
                    newLine = str(classVal)+' '+str(new_xVal)+' '+str(yVal)+' '+str(width)+' '+str(height)+'\n'
                    k.write(newLine)
        else:
            continue
    print('Annotation files successfully generated')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filePath', type=str, help='/path/to/images/')
    parser.add_argument('pathOut', type=str, help='/empty/image/directory/')
    args = parser.parse_args()
    flipImages(filePath=args.filePath, pathOut=args.pathOut)
    alterAnnotations(filePath=args.filePath, pathOut=args.pathOut)

if __name__ == '__main__':
    main()