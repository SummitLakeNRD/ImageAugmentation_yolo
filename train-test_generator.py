import os
import argparse
import random

def outputFiles(training_data, training_percent, prefix_dir):
    image_list = []
    for file in os.listdir(training_data):
        if file.endswith('.txt'):
            continue
        image_list.append(file)
    total_images = len(image_list)
    random.shuffle(image_list)
    training_data_total = round(total_images*training_percent)
    testing_data_total = total_images - training_data_total
    training_data_list = image_list[testing_data_total:]
    testing_data_list = image_list[:testing_data_total]
    

    with open('train.txt', 'w') as f:
        for data in training_data_list:
            filename = prefix_dir+data
            f.write(filename+'\n')

    with open('test.txt', 'w') as k:
        for data in testing_data_list:
            filename = prefix_dir+data
            k.write(filename+'\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('training_data', type=str, help='path/to/training/data')
    parser.add_argument('training_percent', type=float, default=0.80, help='percentage of data for training (ex 0.80)')
    parser.add_argument('prefix_dir', type=str, help='image/prefix/')
    args = parser.parse_args()
    outputFiles(training_data=args.training_data, 
                training_percent=args.training_percent,
                prefix_dir=args.prefix_dir)

if __name__ == '__main__':
    main()