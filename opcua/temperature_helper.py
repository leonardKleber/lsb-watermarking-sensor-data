def temp_data_to_list(temp_data: str):
    temp_list = []
    temp_list.append(temp_data[0] + temp_data[1])
    temp_list.append(temp_data[3] + temp_data[4])
    temp_list.append(temp_data[6] + temp_data[7])
    temp_list.append(temp_data[9] + temp_data[10])
    temp_list.append(temp_data[12] + temp_data[13])
    temp_list.append(temp_data[15] + temp_data[16])
    temp_list.append(temp_data[18] + temp_data[19])
    temp_list.append(temp_data[21] + temp_data[22])
    temp_list.append(temp_data[24] + temp_data[25])
    return temp_list


def temp_data_to_string(temp_data: list):
    temp_string = ''
    for i in temp_data:
        temp_string = temp_string + i + ' '
    temp_string = temp_string + ': crc=' + temp_data[8] + ' YES'
    return temp_string