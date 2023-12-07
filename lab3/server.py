import grpc
from concurrent import futures
import tasks_pb2
import tasks_pb2_grpc

class TaskService(tasks_pb2_grpc.TaskServiceServicer):
    def __init__(self):
        self.tasks = []

    def CreateTask(self, request, context):
       # Generate a unique ID (you might use a library like UUID in a real-world scenario)
        new_id = str(len(self.tasks) + 1)
        request.id = new_id

        # Add the new task to the list
        self.tasks.append(request)

        return request

    def GetTask(self, request, context):
        # Implement logic to retrieve a task by its ID and return it.
        pass

    def UpdateTask(self, request, context):
        # Implement logic to update an existing task and return the updated task.
        pass

    def DeleteTask(self, request, context):
        # Implement logic to delete a task by its ID and return the result.
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tasks_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
