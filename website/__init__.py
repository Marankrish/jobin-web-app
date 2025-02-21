from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL


def create_app():
    app = Flask(__name__)

    # Use Railway MySQL credentials
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "Mdcineluv12#"
    app.config["MYSQL_DB"] = "data1"
    app.config["MYSQL_PORT"] = "3306"  # Change if different

    mysql = MySQL(app) 
    jobs = [
    {
        'id': 1,
        'role': 'Data Scientist',
        'location':'Chennai',
        'salary':'10,00,000'
    },
    {
        'id':2,
        'role':'Full Stack Developer',
        'location': 'Bangalore',
        'salary' : '12,00,000'
    },
    {
        'id':3,
        'role':'Front End Designer',
        'location':'Delhi',
        'salary': '8,50,000'
    },
    {
        'id': 4,
        'role': 'AI engineer',
        'location' : 'Noida',
        'salary' : '15,00,000'
    }
    ]

    @app.route('/')
    def home():
        try:
            con = mysql.connection.cursor()
            sql = "SELECT * from jobs"
            con.execute(sql)
            res = con.fetchall()
            con.close()
            return render_template('home.html',JOBS = res)
        except Exception as e:
            print(f"An error occurred: {e}")  # Debugging: Print the error
            return "An error occurred while fetching data from the database.", 500
    
    
    @app.route('/list')
    def list_home():
        try:
            con = mysql.connection.cursor()
            sql = "SELECT * from jobs"
            con.execute(sql)
            res = con.fetchall()
            con.close()
            return jsonify(res)
        except Exception as e:
            return f"An error occurred: {e}", 500
    
    @app.route('/job/<id>')
    def list_jobs(id):
        try:
            con = mysql.connection.cursor()
            sql = "SELECT * from jobs where id = %s"
            con.execute(sql,(id,))
            res = con.fetchone()
            con.close()
            if res:
                return render_template('jobpage.html',JOBS = res)
            else:
                return "job not found", 404
        except Exception as e:
            return f"An error occurred: {e}", 500
    
    @app.route('/job/<id>/apply',methods = ['post'])
    def application(id):
        datas = request.form
        fullname = datas.get("fullname")
        email = datas.get("mail")
        linkedin = datas.get("linkedin")
        education = datas.get("education")
        skills = datas.get("skills")
        resume = datas.get("resume")
        try:
            con = mysql.connection.cursor()
            sql = """INSERT INTO applications (job_id, fullname, email, linkedin_url, education, skills, resume_url) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            values = (id, fullname, email, linkedin, education, skills, resume)
            con.execute(sql, values)
            mysql.connection.commit()
            con.close()
            return render_template('application_submitted.html',info = datas)
        except Exception as e:
            return f"An error occurred: {e}", 500
    return app