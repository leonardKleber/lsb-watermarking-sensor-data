from engine import TemperatureEngine


if __name__ == '__main__':
    scratchpad = ['58', '01', '4b', '46', '7f', 'ff', '08', '10', 'f9']

    temp = TemperatureEngine(scratchpad)
    print(temp.read_temperature())