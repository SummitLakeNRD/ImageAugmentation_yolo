import cv2
import os
import argparse

def convertToFrames(dir_path, output_path):
    for video in os.listdir(dir_path):
        frame_counter = 0
        video_path = os.path.join(dir_path, video)
        print(video_path)
        cap = cv2.VideoCapture(video_path)
        frame_prefix = video.split('.')[0]
        while True:
            grabbed, frame = cap.read()
            if not grabbed:
                break
            frame_counter+=1
            if frame_counter % 10 == 0:
                filename = os.path.join(output_path) + '/' + frame_prefix + '_' + str(frame_counter) + '.png'
                print(filename)
                #frame = cv2.resize(frame, (1032,1032))
                cv2.imwrite(filename, frame)
            else:
                continue
        print('done with the video')
    print('finalized generating images from video directory, now go away')
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('video_file', type=str, help= 'path/to/video/files')
    parser.add_argument('output_path', type=str, help= 'output/path/to/generated/images')
    args = parser.parse_args()
    convertToFrames(dir_path = args.video_file, output_path = args.output_path)

if __name__ == '__main__':
    main()
