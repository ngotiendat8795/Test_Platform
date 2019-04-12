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

@app.route('/ielts/reading-intro')
def reading_intro():
    return render_template('Reading_Intro.html')

@app.route('/ielts/reading-intro/reading-test')
def reading_test():
    return render_template('Reading_Test.html')

@app.route('/ielts/listening-intro')
def listening_intro():
    return render_template('Listening_Intro.html')

@app.route('/ielts/listening-intro/listening-test')
def listening_test():
    return render_template('Listening_Test.html')

@app.route('/ielts/writing-intro')
def writing_intro():
    return render_template('Writing_Intro.html')

@app.route('/ielts/writing-intro/writing-test')
def writing_test():
    return render_template('Writing_Test.html')

@app.route('/ielts/result')
def result():
    return render_template('Result.html')


if __name__ == '__main__':
    app.run(debug=True)
 