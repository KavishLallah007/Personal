from datetime import datetime, timedelta
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///school.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Display home page"""

    if not session.get("user_id"):
        return redirect("/login")
    else:
        # Get events for this month
        today = datetime.today()
        first_day = today.replace(day=1)
        last_day = first_day.replace(month=first_day.month+1) - timedelta(days=1)
        events = db.execute("SELECT * FROM events WHERE date BETWEEN ? AND ?", first_day.date(), last_day.date())

        return render_template("index.html", events=events)


@app.route("/calender")
def calender():
    """Display calender of activites and classes"""

    if not session.get("user_id"):
        return redirect("/login")
    else:
        events = db.execute("SELECT * FROM events")
        return render_template('calender.html', events=events)


@app.route("/event", methods=["GET", "POST"])
def event():
    """Display calender of activites and classes"""

    if not session.get("user_id"):
        return redirect("/login")
    else:
        user_id = session["user_id"]
        if request.method == "GET":
            return render_template("event.html")

        else:
            event_name = request.form.get("event_name")
            date = request.form.get("date")
            start_time = request.form.get("start_time")
            end_time = request.form.get("end_time")
            event_type = request.form.get("event_type")
            event_grade = request.form.get("grade")

            # Form entry validation
            if not event_name:
                return "Must provide Event name!"

            if not date:
                return "Must provide Date for event!"

            if not start_time:
                return "Must provide start time!"

            if not end_time:
                return "Passwords provide end time"

            if not event_type:
                return "Passwords provide type of event"

            try:
                # Insert test data in events table
                db.execute("INSERT INTO events (user_id, name, date, start_time, end_time, event_type, event_grade) VALUES (?, ?, ?, ?, ?, ?, ?)",user_id, event_name, date, start_time, end_time, event_type, event_grade)
            except:
                return "Error cannot create event"

        return redirect("/calender")


@app.route("/query", methods=["GET", "POST"])
def query():
    """Submit query about event"""

    if not session.get("user_id"):
        return redirect("/login")
    else:
        if request.method == "GET":
            return render_template("query.html")

        else:
            event_id = request.form.get("event_id")
            result = db.execute("SELECT * FROM events WHERE event_id = ?", int(event_id))
            creator = db.execute("SELECT fname, lname FROM users WHERE user_id = (SELECT user_id FROM events WHERE event_id = ?)", int(event_id))
            return render_template("result.html", result=result, creator=creator)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)

        # Ensure password was submitted
        elif not request.form.get("password"):
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return render_template('login.html', error=error)

        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Clear any user_id and redirect user to login form
    session.clear()
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "GET":
        return render_template("register.html")

    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        position = request.form.get("position")

        # Name validation
        if not fname:
            return "Must provide Username!"
        if not lname:
            return "Must provide Username!"

        # Password validation
        if not password:
            return "Must provide Password!"

        if not confirmation:
            return "Must provide password confirmation!"

        if password != confirmation:
            return "Passwords do not match"

        username = (fname + "." + lname).lower()

        hash_pwd = generate_password_hash(password)

        try:
            new_user = db.execute("INSERT INTO users (fname, lname, username, password, position) VALUES (?, ?, ?, ?, ?)", fname, lname, username, hash_pwd, position)
        except:
            error = 'User already exist!'
            return render_template('register.html', error=error)
        session["user_id"] = new_user
        return redirect("/")

