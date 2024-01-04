import grpc
from google.protobuf.empty_pb2 import Empty

import door_pb2
import door_pb2_grpc


def run_client(events):
    channel = grpc.insecure_channel('localhost:50051')
    stub = door_pb2_grpc.DoorStub(channel)

    # Add code to call RPCs
    for event in events:
        response = stub.ProcessEvent(door_pb2.Event(event=event))
        print(response.message)

    # print current state
    print("Current state: ", stub.GetCurrentState(Empty()).current_state)



if __name__ == '__main__':
    events = ["OP", "OP", "CL", "OP"]
    run_client(events)
