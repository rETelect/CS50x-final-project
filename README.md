# ✅ TaskMaster (Personal Productivity Web App)

## 📌 Project Overview
**TaskMaster** is a streamlined, user-centric web application designed for efficient daily task management. Built as a full-stack solution, it allows users to organize their lives by creating, tracking, and managing to-do lists in real-time.

---

## 🛠️ How It Works (The Technical Side)

### 🔌 Backend & Logic (Flask)
The core of the application runs on a **Flask** server (`app.py`), acting as the bridge between the user interface and the data layer. 
* **Dynamic Routing:** Managed various endpoints including `/` for the dashboard, `/add` for task creation, `/complete` for status updates, and `/delete` for record removal.
* **Input Validation:** Implemented server-side checks to prevent empty entries or invalid task lengths.

### 🗄️ Database Management (SQL)
Utilized **SQLite** with the `cs50` SQL library to handle persistent data storage.
* **Schema Design:** Structured a `tasks` table with fields for unique IDs, task descriptions, and status (Pending/Completed).
* **CRUD Operations:** Executed standard SQL commands (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) to maintain data integrity.

### 🎨 Frontend & UI (HTML/CSS)
* **Responsive Design:** Leveraged **Bootstrap** to ensure a seamless experience across mobile and desktop devices.
* **Jinja2 Templating:** Used to dynamically render database content into the HTML structure.

---

## 🧗 Challenges & Learning Journey
Every developer faces hurdles, and TaskMaster provided a significant learning curve:

* **Environment Configuration:** Setting up the development environment on Windows presented challenges with `pip` installations and Flask-to-DB connectivity. I overcame this through methodical troubleshooting of system environment variables.
* **Separation of Concerns:** Initially, I struggled with the architecture, accidentally embedding Python logic within HTML. I resolved this by restructuring the project into a proper **MVC (Model-View-Controller)** pattern, separating backend logic from frontend presentation.

---

## 💻 Technical Stack
* **Language:** `Python`, `SQL`, `HTML/CSS`, `JavaScript`
* **Framework:** `Flask`
* **Styling:** `Bootstrap`
* **Template Engine:** `Jinja2`
* **Database:** `SQLite`

---

## 📂 Project Structure
* `app.py`: Main Flask application and backend logic.
* `tasks.db`: SQLite database for persistent storage.
* `templates/`: 
    * `layout.html`: Base template with Bootstrap integration.
    * `index.html`: Main dashboard displaying the task list.
    * `add.html`: Interface for new task creation.
* `requirements.txt`: List of dependencies (Flask, cs50).

---

## 🙏 Credits & Acknowledgments
Special thanks to the educational resources that helped bridge my knowledge gaps:
* **Ghareeb Elshaikh:** For simplifying complex Flask backend logic.
* **Neso Academy:** For clear and foundational web programming tutorials.
