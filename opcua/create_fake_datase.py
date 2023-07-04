import json
import math
from temperature import TemperatureEngine
import random


def manipulte_dataset():
    # Load data_set
    f = open('results.json', 'rb')
    sample_dataset = json.load(f)
    f.close()

    # Format Dataset
    formatted_dataset = []
    current_set = []
    for i in sample_dataset['results']:
        current_set.append(i[0][0] + i[0][1])
        current_set.append(i[0][3] + i[0][4])
        current_set.append(i[0][6] + i[0][7])
        current_set.append(i[0][9] + i[0][10])
        current_set.append(i[0][12] + i[0][13])
        current_set.append(i[0][15] + i[0][16])
        current_set.append(i[0][18] + i[0][19])
        current_set.append(i[0][21] + i[0][22])
        current_set.append(i[0][24] + i[0][25])

        formatted_dataset.append(current_set)
        current_set = []

    # Insert Watermark
    watermarked_dataset = []
    for i in formatted_dataset:
        temp = TemperatureEngine(i)
        temp.double_watermark_decimal('1', '1')
        watermarked_dataset.append(temp.scratchpad)
    # INSERT DAKE DATA (30.0000 DEGREES) [0011110][0000]
    wrong_temp = ['86', '01', '4b', '46', '7f', 'ff', '0c', '10', 'f4']
    count = 0
    mani_set = []
    for i in watermarked_dataset:
        check = random.randint(0, 9)
        if check % 2 == 0:
            mani_set.append(wrong_temp)
            count = count + 1
        else:
            mani_set.append(i)
    print(str(count) + ' datapoints were altered')
    # Reformat the dataset
    dset = []
    for i in mani_set:
        dset.append([
            i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + i[3] + ' ' + i[4] + ' ' + i[5] + ' ' + i[6] + ' ' + i[7] + ' ' + i[8], []
        ])
    return dset


def format_dataset(dataset: dict):
    formatted_dataset = []
    current_set = []
    for i in dataset:
        current_set.append(i[0][0] + i[0][1])
        current_set.append(i[0][3] + i[0][4])
        current_set.append(i[0][6] + i[0][7])
        current_set.append(i[0][9] + i[0][10])
        current_set.append(i[0][12] + i[0][13])
        current_set.append(i[0][15] + i[0][16])
        current_set.append(i[0][18] + i[0][19])
        current_set.append(i[0][21] + i[0][22])
        current_set.append(i[0][24] + i[0][25])

        formatted_dataset.append(current_set)
        current_set = []
    return formatted_dataset


sample_dataset = manipulte_dataset()
formatted = format_dataset(sample_dataset)

#print(sample_dataset)
#print(formatted)


count = 0
for i in formatted:
    temp = TemperatureEngine(i)
    if temp.verify_double_watermark_decimal('1', '1') == True:
        count = count + 1

print(count)