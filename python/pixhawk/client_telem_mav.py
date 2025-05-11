import os
from pymavlink import mavutil
from dotenv import load_dotenv

# load env variables
load_dotenv()

# Connect to Pixhawk via MAVLink
connection = mavutil.mavlink_connection("SERIAL_PORT", baud="BAUD_RATE")

# Send detected object to another vehicle, forwarded with RFD900 via MAVLink
def sendInfo(object_name):
    message = f"Detected object:{object_name}"
    print(f"Sending message: {message}")

    try:
        connection.mav.statustext_send(
            mavutil.mavlink.MAV_SEVERITY_NOTICE, message.encode('utf-8')
        )
    except Exception as e:
        print("Error sending MAVLink data:", e)

# Sending detected information (Ex: deneme)
sendInfo("deneme")