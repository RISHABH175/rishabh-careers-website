from flask import Flask, render_template, request, jsonify

app = Flask('__name__')

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru,India',
    'salary': 'Rs 1,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi,India',
    'salary': 'Rs 1,15,000'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'DUBAI,UAE',
    'salary': 'AED 30,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'DUBAI,UAE',
    # 'salary': 'AED 30,000'
  },
]


@app.route('/')
def home():
  return render_template('index.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


app.run(host='0.0.0.0', port=8080, debug=True)
