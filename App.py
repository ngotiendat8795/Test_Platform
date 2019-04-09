from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('Homepage.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/create')
def create():
    return render_template('Create_Acc.html')

@app.route('/ielts')
def ielts():
    return render_template('Ielts_Section.html')

@app.route('/ielts/cambridge')
def cambridge():
    return render_template('Ielts_Cambridge.html')

@app.route('/ielts/cambridge/reading-intro')
def reading_intro():
    return render_template('Reading_Intro.html')

@app.route('/ielts/cambridge/reading-intro/reading-test')
def reading_test():
    return render_template('Reading_Test.html')

@app.route('/ielts/cambridge/listening-intro')
def listening_intro():
    return render_template('Listening_Intro.html')

@app.route('/ielts/cambridge/listening-intro/listening-test')
def listening_test():
    return render_template('Listening_Test.html')

@app.route('/ielts/cambridge/writing-intro')
def writing_intro():
    return render_template('Writing_Intro.html')

@app.route('/ielts/cambridge/writing-intro/writing-test')
def writing_test():
    return render_template('Writing_Test.html')

@app.route('/ielts/cambridge/result')
def result():
    return render_template('Result.html')


if __name__ == '__main__':
    app.run(debug=True)
 