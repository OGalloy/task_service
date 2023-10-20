from sqlalchemy import create_engine
from schema import BaseClass, Task
from sqlalchemy import insert
from sqlalchemy import text

engine = create_engine("sqlite:///db_ads.sqlite", echo =True)
BaseClass.metadata.create_all(engine)
