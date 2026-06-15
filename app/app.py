from flask import Flask, render_template, request, redirect, url_for

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

        report={
            "name":name,
            "location":location,
            "title":title,
            "description":description
        }
        reports.append(report)
        print(reports)

        return redirect(url_for("issues"))
       
    return render_template("report.html")

@app.route("/issues")
def issues():
    return render_template("issues.html", reports=reports)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)