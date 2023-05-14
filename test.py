from engine import TemperatureEngine


if __name__ == '__main__':
    scratchpad_01 = ['58', '01', '4b', '46', '7f', 'ff', '08', '10', 'f9']
    scratchpad_02 = ['bd', '01', '4b', '46', '7f', 'ff', '03', '10', 'ff']

    # Test LSB integer watermark.
    temp_01 = TemperatureEngine(scratchpad_01)
    print(temp_01.read_temperature())
    temp_01.watermark_integer('0')
    print(temp_01.read_temperature())

    temp_04 = TemperatureEngine(scratchpad_02)
    print(temp_04.read_temperature())
    temp_04.watermark_integer('0')
    print(temp_04.read_temperature())

    # Test LSB decimal watermark.
    temp_02 = TemperatureEngine(scratchpad_01)
    print(temp_02.read_temperature())
    temp_02.watermark_decimal('1')
    print(temp_02.read_temperature())

    temp_03 = TemperatureEngine(scratchpad_02)
    print(temp_03.read_temperature())
    temp_03.watermark_decimal('0')
    print(temp_03.read_temperature())