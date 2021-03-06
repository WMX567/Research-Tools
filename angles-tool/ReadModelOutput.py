"""
Read CNN results from txt files
wumengxi@umich.edu
"""
import os

def read_model_output(input_file):
    X, Y, video_frames = ([] for i in range(3))
    file = open(input_file, encoding='utf-8', errors='replace')
    lines = [line.strip('\n') for line in file]
    lines.pop(0)
    for line in lines:
        line = line.split()
        image_name = line[0]
        video_frames.append([int(image_name[3:-4])])
        line.pop(0)
        values = [float(s) for s in line if s != '']
        row_X, row_Y = ([] for i in range(2))
        for i in range(len(values)):
            if i % 2 == 0:
                row_X.append(values[i])
            else:
                row_Y.append(values[i])
        X.append(row_X)
        Y.append(row_Y)
    return X, Y, video_frames


def modify_filename(input_file):
    input_file = input_file.replace('FinalSkeleton_', '', 1)
    input_file = input_file.replace('Diag_', '', 1)
    input_file = input_file.replace('Right_', '', 1)
    input_file = input_file.replace('Left_', '', 1)
    input_file = input_file.replace('NoTape_','', 1)
    input_file = input_file.replace('.txt','', 1)
    return input_file

