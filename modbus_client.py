from pyModbusTCP.client import ModbusClient
import time
import os

def send_message(plc_ip, port, register, value):
    print(plc_ip)
    print(port)

    client = ModbusClient(host=plc_ip, port=port)
    open_response = client.open()
    
    status = 0
    if open_response:
        client.write_single_register(register, value)
        time.sleep(100)
        client.close()
        status = 0
    else:
        status = 1

    return status
