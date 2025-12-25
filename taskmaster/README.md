# TaskMaster

#### Video Demo: <https://drive.google.com/file/d/1C4dBbPEmyOTbcrXPN5f-b4gYNOINW8IN/view?usp=sharing>

#### Description</insert>:

TaskMaster is a simple, easy-to-use website for managing your daily to-do lists. I built it with Python, Flask, SQL, and Bootstrap. You can add tasks, see what's still pending, mark things as done, and get rid of tasks you don't need anymore.

### How It Works 

The whole thing runs on a Flask server (`app.py`). This server acts like the middleman, talking between what you see on your screen and where your tasks are stored.

1.  **Database (SQL):**
    I used a SQLite database (`tasks.db`) to keep all your task info safe. Inside, there's a table called `tasks`. It has a number for each task (`id`), what the task is (`task`), and its status (it starts as 'Pending' and can be changed to 'Completed'). I used the `cs50` library's `SQL` tool to talk to the database.
    *   To add new tasks, I use `INSERT` commands.
    *   To show your task list, I use `SELECT` commands.
    *   When you finish a task, an `UPDATE` command changes its status.
    *   And to remove tasks, I use `DELETE` commands.

2.  **Backend (Flask):**
    The `app.py` file takes care of all the web page addresses:
    *   When you go to the main page (`/`), it grabs all your tasks from the database (newest ones first) and shows them to you on the `index.html` page. It also has a backup plan in case something goes wrong with the database.
    *   The `/add` page lets you create new tasks. You can't add an empty task or a super short one, though!
    *   `/complete` is just for updating a task's status to done without deleting it.
    *   `/delete` completely removes a task from your list.

3.  **Frontend (HTML/CSS):**
    The user interface is made with HTML pages that use Jinja2 to show your task data. I used Bootstrap to make everything look good and work well on phones and computers—like the top menu, tables, and buttons.
### My Story  Thanks    

This project was quite a challenge, especially figuring out how to make  (Python) talk to the face (HTML).

**What gave me the most trouble:**
Setting up everything on Windows was the hardest part. I ran into all sorts of problems with `pip` installs, computer settings, and getting Flask to connect to my database. I also messed up the file arrangement at first, putting Python code directly into my HTML, which just showed code instead of the website!

**How I got through it:**
I tackled these issues step by step: first fixing the file layout, then getting the necessary software installed, and finally writing the code bit by bit.

A big shoutout to two YouTube channels that really helped me out:
*   **Ghareeb Elshaikh:** His Flask explanations made the backend logic much simpler to grasp.
*   **Neso Academy:** Their tutorials are always clear and helped me learn web programming basics quickly.

### Files
*   `app.py`: This is the main program for the Flask server and database stuff.
*   `tasks.db`: This is where your tasks are stored.
*   `requirements.txt`: Lists what you need to install (`Flask`, `cs50`) to run the project.
*   `templates/layout.html`: The basic HTML page that links to Bootstrap and has the top menu.
*   `templates/index.html`: The main page where you see your task list.
*   `templates/add.html`: The page where you fill out the form to create new tasks.

Github/edx username:retelect
name:majd najeh