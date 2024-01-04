import time
from concurrent import futures

import grpc
from google.protobuf.empty_pb2 import Empty

import door_pb2
import door_pb2_grpc


class FiniteStateMachine:
    def __init__(self, transitions, initial):
        self.transitions = transitions
        self.current = initial

    def getCurrentState(self):
        return self.current
    
    def run(self, event):
        if event in self.transitions[self.current]:
            self.current = self.transitions[self.current][event]
            return True
        return False
    

transitions = {
    "closed": {"OP": "opening"},
    "opening": {"OP": "opened"},
    "opened": {"CL": "closing"},
    "closing": {"CL": "closed", "OP":"opening"},
}

class DoorServicer(door_pb2_grpc.DoorServicer):
    def __init__(self, fsm):
        self.fsm = fsm

    # Add code to implement RPCs
    def ProcessEvent(self, request, context):
        if self.fsm.run(request.event):
            return door_pb2.Response(message = request.event + " event processed")
        else:
            return door_pb2.Response(message = "Invalid event")

    def GetCurrentState(self, request, context):
        return door_pb2.CurrentStateResponse(current_state=self.fsm.getCurrentState())

def serve():
    fsm = FiniteStateMachine(transitions=transitions, initial="closed")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    door_pb2_grpc.add_DoorServicer_to_server(
        DoorServicer(fsm), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(None)

if __name__ == '__main__':
    serve()
