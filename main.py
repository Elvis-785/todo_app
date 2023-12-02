from tinydb import TinyDB, Query
db = TinyDB('todo.json')

def addTask():
    print('Adding task>>>')
    title = input('Enter task title: ')
    descr = input('Enter task description: ')
    start_time = input('Enter starting time: ')
    end_time = input('Enter task ending time: ')
    completion = False
    task = db.insert({'title': title,
                      'description':descr,
                      'starting time':start_time,
                      'Ending time':end_time,
                      'Completion':completion,
                      })
        
def viewTask():
    print('View your tasks...')
    for task in db:
        print(task)
    
def updateTask():
    key = input('New task update: ')
    value = input('New value update: ')
    id = int(input('Enter task id: '))
    return db.update({key:value}, doc_ids=[id])

def deleteTask():
    return db.truncate()

while True:
    user_input = input("""
What would you like to do?
1.Add a new task.
2.Look up task.
3.Update the task.
4.Delete task.
5.Quit.\n""")
    if user_input == '1':
        addTask()
    if user_input == '2':
        viewTask()
    if user_input == '3':
        updateTask()
    if user_input == '4':
        deleteTask()
    if user_input == ['q', 'Q']:
        print('Exiting')
        break
        