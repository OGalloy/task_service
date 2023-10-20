#db connection

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.schema import Task
from sqlalchemy import select


class DB_connection:
    def __init__(self, db_name = "db/db_ads.sqlite"):
        self.engine = create_engine(f"sqlite:///{db_name}", echo =True)

    def insert(self, task_id, desc):
        with Session(self.engine) as session:
            newtask = Task(task_id=task_id, description=desc)
            session.add_all([newtask])
            session.commit()

    def select_all_tasks(self):
        data = []
        with Session(self.engine) as session:
    	    stmt = select(Task)
    	    for task in session.scalars(stmt):
    		    data.append(task.description)
        return data



if __name__ == "__main__":
	db = DB_connection()
	#db.insert(1, "desc1")
	db.select_desc()

