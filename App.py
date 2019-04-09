from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/ielts')
def ielts():
    return render_template('ielts.html')

@app.route('/ielts/cambridge')
def cambridge():
    return render_template('cambridge.html')

@app.route('/ielts/cambridge/reading-intro')
def reading_intro():
    return render_template('reading-intro.html')

@app.route('/ielts/cambridge/reading-intro/reading-test')
def reading_test():
    return render_template('reading-test.html')

@app.route('/ielts/cambridge/listening-intro')
def listening_intro():
    return render_template('listening-intro.html')

@app.route('/ielts/cambridge/listening-intro/listening-test')
def listening_test():
    return render_template('listening-test.html')

@app.route('/ielts/cambridge/writing-intro')
def writing_intro():
    return render_template('writing-intro.html')

@app.route('/ielts/cambridge/writing-intro/writing-test')
def writing_test():
    return render_template('writing-test.html')

@app.route('/ielts/cambridge/result')
def result():
    return render_template('result.html')

@app.route('/user-profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
 