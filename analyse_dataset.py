import json
import math
from engine import TemperatureEngine


def format_dataset(dataset: dict):
    formatted_dataset = []
    current_set = []
    for i in dataset['results']:
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


def read_temperatures(formatted_dataset: list):
    temperatures = []
    for i in formatted_dataset:
        temp = TemperatureEngine(i)
        temperatures.append(temp.read_temperature())
    return temperatures


def std_deviation(temperatures: list):
    n = len(temperatures)
    mean = 0.0
    for i in temperatures:
        mean = mean + i
    mean = mean / n
    variance = 0.0
    for i in temperatures:
        value = i - mean
        value = value * value
        variance = variance + value
    variance = variance / (n - 1)
    std_deviation = math.sqrt(variance)
    return std_deviation


if __name__ == '__main__':
    # Get sample dataset from file.
    f = open('results.json', 'rb')
    sample_dataset = json.load(f)
    f.close()
    # Measure the standard deviation of the sample dataset.
    form = format_dataset(sample_dataset)
    temp = read_temperatures(form)
    print('Standard Deviation of dataset without watermark:      ' + str(std_deviation(temp)))
    # Measure the standard deviation of the sample dataset with ineteger watermark.
    form_int = format_dataset(sample_dataset)
    t_int = []
    for i in form_int:
        temp_int = TemperatureEngine(i)
        temp_int.watermark_integer('1')
        t_int.append(temp_int.read_temperature())
    print('Standard Deviation of dataset with capacity 1  integer watermark: ' + str(std_deviation(t_int)))
    # Measure the standard deviation of the sample dataset with decimal watermark.
    form_dec = format_dataset(sample_dataset)
    t_dec = []
    for i in form_dec:
        temp_dec = TemperatureEngine(i)
        temp_dec.watermark_decimal('1')
        t_dec.append(temp_dec.read_temperature())
    print('Standard Deviation of dataset with capacity 1 decimal watermark: ' + str(std_deviation(t_dec)))

    dataset_0 = format_dataset(sample_dataset)
    temperatures_0 = []
    counter = 0
    for i in dataset_0:
        temp_dec = TemperatureEngine(i)
        if counter % 2 == 0:
            temp_dec.watermark_decimal('1')
        temperatures_0.append(temp_dec.read_temperature())
        counter = counter + 1
    print('Standard Deviation of dataset with capacity 0.5 decimal watermark: ' + str(std_deviation(temperatures_0)))

    dataset_1 = format_dataset(sample_dataset)
    temperatures_1 = []
    counter = 0
    for i in dataset_1:
        temp_int = TemperatureEngine(i)
        if counter % 2 == 0:
            temp_int.watermark_integer('1')
        temperatures_1.append(temp_int.read_temperature())
        counter = counter + 1
    print('Standard Deviation of dataset with capacity 0.5 integer watermark: ' + str(std_deviation(temperatures_1)))

    dataset_2 = format_dataset(sample_dataset)
    temperatures_2 = []
    counter = 0
    for i in dataset_2:
        temp_int = TemperatureEngine(i)
        if counter % 4 == 0:
            temp_int.watermark_integer('1')
        temperatures_2.append(temp_int.read_temperature())
        counter = counter + 1
    print('Standard Deviation of dataset with capacity 0.25 integer watermark: ' + str(std_deviation(temperatures_2)))

    dataset_3 = format_dataset(sample_dataset)
    temperatures_3 = []
    counter = 0
    for i in dataset_3:
        temp_int = TemperatureEngine(i)
        if counter % 10 == 0:
            temp_int.watermark_integer('1')
        temperatures_3.append(temp_int.read_temperature())
        counter = counter + 1
    print('Standard Deviation of dataset with capacity 0.1 integer watermark: ' + str(std_deviation(temperatures_3)))