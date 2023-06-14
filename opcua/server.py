import sys
import json
import time
from opcua import ua, Server
from temperature import TemperatureEngine
from temperature_helper import temp_data_to_list, temp_data_to_string


sys.path.insert(0, "..")


if __name__ == "__main__":
    # Set up server.
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)
    
    # Set up API object with temperature data variable.
    objects = server.get_objects_node()
    api = objects.add_object(idx, 'API')
    temp_data = api.add_variable(idx, 'TemperatureData', '')
    temp_data.set_writable()
    
    # Get sample dataset from file.
    f = open('sample_dataset.json', 'rb')
    sample_dataset = json.load(f)
    f.close()
    
    # Start the server.
    server.start()
    try:
        # Update the current temperature data every 1 seconds.
        counter = 0
        while True:
            counter = counter + 1
            if counter == 1000:
                counter = 0
            else:
                # Get current sample and convert it to list.
                current_sample = sample_dataset['results'][counter][0]
                scratchpad = temp_data_to_list(current_sample)
                
                # Insert watermark.
                watermark = '1'
                temperature = TemperatureEngine(scratchpad)
                temperature.watermark_integer(watermark)
                
                # Send temperature string to client.
                temp_data.set_value(temp_data_to_string(temperature.scratchpad))
            time.sleep(1)
    finally:
        server.stop()