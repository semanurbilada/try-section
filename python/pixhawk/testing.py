from pymavlink import mavutil
import time

master = mavutil.mavlink_connection('/dev/ttyTHS1', baud=115200)

print("Waiting for heartbeat...")
master.wait_heartbeat()
print("Heartbeat received!")

# Function to send RC override commands
def send_rc_override(throttle, steering):
    """
    Sends RC override commands to control throttle and steering.
    Args:
    - throttle: Value for throttle (1100-1900; 1500 for neutral)
    - steering: Value for steering (1100-1900; 1500 for neutral)
    """
    master.mav.rc_channels_override_send(
        master.target_system,  # Target system
        master.target_component,  # Target component
        steering,   # Channel 1 (Steering)
        1500,       # Channel 2 (Neutral if unused)
        throttle,   # Channel 3 (Throttle)
        1500,       # Channel 4 (Neutral if unused)
        0, 0, 0, 0  # Channels 5-8 (Optional)
    )

# Control sequence
print("Running motors...")
try:
    # Move forward
    send_rc_override(1600, 1500)  # Forward with neutral steering
    time.sleep(3)

    # Turn right
    send_rc_override(1600, 1600)  # Forward with right steering
    time.sleep(3)

    # Stop
    send_rc_override(1500, 1500)  # Neutral throttle and steering
    time.sleep(1)

except KeyboardInterrupt:
    # Ensure motors stop on exit
    send_rc_override(1500, 1500)
    print("Stopped motors.")

print("Done!")