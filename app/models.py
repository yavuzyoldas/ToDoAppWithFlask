from database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey,String,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime
from datetime import datetime

class Todo(Base):

    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)

    todos_title = Column(String(80))
    todos_content = Column(Text)
    todos_complete = Column(Boolean)
    def __init__(self,todos_title,todos_content,todos_complete):
        self.todos_title = todos_title
        self.todos_content = todos_content
        self.todos_complete = todos_complete
     