from flask import Flask,render_template,request,redirect,url_for     
from database import init_db
from database import get_all_todos,create_todo,delete_todo,update_todo,todo_detail

app = Flask(__name__)


@app.route("/")
def index():
    todos = get_all_todos()
    return render_template("index.html",todos = todos)

@app.route("/add",methods = ["POST"])
def addTodo():
   title = request.form.get("title")
   content = request.form.get("content")
   create_todo(title=title,content=content)
   return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def updateTodo(id):
    update_todo(id)  
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):
    delete_todo(id)
    return redirect(url_for("index"))

@app.route("/detail/<string:id>")
def detailTodo(id):
     todo = todo_detail(id)
     return render_template("detail.html",todo =todo)


if __name__ == '__main__':
    init_db()
    app.run(debug=True,host='0.0.0.0', port=5802)

