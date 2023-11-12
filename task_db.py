from tinydb import TinyDB, Query
db = TinyDB("todo.json")
db.default_table_name="tasks"
Qtask=Query()