from services.tasks_service import TasksService
import time

taskService = TasksService()


def createTasks():
    print("Creating dummy task 3")
    res = taskService.createTask("dummy task 3", "a dummy sample task three")
    print("OUTPUT", res)
    print("------------------------------------XXXXXXXXXX--------------------------------------")
    time.sleep(1)
    print("Creating dummy task 4")
    res = taskService.createTask("dummy task 4", "a dummy sample task four")
    print("OUTPUT", res)
    print("------------------------------------XXXXXXXXXX--------------------------------------")


def getTasks():
    print("Getting all tasks")
    time.sleep(1)
    res = taskService.getTasks()
    print("OUTPUT", res)
    print("------------------------------------XXXXXXXXXX--------------------------------------")


def updateTask(taskid: str):
    print(f"Updating a task {taskid} completion")
    time.sleep(1)
    res = taskService.updateTask(taskid=taskid)
    print("OUTPUT", res)
    print("------------------------------------XXXXXXXXXX--------------------------------------")


# print(taskService.getWorkflows())
# createTasks()
getTasks()
updateTask("1212055834231058")
updateTask("1212055833717485")
# print(taskService.getUsers())
