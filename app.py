from flask import Flask,render_template, request, redirect, url_for

app = Flask(__name__,template_folder='templates')

tasks = []


@app.route('/')#An app instance 
def home():
    return render_template("index.html",tasks = tasks)


#Creating a function for a new task
@app.route('/add_task',methods = ['POST'])
def create_task():
    task = request.form.get('task')
    tasks.append(task)
    return redirect (url_for('home'))


@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect (url_for('home'))




if __name__ =="__main__":#activating the debug mode 
    app.run(debug=True)