import os
import math
import random
import shutil
from argparse import ArgumentParser


def moveTrainFiles(sourceFiles, trainDest, trainPercentage):
    files = os.listdir(sourceFiles)
    no_of_files = math.floor(len(files) * trainPercentage)

    for file_name in random.sample(files, no_of_files):
        shutil.move(os.path.join(sourceFiles, file_name), trainDest)
    print('Finished moving train files')


def moveTestFiles(sourceFiles, testDest):
    for file_name in os.listdir(sourceFiles):
        shutil.move(os.path.join(sourceFiles, file_name), testDest)
    print('Finished moving test files')


def main():
    parser = ArgumentParser()
    parser.add_argument('source', type=str, help='source files location')
    parser.add_argument('train_destination', type=str, help='training data file destination')
    parser.add_argument('test_destination', type=str, help='testing data file destination')
    parser.add_argument('--train_percentage', type=float, default=0.8)
    args = parser.parse_args()
    moveTrainFiles(args.source, args.train_destination, args.train_percentage)
    moveTestFiles(args.source, args.test_destination)


if __name__ == '__main__':
    main()