import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///tasks.db")

# Init DB
db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL, status TEXT DEFAULT 'Pending')")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    # Grab data
    try:
        tasks = db.execute("SELECT * FROM tasks ORDER BY id DESC")
        return render_template("index.html", tasks=tasks)
    except Exception as e:
        print(f"Error fetching tasks: {e}") # Debugging print
        flash("Something went wrong loading your list.")
        return render_template("index.html", tasks=[])

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        content = request.form.get("task")
        
        # Human fix: strip whitespace to prevent "   " empty tasks
        if not content or not content.strip(): 
            flash("You can't add an empty task!")
            return redirect("/add")
            
        try:
            db.execute("INSERT INTO tasks (task) VALUES (?)", content.strip())
            print(f"User added task: {content}") # Debugging trace
            flash("Success! Added to your list.")
            return redirect("/")
        except:
            flash("Database error. Try again.")
            return redirect("/add")
    
    return render_template("add.html")

@app.route("/complete", methods=["POST"])
def complete():
    id_to_update = request.form.get("id")
    
    if id_to_update:
        db.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", id_to_update)
        flash("Marked as done. Good job!")
    
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    task_id = request.form.get("id")
    
    if task_id:
        # Check if it actually deleted anything (Human logic)
        result = db.execute("DELETE FROM tasks WHERE id = ?", task_id)
        if result: 
            flash("Got it! Task removed from list.")
        else:
            flash(" weird... that task didn't exist.")
            
    return redirect("/")