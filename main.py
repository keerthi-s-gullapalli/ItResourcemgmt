from flask import Flask, render_template, request
import DB_Connect
import os
import GenerateStatsGraph

APP_FOLDER = os.path.join('static', 'images_folder')


app = Flask('__name__')
app.config['UPLOAD_FOLDER'] = APP_FOLDER


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login',methods=['POST', 'GET'])
def login():
    print("inside login method")
    return render_template("login.html")



@app.route('/update_Profile', methods=['POST','GET'])
def update_Profile():
    print("inside update profile method")
    userDetails = dict()
    userDetails['Fname'] = request.form['FName']
    userDetails['Lname'] = request.form['LName']
    userDetails['Email'] = request.form['Email']
    userDetails['Addr1'] = request.form['Addr1']
    userDetails['Addr2'] = request.form['Addr2']
    userDetails['City'] = request.form['City']
    userDetails['State'] = request.form['State']
    userDetails['Pin'] = request.form['Pin']
    print("Update Profile dictionary values",userDetails)
    returnString = DB_Connect.updateUserProfile(userDetails)
    return render_template('userProfile.html', returnMessage=returnString,return_value=request.form['Email'])

@app.route('/form_login', methods=['POST', 'GET'])
def login_validate():
    user_name = request.form['0']
    pwd = request.form['passWord']
    returnString = DB_Connect.getUserDetails(user_name, pwd)
    print("return value after calling getuser details=",returnString)
    if returnString == "valid":
        print('User Name= ' + user_name)
        print('Password = ' + pwd)
        GenerateStatsGraph.generateGraph(DB_Connect.getUserStats(user_name),user_name)
        if("admin" in user_name):
            full_filename=os.path.join(app.config['UPLOAD_FOLDER'], 'AdminGraph.png')
        else:
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], user_name+'_loginGraph.png')
        print("image path=" + full_filename)
        return render_template("userProfile.html", return_value=user_name,user_image=full_filename)
    else:
        return render_template('login.html', return_value=returnString)



@app.route('/register_User', methods=['POST', 'GET'])
def register_User():
    return render_template("userRegistration.html")

@app.route('/forgot_Pwd', methods=['POST','GET'])
def forgot_Pwd():
    return render_template("ForgotPwd.html")



@app.route('/update_Pwd', methods=['POST', 'GET'])
def update_Pwd():
    print("insde update method")
    user_name=request.form['userName']
    pwd=request.form['Pwd']
    print("User name=",user_name)
    print("password=",pwd)
    returnString = DB_Connect.updateUserDetails(user_name, pwd)
    return render_template('login.html', return_value=returnString)

@app.route('/display_Profile', methods=['POST','GET'])
def display_Profile():
    print("inside display profile")
    print("Inside display profile - user name=",request.form['user_name'])
    userProfile=DB_Connect.getUserProfile(request.form['user_name'])
    return render_template('updateProfile.html', result=userProfile)

@app.route('/list_users', methods=['POST','GET'])
def display_users():
    userDetails=DB_Connect.getAllUsers("login")
    return render_template('userLoginData.html', result=userDetails)

@app.route('/list_Allusers', methods=['POST','GET'])
def display_Allusers():
    userDetails=DB_Connect.getAllUsers("all")
    return render_template('userData.html', result=userDetails)


@app.route('/create_User', methods=['POST', 'GET'])
def create_User():
    print("Inside the method")
    userDetails = dict()
    userDetails['Fname'] = request.form['FName']
    userDetails['Lname'] = request.form['LName']
    userDetails['Email'] = request.form['Email']
    userDetails['Addr1'] = request.form['Addr1']
    userDetails['Addr2'] = request.form['Addr2']
    userDetails['City'] = request.form['City']
    userDetails['State'] = request.form['State']
    userDetails['Pin'] = request.form['Pin']
    userDetails['Pwd'] = request.form['Pwd']
    returnString = DB_Connect.createUserDetails(userDetails)
    return render_template('index.html', return_value=returnString)
    # define a new py file that has class and methods to create a new user.  call that here
    # design new register user form to accept the details of the user and call that html using render template here


if __name__ == "__main__":
    app.run()
