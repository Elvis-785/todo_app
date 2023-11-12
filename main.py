from task_db import db, Qtask
#crud

def task_manager():
    choice=0
    while choice != 5:
        print("""
Welcome to your task manager, what would you like to do?
1.Add a task.
2.View your task.
3.Update your task.
4.Delete task.
5.Quit.
        """)
        choice=int(input())
        if choice==1:
            print("Adding tasks >>>")
            title=input("Enter the title: ")
            descr=input("Enter task description: ")
            start_time=input("Enter the starting time: ")
            end_time=input("Enter the ending time: ")
            Completion=False
            task= db.insert({"title":title,
                        "description":descr, 
                        "starting time":start_time, 
                        "Ending time": end_time, 
                        "Completion":Completion})

        elif choice==2:
            print("View your tasks...")
            for task in db:
                print(task)
        elif choice==3:
            key=input("New task update: ")
            value=input("New value update: ")
            id=int(input("Enter task id: "))
            db.update({key:value}, doc_ids=[id])
        elif choice==4:
            
            db.truncate()
            




    print("Exit program")

if __name__=="__main__":
    task_manager()
        