import random
import time

def learn_normal_heart_rate():
    print("Learning patient's normal heart rate...")
    samples = []
    for i in range(20):
        hr = random.randint(70, 90)
        samples.append(hr)
        time.sleep(0.1)
    avg_hr = sum(samples) / len(samples)
    print(f"Normal Heart Rate Learned: {avg_hr:.2f} BPM\n")
    return avg_hr

def get_location():
    latitude = 10.7905
    longitude = 78.7047
    return latitude, longitude

def send_emergency_alert(current_hr, location):
    print("\n🚨 EMERGENCY ALERT TRIGGERED 🚨")
    print(f"Abnormal Heart Rate Detected: {current_hr} BPM")
    print(f"Patient Location: {location}")
    print("Alert sent to Hospital and Family")
    print("Ambulance Dispatched!\n")

def monitor_heart_rate(normal_hr):
    print("Monitoring heart rate...\n")
    while True:
        time.sleep(2)
        current_hr = random.randint(60, 140)
        print(f"Current Heart Rate: {current_hr} BPM")
        if current_hr > normal_hr + 30 or current_hr < normal_hr - 20:
            location = get_location()
            send_emergency_alert(current_hr, location)
            break

normal_hr = learn_normal_heart_rate()
monitor_heart_rate(normal_hr)
