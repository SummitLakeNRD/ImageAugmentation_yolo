import cv2
import os
import argparse

def convertToFrames(video_path, output_path):

    for video in os.listdir(video_path):
        frame_counter = 0
        cap = cv2.VideoCapture(video_path+video)
        frame_prefix = video.split('.')[0]
        while True:
            grabbed, frame = cap.read()
            if not grabbed:
                break
            frame_counter+=1
            filename = output_path+frame_prefix+'_'+str(frame_counter)+'.png'
            frame = cv2.resize(frame, (416,416))
            cv2.imwrite(filename, frame)
        print('done with the video')
    print('finalized generating images from video directory, now go away')
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('video_file', type=str, help= 'path/to/video/files')
    parser.add_argument('output_path', type=str, help= 'output/path/to/generated/images')
    args = parser.parse_args()
    convertToFrames(video_path = args.video_file, output_path = args.output_path)

if __name__ == '__main__':
    main()