import os
import json
from datetime import datetime
class TaskManager:
    def __init__(self,Taskid,Desc,status="To do"):
        self.Taskid = Taskid
        self.Desc =Desc
        self.status =status #default value is "To do"
        self.createdAt=datetime.now()
        self.updatedAt = datetime.now()
        self.tasks = []  # List to store tasks
     
    def Update_Task(self,newTaskid,newdesc):
        self.Taskid=newTaskid
        self.desc=newdesc
        self.updatedAt=datetime.now()
        print(f"Created at{self.createdAt}")
        print(f"Changed at{self.updatedAt}")

    def add_Task(self,Desc,status):
        self.Taskid += 1
        self.Desc =Desc
        self.createdAt=datetime.now()
        self.updatedAt = datetime.now()
        new_task = TaskManager(self.Taskid,self.desc)
        self.tasks.append(new_task)
    
    def delet_Task(self,Taskid,task):
        if not any(task.Taskid == Taskid for task in self.tasks):
            print("This task does not exist, sir!")
        else:
            self.tasks.remove(task)
    
    def update_status(self,new_status):
        #Display the list of taskes for the user , to chose witch status of task he would change
        for task in self.tasks:
            print(f"Id {task.Taskid}, Description {task.Desc}, Status {task.status}")
        task_id =int(input("enter the ID of the task you want to udpate"))
        The_right_task = next((task for task in self.tasks if task.Taskid == task_id), None)
        if The_right_task:
            status_ch ={
            1:  "To do",
            2:  "in progres",
            3:  "Done"
        }
            print("Choose a status:")
            for key, value in status_ch.items():
                    print(f"{key}: {value}")
            id_status = int(input("Choose a status (1 to 3): "))        
            match id_status:
                case 1:
                    print("your status its 'to do' keep working !!")
                    The_right_task.status = "To do"
                case 2:
                    print("your status its 'in progress' keep working !!")
                    The_right_task.status = "in progres"
                case 3:
                    print("your status its 'done' congratulation !!")
                    The_right_task.status = "Done"
                case _:
                    print("This choice does not exist !")
            The_right_task.updatedAt = datetime.now()  # Update timestamp
        else:
            print("Task not found!")
    def Alltasks(self): #To return all the tasks
        return self.tasks
    
    def TasksDone(self):
        Task_Done = [task for task in self.tasks if task.status == "Done"]
        return Task_Done
