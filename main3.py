import zmq
import pprint

def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:5558")
    collecter_data = {}
    while True:
        result = results_receiver.recv_json()
        pprint.pprint(result)

result_collector()