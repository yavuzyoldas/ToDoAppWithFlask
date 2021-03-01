from database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey,String,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime
from datetime import datetime

class Todo(Base): # Account Kit, Accelerate Kit etc
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.
    __tablename__ = 'todos'
    # We always need an id
    id = Column(Integer, primary_key=True)

    # A dessert has a name, a price and some calories:
    todos_title = Column(String(80))
    todos_content = Column(Text)
    todos_complete = Column(Boolean)
    def __init__(self,todos_title,todos_content,todos_complete):
        self.todos_title = todos_title
        self.todos_content = todos_content
        self.todos_complete = todos_complete

class User(Base): # it can be android, ios, flutter etc.
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.
    __tablename__ = 'users'
    # We always need an id
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    todo_id = Column(Integer, ForeignKey("todos.id"))
    kit = relationship("Todo", back_populates='users')
    created_date = Column(DateTime, default=datetime.utcnow)
    def __init__(self, name):
        self.name = name
        self.created_date = datetime.now() 
    


""" class Todo(db.Model):
   __tablename__ = "todos"
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(80))
   content = db.Column(db.Text)
   complete = db.Column(db.Boolean)"""       