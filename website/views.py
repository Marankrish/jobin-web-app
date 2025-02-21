from flask import Blueprint,render_template,jsonify
views = Blueprint('views',__name__)
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
@views.route('/views')
def home():
    return render_template('home.html',JOBS = jobs)

@views.route('/list')
def list_jobs():
    return jsonify(jobs)    
