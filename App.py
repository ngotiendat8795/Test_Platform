from flask import *
from bson.objectid import ObjectId
from users import users
app = Flask(__name__)

from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:admin@c4e28cluster-chzuv.mongodb.net/test?retryWrites=true"

client = MongoClient(mongo_uri)
ielts_database = client.db_ielts

reading_test = ielts_database["Reading_Test"]
writing_test = ielts_database["Writing_Test"]
reading_answer = ielts_database["reading_answer"]
answer_key = ielts_database["Answer_Key"]
band_score = ielts_database["Band_Score"]

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
    

@app.route('/ielts/ielts-cambridge<id1>/reading-test<id2>', methods = ["GET", "POST"])
def reading_template(id1,id2):
    if request.method == "GET":
        Test_ID = "IC"+str(id1)+"_T"+str(id2)
        Test_Content = reading_test.find_one({"Test_ID":Test_ID})
        return render_template('Reading_Test.html', Test_Content=Test_Content)
    elif request.method == "POST":
      Test_ID = "IC"+str(id1)+"_T"+str(id2)
      time_accessed = reading_answer.find({"USER":"ngotiendat8795","TEST_ID": Test_ID,"Section" : "R"}).count()
      form = request.form
      answer_sheet = {
      "USER":session['username'],
      "TEST_ID": Test_ID,
      "Section" : "R",
      "Time_Acessed" : time_accessed + 1,
      }
      for i in range(1,41):

        answer_id = "IC"+str(id1)+"_T"+str(id2)+"_R_"+str(i)
        try:
          answer_value = form[answer_id]
          if answer_value == "":
            answer_value = "N/A"
        except KeyError:
          answer_value = "N/A"
        answer_sheet[answer_id] = answer_value
      reading_answer.insert_one(answer_sheet)
      return redirect('/ielts/ielts-cambridge{0}/reading-test{1}/result'.format(id1,id2))


@app.route('/ielts/ielts-cambridge<id1>/listening-test<id2>', methods = ["GET", "POST"])
def listening_test(id1,id2):
    if request.method == "GET":
        return render_template('Listening_Test.html')
    elif request.method == "POST":
      Test_ID = "IC"+str(id1)+"_T"+str(id2)
      time_accessed = reading_answer.find({"USER":"ngotiendat8795","TEST_ID": Test_ID,"Section" : "L"}).count()
      form = request.form
      answer_sheet = {
      "USER":session["username"],
      "TEST_ID": Test_ID,
      "Section" : "L",
      "Time_Acessed" : time_accessed + 1,
      }
      for i in range(1,41):

        answer_id = "IC"+str(id1)+"_T"+str(id2)+"_L_"+str(i)
        try:
          answer_value = form[answer_id]
          if answer_value == "":
            answer_value = "N/A"
        except KeyError:
          answer_value = "N/A"
        answer_sheet[answer_id] = answer_value
      reading_answer.insert_one(answer_sheet)
      return redirect('/ielts/ielts-cambridge{0}/listening-test{1}/result'.format(id1,id2))
  

@app.route('/ielts/ielts-cambridge<id1>/writing-test<id2>',methods = ["GET", "POST"])
def writing_template(id1,id2):
    if request.method == "GET":
      Test_ID = "IC"+str(id1)+"_T"+str(id2)
      Test_Content = writing_test.find_one({"Test_ID":Test_ID})
      return render_template('Writing_Test.html', Test_Content=Test_Content)
    elif request.method == "POST":
      Test_ID = "IC"+str(id1)+"_T"+str(id2)
      time_accessed = reading_answer.find({"USER":"ngotiendat8795","TEST_ID": Test_ID,"Section" : "W"}).count()
      form = request.form
      answer_sheet = {
      "USER":session["username"],
      "TEST_ID": Test_ID,
      "Section" : "W",
      "Time_Acessed" : time_accessed + 1,
      }
      for i in range(1,3):

        answer_id = "IC"+str(id1)+"_T"+str(id2)+"_W_"+str(i)
        try:
          answer_value = form[answer_id]
          if answer_value == "":
            answer_value = "N/A"
        except KeyError:
          answer_value = "N/A"
        answer_sheet[answer_id] = answer_value
      reading_answer.insert_one(answer_sheet)
      return redirect('/ielts/ielts-cambridge{0}/writing-test{1}/result'.format(id1,id2))

@app.route('/ielts/ielts-cambridge<id1>/<id3>-test<id2>/result')
def result(id1,id2,id3):
  Test_ID = "IC"+str(id1)+"_T"+str(id2)
  reading_history = reading_answer.find({"USER":session['username'],"TEST_ID": Test_ID,"Section" : "R"})
  time_accessed_r = reading_history.count()
  if time_accessed_r >= 1:
    latest_result_r = reading_history[time_accessed_r-1]

  listening_history = reading_answer.find({"USER":session['username'],"TEST_ID": Test_ID,"Section" : "L"})
  time_accessed_l = listening_history.count()
  if time_accessed_l >= 1:
    latest_result_l = listening_history[time_accessed_l-1]

  writing_history = reading_answer.find({"USER":session['username'],"TEST_ID": Test_ID,"Section" : "W"})
  time_accessed_w = writing_history.count()
  if time_accessed_w >= 1:
    latest_result_w = writing_history[time_accessed_w-1]

  if id3 == "reading":
    return render_template('Result_R.html',Test_ID=Test_ID,Answer_Key=answer_key,reading_history=reading_history,latest_result_r=latest_result_r,band_score=band_score)
  elif id3 == "listening":
    return render_template('Result_L.html',Test_ID=Test_ID,Answer_Key=answer_key,listening_history=listening_history,latest_result_l=latest_result_l,band_score=band_score)
  else:
    return render_template('Result_W.html',Test_ID=Test_ID,Answer_Key=answer_key,writing_history=writing_history,latest_result_w=latest_result_w)



if __name__ == '__main__':
    app.secret_key = '123456789'
    app.run(debug=True)
 