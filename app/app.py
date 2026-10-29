from flask import Flask, render_template, request, redirect, url_for,flash,session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app= Flask(__name__)
app.secret_key="civicbridge_secret"

reports = []

@app.route("/")
def home():

    conn = sqlite3.connect("civicbridge.db")
    cursor = conn.cursor()

    # Recent Issues
    cursor.execute("""
        SELECT *
        FROM reports
        ORDER BY id DESC
        LIMIT 3
    """)
    recent_reports = cursor.fetchall()

    # Total Reports
    cursor.execute("SELECT COUNT(*) FROM reports")
    total_reports = cursor.fetchone()[0]

    # Pending Reports
    cursor.execute("SELECT COUNT(*) FROM reports WHERE status='Pending'")
    pending_reports = cursor.fetchone()[0]

    # Resolved Reports
    cursor.execute("SELECT COUNT(*) FROM reports WHERE status='Resolved'")
    resolved_reports = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        recent_reports=recent_reports,
        total_reports=total_reports,
        pending_reports=pending_reports,
        resolved_reports=resolved_reports
    )

@app.route("/report", methods=["GET","POST"])
def report():

    if "username" not in session:
        flash("Please log in to report an issue.")
        return redirect(url_for("login"))

    if request.method == "POST":
        name = request.form["name"].strip()
        location = request.form["location"].strip()
        title = request.form["title"].strip()
        description = request.form["description"].strip()

        if not name or not location or not title or not description:
            flash("All fields are required!")
            return redirect(url_for("report"))

        conn=sqlite3.connect("civicbridge.db")
        cursor=conn.cursor()
        cursor.execute(
            "INSERT INTO reports (name, location, title, description, status, username) VALUES (?, ?, ?, ?, ?, ?)",
            (name, location, title, description, "Pending", session["username"])
        )
        conn.commit()
        conn.close()

        flash("✅ Issue reported successfully!")
        
        return redirect(url_for("issues"))
       
    return render_template("report.html")

@app.route("/my-reports")
def my_reports():

    if "username" not in session:
        flash("Please log in to view your reports.")
        return redirect(url_for("login"))

    conn = sqlite3.connect("civicbridge.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM reports WHERE username=?",
        (session["username"],)
    )

    reports = cursor.fetchall()

    conn.close()

    return render_template("my_reports.html", reports=reports)

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        if not username or not password:
            flash("Username and password are required!")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect("civicbridge.db")
        cursor = conn.cursor()

        try:

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()

        except sqlite3.IntegrityError:

            conn.close()

            flash("Username already exists!")

            return redirect(url_for("register"))

        conn.close()

        flash("Registration successful! Please log in.")

        return redirect(url_for("home"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        conn = sqlite3.connect("civicbridge.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):

            session["username"] = username

            session["role"] = user[3]

            flash("Login successful!")

            return redirect(url_for("home"))

        flash("Invalid username or password!")

        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.pop("username", None)

    flash("You have been logged out.")

    return redirect(url_for("home"))

@app.route("/issues")
def issues():
    conn = sqlite3.connect("civicbridge.db")
    cursor=conn.cursor()
    
    status=request.args.get("status")
    search=request.args.get("search")
    

    if search:
        cursor.execute(
            "SELECT * FROM reports WHERE title LIKE ?",
            (f"%{search}%",)
        )
    
    
    elif status:
        cursor.execute(
            "SELECT * FROM reports WHERE status=?",
            (status,)
        )

    else:
        cursor.execute("SELECT * from reports")    
    
    reports=cursor.fetchall()

    conn.close()
    return render_template("issues.html", reports=reports)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/delete/<int:id>")
def delete(id):
    if "username" not in session:
        flash("Please log in to delete an issue.")
        return redirect(url_for("login"))

    if session.get("role") != "Citizen":
        flash("You are not authorized to delete issues.")
        return redirect(url_for("issues"))

    conn = sqlite3.connect("civicbridge.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM reports WHERE id = ? AND username = ?",
        (id, session["username"])
    )
    if cursor.rowcount == 0:
        conn.close()
        flash("You are not authorized to delete this report.")
        return redirect(url_for("issues"))

    conn.commit()
    conn.close()

    flash("🗑️ Issue deleted successfully!")
    return redirect(url_for("issues"))

@app.route("/resolve/<int:id>")
def resolve(id):
    if "username" not in session:
        flash("Please log in to resolve an issue.")
        return redirect(url_for("login"))

    if session.get("role") != "Representative":
        flash("You are not authorized to resolve issues.")
        return redirect(url_for("issues"))

    conn=sqlite3.connect("civicbridge.db")
    cursor=conn.cursor()

    cursor.execute(
        "UPDATE reports SET status=? WHERE id=?",
        ("Resolved",id)
    )

    conn.commit()
    conn.close()

    flash("✅ Issue marked as resolved!")
    return redirect(url_for("issues"))

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    if "username" not in session:
        flash("Please log in to edit an issue.")
        return redirect(url_for("login"))

    if session.get("role") != "Citizen":
        flash("You are not authorized to edit issues.")
        return redirect(url_for("issues"))

    conn=sqlite3.connect("civicbridge.db")
    cursor=conn.cursor()

    if request.method=="POST":
        title=request.form["title"]
        description=request.form["description"]

        cursor.execute(
            """
            UPDATE reports
            SET title=?,description=?
            WHERE id=? AND username=?
            """,
            (title,description,id,session["username"])
        )

        conn.commit()
        conn.close()

        flash("✏️ Issue updated successfully!")

        return redirect(url_for("issues"))

    cursor.execute(
        "SELECT * FROM reports WHERE id = ?",
        (id,)
    )
    report=cursor.fetchone()

    if report is None:
        conn.close()
        flash("Report not found.")
        return redirect(url_for("issues"))

    if report[6] != session["username"]:
        conn.close()
        flash("You are not authorized to edit this report.")
        return redirect(url_for("issues"))
    
    if report[5]=="Resolved":
        conn.close()
        flash("This report has already been resolved and cannot be edited.")
        return redirect(url_for("issues"))
    
    conn.close()
    return render_template("edit.html",report=report)

@app.route("/representative-dashboard")
def representative_dashboard():

    if "username" not in session:
        flash("Please log in to access the Representative Dashboard.")
        return redirect(url_for("login"))

    if session.get("role") != "Representative":
        flash("You are not authorized to access the Representative Dashboard.")
        return redirect(url_for("home"))

    conn = sqlite3.connect("civicbridge.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM reports")
    total_reports = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reports WHERE status='Pending'")
    pending_reports = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reports WHERE status='Resolved'")
    resolved_reports = cursor.fetchone()[0]

    status = request.args.get("status", "Pending")

    if status not in ["Pending", "Resolved"]:
        status = "Pending"

    cursor.execute(
        "SELECT * FROM reports WHERE status = ? ORDER BY id DESC",
        (status,)
    )

    report_list = cursor.fetchall()
    conn.close()

    return render_template(
        "representative_dashboard.html",
        total_reports=total_reports,
        pending_reports=pending_reports,
        resolved_reports=resolved_reports,
        report_list=report_list,
        selected_status=status
    )

if __name__=="__main__":
    app.run(debug=True)


