from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "key456"
DB_FILE = "users.db"

def get_db():
    return sqlite3.connect(DB_FILE)

def init_db():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    conn = get_db()
    conn.execute("""CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, user TEXT UNIQUE, password TEXT)""")
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def start():
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name, user, password = request.form.get("name"), request.form.get("user"), request.form.get("password")
        conn = get_db()
        try:
            conn.execute("INSERT INTO users(name, user, password) VALUES (?, ?, ?)", (name, user, password))
            conn.commit()
            conn.close()
            return redirect("/login")
        except sqlite3.IntegrityError:
            conn.close()
            return render_template("register.html", error="Username already exists")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user, password = request.form.get("user"), request.form.get("password")
        conn = get_db()
        data = conn.execute("SELECT * FROM users WHERE user=? AND password=?", (user, password)).fetchone()
        conn.close()
        if data:
            session["user"], session["name"] = data[2], data[1]
            return redirect("/dashboard")
        return render_template("login.html", error="Wrong username or password")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", name=session.get("name", "User"), username=session.get("user", ""))
    return redirect("/login")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)