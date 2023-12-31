import os

import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session["user_id"]
    transactions_db = db.execute(
        "SELECT symbol, name, SUM(shares) AS shares, price FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    balance_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    balance = balance_db[0]["cash"]

    total = balance
    for item in transactions_db:
        total += item["price"] * item["shares"]

    return render_template("index.html", database=transactions_db, balance=usd(balance), total=usd(total), usd=usd)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "GET":
        return render_template("buy.html")

    else:
        symbol = request.form.get("symbol")

        # Validate symbol
        if not symbol:
            return apology("Must provide symbol!")

        stock = lookup(symbol.upper())

        if not stock:
            return apology("Symbol does not exist!")

        # Validate shares
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Shares must be an integer!")

        if shares <= 0:
            return apology("Shares must be positive integer!")

        item_name = stock["name"]
        item_price = stock["price"]
        transaction_value = shares * item_price
        user_id = session["user_id"]
        user_balance_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_balance = user_balance_db[0]["cash"]

        if user_balance < transaction_value:
            return apology("Not enough money to buy!")
        else:
            update_balance = user_balance - transaction_value

            db.execute("UPDATE users SET cash = ? WHERE id = ?", update_balance, user_id)

            date = datetime.datetime.now()
            db.execute("INSERT INTO transactions (user_id, name, symbol, shares, price, date, type) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       user_id, item_name, stock["symbol"], shares, item_price, date, 'Buy')

            flash("Shares bought!")

            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions_db = db.execute("SELECT * FROM transactions WHERE user_id = ?", user_id)
    return render_template("history.html", transactions=transactions_db)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request .method == "GET":
        return render_template("/quote.html")
    else:
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Must provide symbol!")

        stock = lookup(symbol.upper())

        if not stock:
            return apology("Symbol does not exist!")

        return render_template("quoted.html", name=stock["name"], price=usd(stock["price"]), symbol=stock["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "GET":
        return render_template("register.html")

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Username validation
        if not username:
            return apology("Must provide Username!")

        # Password validation
        if not password:
            return apology("Must provide Password!")

        if not confirmation:
            return apology("Must provide password confirmation!")

        if password != confirmation:
            return apology("Passwords do not match")

        hash_pwd = generate_password_hash(password)
        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_pwd)
        except:
            return apology("Username already exist!")

        session["user_id"] = new_user
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        symbols_user = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", user_id)
        return render_template("sell.html", symbols=[row["symbol"] for row in symbols_user])
    else:
        user_id = session["user_id"]
        symbol = request.form.get("symbol")

        # Validate symbol
        if not symbol:
            return apology("Must provide symbol!")

        stock = lookup(symbol.upper())

        if not stock:
            return apology("Symbol does not exist!")

        # Validate shares
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Shares must be an integer!")

        if shares <= 0:
            return apology("Shares must be a positive number!")

        item_name = stock["name"]
        item_price = stock["price"]

        user_shares = db.execute("SELECT shares FROM transactions WHERE user_id=? AND symbol =? GROUP BY symbol", user_id, symbol)
        user_shares_real = user_shares[0]["shares"]

        if shares > user_shares_real:
            return apology("You do not possess this amount of shares!")

        user_balance_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_balance = user_balance_db[0]["cash"]

        transaction_value = shares * item_price
        update_balance = user_balance + transaction_value

        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_balance, user_id)

        date = datetime.datetime.now()
        db.execute("INSERT INTO transactions (user_id, name, symbol, shares, price, date, type) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   user_id, item_name, stock["symbol"], -shares, item_price, date, 'Sell')

        flash("Sold!")

        return redirect("/")


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """User can add cash to account"""
    if request.method == "GET":
        return render_template("add.html")
    else:
        add_cash = int(request.form.get("add_cash"))

        # Validate cash
        if not add_cash:
            return apology("Must provide value to add cash!")

        user_id = session["user_id"]
        user_balance_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_balance = user_balance_db[0]["cash"]

        update_balance = user_balance + add_cash

        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_balance, user_id)
        return redirect("/")


@app.route("/change_pwd", methods=["GET", "POST"])
def change_pwd():
    """User can change password"""
    user_id = session["user_id"]
    if request.method == "GET":
        return render_template("change.html")

    else:
        password = request.form.get("password")
        confirmation = request.form.get("confirm")

        # Password validation
        if not password:
            return apology("Must provide Password!")

        if not confirmation:
            return apology("Must provide password confirmation!")

        if password != confirmation:
            return apology("Passwords do not match")

        hash_pwd = generate_password_hash(password)

        # Update record
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash_pwd, user_id)
        return redirect("/")

