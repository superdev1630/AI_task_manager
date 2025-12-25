from services.tasks_service import TasksService

tasksService = TasksService()


def getTasks():
    """Getting all tasks to you"""
    print("Calling getTasks tool")
    return tasksService.getTasks()


def getTask(taskId: str):
    """to get task detail for a task id"""
    print("Calling getTask tool")
    return tasksService.getTask(taskid=taskId)


def createTask(name: str, description: str):
    """create task with name and description"""
    print("Calling createTask tool")
    return tasksService.createTask(name, description=description)


def updateTaskToComplete(taskId: str):
    """Update the task to complete status"""
    print("Calling updateTaskToComplete tool")
    return tasksService.updateTask(taskid=taskId)
