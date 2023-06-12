import sys
import time
from opcua import Client
from temperature import TemperatureEngine


sys.path.insert(0, "..")


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


if __name__ == "__main__":
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    try:
        client.connect()
        while True:
            root = client.get_root_node()
            temp_data = root.get_child(["0:Objects", "2:API", "2:TemperatureData"])
            api = root.get_child(["0:Objects", "2:API"])
            current_temp_data = temp_data.get_value()
            temp_value = TemperatureEngine(temp_data_to_list(current_temp_data))
            #print(current_temp_data)
            #print(temp_data_to_list(current_temp_data))
            #print(read_temperature(current_temp_data))
            print(temp_value.read_temperature())
            time.sleep(1)
    finally:
        client.disconnect()