import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = 'database'
port = '5432'
engine = create_engine('postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)) 

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    if not engine.dialect.has_table(engine, "todos"):  # If table don't exist, Create.
        print("creating tables first time.............")
        import models
        Base.metadata.create_all(bind=engine)
    else:
        print("tables are already created.............")



def create_todo(title,content):
     from models import Todo
     complete = False
     new_todo = Todo(todos_title=title,todos_content=content,todos_complete=complete)
     db_session.add(new_todo)
     db_session.commit()

def get_all_todos():
    from models import Todo
    all_todos = db_session.query(Todo)
    return all_todos    

def delete_todo(id):
    from models import Todo
    todo = db_session.query(Todo).filter_by(id=id).first()
    db_session.delete(todo)
    db_session.commit()  

def update_todo(id):
    from models import Todo    
    todo = db_session.query(Todo).filter_by(id=id).first()
    if(todo.todos_complete == False):
       todo.todos_complete = True
    else:
       todo.todos_complete = False
    db_session.commit()
    
def todo_detail(id):
    from models import Todo    
    todo = db_session.query(Todo).filter_by(id=id).first()    
    return todo 





            
    
    
    
