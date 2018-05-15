from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def first_route():
    return render_template('first_route.html')
@app.route('/ninja')
def ninja():
    return render_template('ninjas.html')
@app.route('/ninja/<colors>')
def ninja_blue(colors):
    return render_template('red_ninja.html', color=colors)
app.run(debug = True)