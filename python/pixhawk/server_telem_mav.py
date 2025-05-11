import os
from pymavlink import mavutil
from dotenv import load_dotenv

# load env variables
load_dotenv()

# Connect to Pixhawk via MAVLink
connection = mavutil.mavlink_connection("SERIAL_PORT", baud="BAUD_RATE")

# Receive detected object from another vehicle's Pixhawk, RFD900 via MAVLink
def receiveInfo():
    print("Listening for incoming information from...\n")

    while True:
        msg = connection.recv_match(type='STATUSTEXT', blocking=True)
        if msg:
            decoded_message = msg.text.decode('utf-8')
            if decoded_message.startswith("Detected object:"):
                detected_object = decoded_message.split(":")[1]
                print(f"Received detected object: {detected_object}")

if __name__ == "__main__":
    receiveInfo()