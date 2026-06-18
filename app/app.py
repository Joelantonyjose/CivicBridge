from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app= Flask(__name__)

reports = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report", methods=["GET","POST"])
def report():
    if request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]
        title = request.form["title"]
        description = request.form["description"]

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
    cursor.execute("SELECT * FROM reports")
    reports=cursor.fetchall()
    print(reports)

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

if __name__=="__main__":
    app.run(debug=True)