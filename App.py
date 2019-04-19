from flask import *
from bson.objectid import ObjectId
from users import users
app = Flask(__name__)

# HomePage
@app.route('/')
def index():
  if 'username' in session:
    return render_template('index.html', session = session)
  else:
    return render_template('index.html')


# Ielts Section
@app.route('/ielts-section')
def ielts_section():
  if 'username' in session:
    return render_template('Ielts_Section.html', session = session)
  else:
    return render_template('Ielts_Section.html')


# Sign Up
@app.route('/sign-up', methods = ["POST", "GET"])
def sign_up():
  if request.method == "GET":
    return render_template("sign-up.html")
  elif request.method == "POST":
    form = request.form
    full_name = form["name"]
    username = form["username"]
    password = form["password"]
    exist_user = users.find_one({"username" : username})
    if exist_user == None:
      new_user = {
        "full_name" : full_name,
        "username" : username,
        "password" : password,
        "test" : []
      }
      users.insert_one(new_user)
      return redirect(url_for('login'))
    else:
      display_error = "This username has been used"      
      return render_template("sign-up.html", display_error = display_error)


# Sign in
@app.route('/login', methods = ["POST", "GET"])
def login():
  if 'username' not in session:
    if request.method == "GET":
      return render_template('login.html')
    elif request.method == "POST":
      form = request.form
      username = form["username"]
      password = form["password"]
      login_user = users.find_one({"username" : username})
      
      if login_user:
        if password == login_user['password']:
          session["username"] = username
          return redirect(url_for('index'))
        else:
          wrong_password = "Wrong password"        
          return render_template('login.html', wrong_password = wrong_password)
      else:
        wrong_username = "Wrong username"
        return render_template('login.html', wrong_username = wrong_username)
  else:
    return redirect('/')


# Sign out
@app.route('/logout')
def logout():
  del session['username']
  return redirect('/')
    

@app.route('/ielts/result')
def result():
    return render_template('Result.html')


if __name__ == '__main__':
    app.secret_key = '123456789'
    app.run(debug=True)
 