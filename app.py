from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Houston, TX',
        'salary': '$210,000'
    },
    {
        'id': 2,
        'title': 'Network Engineer',
        'location': 'San Francisco, CA',
        'salary': '$250,000'
    },
    {
        'id': 3,
        'title': 'Software Testing Engineer',
        'location': 'Remote',
        
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs = JOBS, company_name="Jovian")

@app.route("/ap/jobs")
def list_jobs():
    return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)