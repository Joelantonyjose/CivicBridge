from flask import Flask, render_template, request, redirect, url_for,flash
import sqlite3

app= Flask(__name__)
app.secret_key="civicbridge_secret"

reports = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report", methods=["GET","POST"])
def report():
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
            "INSERT INTO reports (name, location, title, description, status) VALUES (?, ?, ?, ?, ?)",
            (name, location, title, description, "Pending")
        )
        conn.commit()
        conn.close()
        
        return redirect(url_for("issues"))
       
    return render_template("report.html")

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
    conn = sqlite3.connect("civicbridge.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM reports WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()
    
    return redirect(url_for("issues"))

@app.route("/resolve/<int:id>")
def resolve(id):
    conn=sqlite3.connect("civicbridge.db")
    cursor=conn.cursor()

    cursor.execute(
        "UPDATE reports SET status=? WHERE id=?",
        ("Resolved",id)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("issues"))

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    conn=sqlite3.connect("civicbridge.db")
    cursor=conn.cursor()

    if request.method=="POST":
        title=request.form["title"]
        description=request.form["description"]

        cursor.execute(
            """
            UPDATE reports
            SET title=?,description=?
            WHERE id=?
            """,
            (title,description,id)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("issues"))

    cursor.execute(
        "SELECT * FROM reports WHERE id = ?",
        (id,)
    )
    report=cursor.fetchone()
    conn.close()
    return render_template("edit.html",report=report)

if __name__=="__main__":
    app.run(debug=True)