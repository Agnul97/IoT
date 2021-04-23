# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import zmq
import pandas as pd

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")

    data = pd.read_csv('http://iot.ee.surrey.ac.uk:8080/datasets/traffic/traffic_feb_june/trafficData158324.csv')
    print(data)
    exit(1)
    print("modPortatile")
    # Start your result manager and workers before you start your producers
    for num in range(20000):
        work_message = { 'num' : num }
        zmq_socket.send_json(work_message)
        time.sleep(1)
producer()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
