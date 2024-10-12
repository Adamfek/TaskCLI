import os
import json
from datetime import datetime
class TaskManager:
    def __init__(self,Taskid,Desc,status):
        self.Taskid = Taskid
        self.Desc =Desc
        self.createdAt=datetime.now()
        self.updatedAt = datetime.now()
        self.tasks = []  # List to store tasks
     
    def Update_Task(self,newTaskid,newdesc):
        self.Taskid=newTaskid
        self.desc=newdesc
        self.updatedAt=datetime.now()

    def add_Task(self,Desc,status):
        self.Taskid += 1
        self.Desc =Desc
        self.createdAt=datetime.now()
        self.updatedAt = datetime.now()
        new_task = TaskManager(self.Taskid,self.desc)
        self.tasks.append(new_task)
    
    def delet_Task(self,Taskid):
        if not any(task.Taskid == Taskid for task in self.tasks):
            print("This task does not exist, sir!")
        else:
            self.tasks.remove(task)
    
    def update_status(self,status):
        pass