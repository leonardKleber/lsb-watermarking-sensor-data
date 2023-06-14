import sys
import time
from opcua import Client
from temperature import TemperatureEngine
from temperature_helper import temp_data_to_list, temp_data_to_string


sys.path.insert(0, "..")


if __name__ == "__main__":
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    try:
        client.connect()
        while True:
            # Set up connection to server variable.
            root = client.get_root_node()
            temp_data = root.get_child(["0:Objects", "2:API", "2:TemperatureData"])
            api = root.get_child(["0:Objects", "2:API"])

            # Recieve temperature string from server.
            temperature_string = temp_data.get_value()
            scratchpad = temp_data_to_list(temperature_string)

            # Verify the watermark.
            watermark = '0'
            temperature = TemperatureEngine(scratchpad)
            print('Watermark has been detected: ' + str(temperature.verify_watermark_integer(watermark)))

            time.sleep(1)
    finally:
        client.disconnect()