from flask import Flask,render_template,request,redirect, url_for,jsonify, json
from base import db
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import random
import re


app = Flask(__name__, template_folder="app")
login_manager = LoginManager()
login_manager.login_view = "http://127.0.0.1:5000/form" #page error
login_manager.init_app(app)
app.config.update(
    SECRET_KEY = 'SIA'
)

data = {

}


def check_string(string):
    
    phone = re.sub(r'\b\D', '', string)
    clear_phone = re.sub(r'[\ (]?', '', phone)
    if re.findall(r'^[+7|8]?\d{10}$', clear_phone) or re.match(r'^\w+[.]?(\w+)@(\w+.)*\w{2,}$',string):
        return(bool(string))
    else: return(False)

class User(UserMixin):
    def __init__(self, id):
        self.id = id
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

#registers
@app.route('/form/' )
def form_get():
    return render_template('form2.html')


@app.route('/login/', methods=['POST'])
def login_post_form():
    print(request.form)
   
    i = db.users.get("number", request.form["number"])

    if not i:
         return 'err'
    if request.form['number'] != i.number:
        return 'err1' #errors
    if request.form['password'] != i.password:
        return 'err2'
    _user = User(request.form['number'])
    login_user(_user)


    return redirect("http://127.0.0.1:5000/home")


@app.route('/register/', methods=['POST'])
def register(): 
    print(request.form)
    if not request.form["password"] or not request.form["number"] or not request.form["id"]:
        return 'err3' # error 4...
    



    try:
        db.users.put(request.form)
    except:
        return 'err4' # error 400
    _user = User(request.form["number"])
    login_user(_user)
    return redirect('http://127.0.0.1:5000/home')





@app.route('/home/')
@login_required
def index():

   
        
    statick = [
        {
        'invalid': 'none',
        }
    ]
    return render_template('test.html', statick=statick,data = data )



@app.route('/api/')
def api():
    global output
    io = db.users.get_all()
    for i in io:
        data[i.id] = i.login
        o = random.choice(list(data.items()))
        output = ", ".join(o)
    return jsonify(output)

if __name__ == "__main__":
    app.run()