from pydantic_ai import Agent
from tools.task_tools import createTask, updateTaskToComplete, getTask, getTasks
from dotenv import load_dotenv
import sys
load_dotenv()

SYSTEM_PROMPT = """
A helpful AI Agent that will help you list tasks, create task, get task details and update a task in asana.
You will be given a brief description of what user want to do, you need to create a task with name and description using createTask tool.
Incase you are to asked to get task details try to list all tasks and match with which task id it matches a description or name, then get task with task id.
Incase you are asked to update a task, list all tasks and match with which task id it matches description or name, then update task with taskid
"""
agent = Agent(model="openai:gpt-4o",
              tools=[createTask, updateTaskToComplete, getTask, getTasks], )


def run_sync(prompt: str):
    result = agent.run_sync(prompt)
    return result.output


if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    print(run_sync(prompt))
