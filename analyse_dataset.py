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
    f = open('sample_dataset.json', 'rb')
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
    print('Standard Deviation of dataset with integer watermark: ' + str(std_deviation(t_int)))
    # Measure the standard deviation of the sample dataset with decimal watermark.
    form_dec = format_dataset(sample_dataset)
    t_dec = []
    for i in form_dec:
        temp_dec = TemperatureEngine(i)
        temp_dec.watermark_decimal('1')
        t_dec.append(temp_dec.read_temperature())
    print('Standard Deviation of dataset with decimal watermark: ' + str(std_deviation(t_dec)))