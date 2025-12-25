from services.base_http_client import BaseHTTPClient
from dotenv import load_dotenv
import os

load_dotenv()


class TasksService:
    def __init__(self):
        self.client = BaseHTTPClient(
            base_url=os.environ["ASANA_BASE_URL"], api_key=os.environ["ASANA_AUTH_TOKEN"])
        self.workspaceId = os.environ["WORKSPACE_ID"]
        self.userId = os.environ["USER_ID"]

    def createTask(self, name: str, description: str):
        body = {
            "name": name,
            "notes": description,
            "workspace": self.workspaceId,
            "assignee": self.userId
        }
        response = self.client.postCall("tasks", {"data": body})
        print("RESPONSE", response)
        data = {
            "name": response["data"]["name"],
            "created_at": response["data"]["created_at"],
            "gid": response["data"]["gid"]
        }
        return data

    def getTasks(self):
        response = self.client.getCall(
            f"tasks?workspace={self.workspaceId}&assignee={self.userId}")
        print("RESPONSE", response)
        data = response["data"]
        results = []
        for d in data:
            result = {
                "name": d["name"],
                "gid": d["gid"],
                "description": d.get("notes", "no note found"),
                "completed": d.get("completed", False)
            }
            results.append(result)

        return results

    def getTask(self, taskid: str):
        response = self.client.getCall(f"tasks/{taskid}")
        data = response["data"]
        result = {
            "name": data["name"],
            "gid": data["gid"],
            "description": data["notes"],
            "completed": data["completed"],
            "completedBy": data.get("created_by", {}).get("name", "Not Completed yet")
        }
        return result

    def updateTask(self, taskid: str):
        body = {
            "completed": True
        }
        response = self.client.putCall(f"tasks/{taskid}", {
            "data": body
        })
        data = {
            "name": response["data"]["name"],
            "created_at": response["data"]["created_at"],
            "gid": response["data"]["gid"],
            "completed": response["data"]["completed"]
        }
        return data

    def getWorkflows(self):
        response = self.client.getCall("workspaces")
        data = response["data"]
        results = []
        for d in data:
            result = {
                "gid": d["gid"],
                "name": d["name"],
                "resource_type": d["resource_type"]
            }
            results.append(result)
        return results

    def getUsers(self):
        response = self.client.getCall(f"users?workspace={self.workspaceId}")
        return response["data"]
